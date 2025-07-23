import argparse
import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

from functions.call_func import available_functions, call_function

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key) 
system_prompt = """
When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

def main():

    parser = argparse.ArgumentParser(
        description="Interacte with GenAI via CLI!!",
        usage="python main.py <prompt> [ -verbose | -v ]"
    )

    parser.add_argument("prompt", type=str, nargs="+", help="Prompt to send to GenAI")
    parser.add_argument('--verbose', '-v', action='store_true', help="Print verbose output")


    args = parser.parse_args()
    user_prompt = " ".join(args.prompt)

    messages = [
        types.Content(role='user', parts=[types.Part(text=user_prompt)])
    ]

    config = types.GenerateContentConfig(
        tools=[available_functions],
        system_instruction=system_prompt,
    )

    max_turns = 20
    turn_count = 0

    if args.verbose:
        print(f"Initial User Prompt: {user_prompt}\n")

    while turn_count < max_turns:
        try:
            print(f"--- Calling GenAI (Turn {turn_count + 1}) ---")
            response = client.models.generate_content(
                model='gemini-2.0-flash-001',
                contents=messages,
                config=config,
            )

            if args.verbose:
                print("\n")
                print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
                print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
                if response.candidates:
                    print("  Model's raw candidate content:")
                    for i, candidate in enumerate(response.candidates):
                        print(f"    Candidate {i} (Role: {candidate.content.role}):")
                        for part in candidate.content.parts:
                            if part.text:
                                print(f"      Text: {part.text[:200]}...") # Print first 200 chars
                            if part.function_call:
                                print(f"      Function Call: {part.function_call.name}({part.function_call.args})")
                else:
                    print("  No candidates in response.")
                    # If no candidates, it might be a blocked response. Print an error and break.
                    print("Error: GenAI returned no candidates. Check safety settings or prompt.")
                    break # Exit loop on no candidates

            if response.candidates:
                messages.append(response.candidates[0].content)
            else:
                break

            if not response.function_calls:
                print("\n--- Final Model Text Response ---")
                print(response.text)
                break # Exit the while loop

            print("\n--- Executing Function Calls ---")

            for func in response.function_calls:
                func_result = call_function(func, args.verbose)
                if (
                    not func_result.parts
                    or not func_result.parts[0].function_response
                ):
                    raise Exception("empty function call result")

                messages.append(func_result)

                if args.verbose:
                    tool_response_data = func_result.parts[0].function_response.response
                    print(f"-> Tool response sent to model for {func.name}: {tool_response_data}")

            turn_count += 1
        except Exception as e:
            print(f"an Error occured: {e}")
            sys.exit(1)

        if turn_count == max_turns:
            print(f"\nMax turns ({max_turns}) reached. Conversation may not be complete.")
            # If the last response had text, print it
            if response and response.text:
                 print(f"Last model text response:\n{response.text}")


if __name__ == "__main__":
    main()
