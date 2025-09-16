# Creating class that inherits from BaseModel defines data schema with built-in validation, 
# serialization, and type enforcement.
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

class File(BaseModel):
    path: str = Field(description="The path to the file to be created or modified")
    purpose: str=Field(description="The purpose fo the file, e.g. 'main app logic', 'data processing module', etc.")

class Plan(BaseModel):
    name :str = Field(description="The name of app to be built")
    description: str=Field(description="A online description of the app to be built, eg 'A web application for managing personal finances'")
    techstack: str=Field(description="The tech stack to be used for the app, e.g. python, javascript, react, flask, etc.")
    features: list[str]=Field(description="A list of features that the app should have, e.g. 'user authentication', 'data visualization', etc.")
    files: list[File] = Field(description="A list of files to be created, each with a 'path' and 'purpose'")

class ImplementationTask(BaseModel):
    filepath: str = Field(description="The path to the file to be modified")
    task_description: str = Field(description="A detailed description of the task to be performed on the file, e.g. 'add user authentication', 'implement data processing logic', etc.")

class TaskPlan(BaseModel):
    implementation_steps: list[ImplementationTask] = Field(description="A list of steps to be taken to implement the task")
    model_config = ConfigDict(extra="allow") # makes BaseModel obj to allow adding extra element to it

class CoderState(BaseModel):
    task_plan: TaskPlan = Field(description="The plan for the task to be implemented")
    cur_step_i: int = Field(0, 
        description="The index of the current step in the implementation steps")
    cur_file_content: Optional[str] = Field(None, 
        description="The content of the file currently being edited or created")


