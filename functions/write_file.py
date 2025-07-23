import os

from google.genai import types


def write_file(working_directory, file_path, content):
    path = os.path.join(working_directory, file_path)
    abs_working_dir = os.path.abspath(working_directory)
    abs_path = os.path.abspath(path)
    if not abs_path.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        os.makedirs(os.path.dirname(abs_working_dir), exist_ok=True)


        with open(abs_path, 'w') as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error writing to file "{file_path}": {e}'

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="writes to file, if file doesn't exist, make it and write to it",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="the file to write to",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="the content to be written",
            ),
        },
        required=["file_path", "content"],
    ),
)
