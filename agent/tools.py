import pathlib
import subprocess
from typing import Tuple
from langchain_core.tools import tool

PROJECT_ROOT = pathlib.Path.cwd() / "generated_proj"

def safe_path_for_proj(path: str) -> pathlib.Path:
    p = (PROJECT_ROOT/path).resolve()
    if PROJECT_ROOT.resolve() not in p.parents and PROJECT_ROOT.resolve() != p.parent and PROJECT_ROOT.resolve() != p:
        # guard rail
        raise ValueError("Attempt to write outside project root")
    return p

@tool
def write_file(path: str, content: str) -> str:
    """ writes content to a file at the specified path within the project root"""
    p = safe_path_for_proj(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(content)
    return f"WROTE:{p}"

@tool
def read_file(path: str) -> str:
    """ REads content from a file at the specified path within the project root."""
    p = safe_path_for_proj(path)
    if not p.exists():
        return ""
    with open(p, "r", encoding="utf-8") as f:
        return f.read()
    
@tool
def get_current_directory() -> str:
    """ Returns current working directory"""
    return str(PROJECT_ROOT)

@tool
def list_files(directory: str=".") -> str:
    """ Lists all files in the specified directory within the project root."""
    p = safe_path_for_proj(directory)
    if not p.is_dir():
        return f"ERROR {p} is not a directory"
    files = [str(f.relative_to(PROJECT_ROOT)) for f in p.glob("**/*") if f.is_file()]
    return "\n".join(files) if files else "No files found"

@tool
def run_cmd(cmd: str, cwd: str=None, timeout: int=30) -> Tuple[int, str, str]:
    """ Runs a shell command in the specified dir and return result. """
    cwd_dir = safe_path_for_proj(cwd) if cwd else PROJECT_ROOT
    res = subprocess.run(cmd, shell=True, cwd=str(cwd_dir), capture_output=True, text=True, timeout=timeout)
    return res.returncode, res.stdout, res.stderr

def init_project_root():
    PROJECT_ROOT.mkdir(parents=True, exist_ok=True)
    return str(PROJECT_ROOT)