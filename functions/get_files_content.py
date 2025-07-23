import os

from google.genai import types

from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    path = os.path.join(working_directory, file_path)
    abs_working_dir = os.path.abspath(working_directory)
    abs_path = os.path.abspath(path)

    if not abs_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    elif not os.path.isfile(path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(abs_path, 'r') as f:
            file_content_string = f.read(MAX_CHARS)
            if os.path.getsize(abs_path) > MAX_CHARS:
                file_content_string += f"[...File \"{file_path}\" truncated at 10000 characters]"
        return file_content_string
    except Exception as e:
        return f'Error reading file "{file_path}": {e}'

schema_get_files_content = types.FunctionDeclaration(
    name="get_file_content",
    description="gets the content of the file, and truncates it if the file size surpasses 10k words",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="the file to get the content of",
            ),
        },
        required=['file_path'],
    ),
)
