import os

from google.genai import types


def get_files_info(working_directory, dir='.'):
    try:
        path = os.path.join(working_directory, dir)

        # Check for path traversal attempts and non-directory inputs
        abs_working_dir = os.path.abspath(working_directory)
        abs_path = os.path.abspath(path)

        if not abs_path.startswith(abs_working_dir):
            return f'Result for \'{dir}\' directory:\nError: Cannot list "{dir}" as it is outside the permitted working directory'
        elif not os.path.isdir(path):
            return f'Result for \'{dir}\' directory:\nError: "{dir}" is not a directory'

        files = []
        for file in os.listdir(path):
            file_path = os.path.join(path, file)
            files.append(f"- {file}: file_size={os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}")

        # Add the "Result for X directory:" prefix here for successful cases
        return f"Result for '{dir}' directory:\n" + "\n".join(files)

    except Exception as e:
        # Keep this for unexpected errors, though the checks above cover most
        return f"Result for '{dir}' directory:\nError: {e}"

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "dir": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
