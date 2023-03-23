#Write an web API using FASTAPI framwork in python which will execute  a shell script in a server 

import subprocess
import os

def run_shell_script(script_path):
    # check if script path is valid
    if os.path.isfile(script_path):
        # run the shell script
        return subprocess.call(script_path, shell=True)
    else:
        raise ValueError("Invalid script path")

from fastapi import FastAPI
from starlette.responses import JSONResponse

app = FastAPI()

@app.post("/run-shell-script")
def run_script(script_path: str):
    try:
        # call the run_shell_script function
        result = run_shell_script(script_path)
        # return the result
        return JSONResponse(status_code=200, content={"result": result})
    except ValueError as e:
        return JSONResponse(status_code=400, content={"message": str(e)})
