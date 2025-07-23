import os
import subprocess
import sys

from google.genai import types


def run_python_file(working_directory, file_path, args=None):
    if args is None:
        args = []

    path = os.path.join(working_directory, file_path)
    abs_working_dir = os.path.abspath(working_directory)
    abs_path = os.path.abspath(path)

    if not abs_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_path):
        return f'Error: File "{file_path}" not found.'
    if not abs_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        commands = ['python', abs_path]
        commands.extend(args)

        complete_process = subprocess.run(
            commands,
            cwd=working_directory,
            timeout=30,
            capture_output=True, 
            text=True,
            check=False,
        )

        output = []
        if complete_process.stdout:
            output.append(f"STDOUT:\n{complete_process.stdout.strip()}")
        if complete_process.stderr:
            output.append(f"STDERR:\n{complete_process.stderr.strip()}")

        if complete_process.returncode != 0:
            # Include error code and captured output for better debugging
            error_msg = f"Process exited with code: {complete_process.returncode}"
            if output:
                error_msg += "\n" + "\n".join(output)
            return error_msg

        return "\n".join(output) if output else "No output produced."

    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="runs the python file provided",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="the file to run",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="the arguments to be passed to the python file",
            ),
        },
        required=["file_path"],
    ),
)
