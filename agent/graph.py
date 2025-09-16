from langchain_groq import ChatGroq
from langgraph.constants import END
from langgraph.graph import StateGraph
from langgraph.prebuilt import create_react_agent

from dotenv import load_dotenv
from states import *
from prompts import *
from tools import *
load_dotenv()

llm = ChatGroq(model="openai/gpt-oss-120b") 

def planner_agent(state: dict)-> dict:
    users_prompt = state["user_prompt"]
    # langchain has with_structured_output which specifies output schema
    res = llm.with_structured_output(Plan).invoke(planner_prompt(user_prompt))
    if res is None:
        raise ValueError("Architect didnt return valid response")
    return {"plan": res}

def arch_agent(state: dict) -> dict:
    plan: Plan = state["plan"]  # plan is type hinted to be of class Plan
    res = llm.with_structured_output(TaskPlan).invoke(arch_prompt(plan=plan))
    if res is None:
        raise ValueError("Architect didnt return valid response")
    res.plan = plan   # we are able to add because model_config extra is set to allow
    return {"task_plan": res}

def coder_agent(state: dict) -> dict:
    coder_state = state.get("coder_state")
    if coder_state is None:
        coder_state = CoderState(task_plan=state["task_plan"], cur_step_i=0)
    steps = coder_state.task_plan.implementation_steps
    if coder_state.cur_step_i >= len(steps):
        return {
            "coder_state": coder_state,
            "status": "DONE"
        }

    current_task = steps[coder_state.cur_step_i]
    existing_content = read_file.run(current_task.filepath)
    user_prompt = (
        f"Task: {current_task.task_description}\n"
        f"File: {current_task.filepath}\n"
        f"Existing content: \n{existing_content}\n"
        "Use write_file(path, content) to save your changes."
    )
    system_prompt = coder_system_prompt()
    # resp = llm.invoke(system_prompt + user_prompt)
    coder_tools = [read_file, write_file, list_files, get_current_directory]
    react_agent = create_react_agent(llm, coder_tools)
    react_agent.invoke({
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    })
    coder_state.cur_step_i += 1
    return {"coder_state": coder_state}

# state = {
#     "user_prompt": user_prompt,
#     "plan":  ""
# }

graph = StateGraph(dict)
graph.add_node("planner", planner_agent)
graph.add_node("architect", arch_agent)
graph.add_node("coder", coder_agent)

graph.add_edge("planner", "architect")
graph.add_edge("architect", "coder")
graph.add_conditional_edges(
    "coder",
    lambda s: "END" if s.get("status")=="DONE" else "coder",
    {"END": END, "coder": "coder"}
)

graph.set_entry_point("planner")
agent = graph.compile()

if __name__ == "__main__":
    user_prompt = "Create a simple calculator web application"

    result = agent.invoke({"user_prompt": user_prompt}, {"recursion_limit": 100})
    print(result)