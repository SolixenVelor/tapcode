def planner_prompt(user_prompt: str):
    # PLANNER PROMPT
    planner_prompt = f""" 
    You are the PLANNER agent. Convert the user prompt into a COMPLETE engineering project plan 
    User request: {user_prompt}
    """
    return planner_prompt


def arch_prompt(plan: str):
    # ARCHITECT PROMPT
    arch_prompt = f"""
You are ARCHITECT agent, Given this project plan, break it down into explicit engineering tasks. 

RULES :
- For each FILE in the pla, create one or more IMPLEMENTATION TASKS. 
- In each task description:
    * Specifiy exactly what to implement. 
    * Name the variables, functions, classes, and components to be defined. 
    * Mention how this depends on or will be used by previous tasks. 
    * Include integration details: imports, expected function signatures, data flow. 
- Order tasks so that dependencies are implemented first. 
- Each step must be SELF-CONTAINED but also carry FORWARD the relevant context from earlier tasks.

Project Plan:
{plan}
    """
    return arch_prompt

def coder_system_prompt() -> str:
    CODER_SYS_PROMPT = """
You are CODER agent. 
You are implementing a specific engineering task. 
You have access to tools to read and write files.

Always:
- Review all existing files to maintain compatiblility.
- Implement the FULL file content, integrating with other modules.
- Maintain consistent naming of variables, functions, and imports.
- When a module is imported from another file, ensure it exists and is implemented
"""
    return CODER_SYS_PROMPT