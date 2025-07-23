# from get_files_info import get_files_info
#
# inputs = [
#     ('calculator', '.','Result for current directory:\n- main.py: file_size=576 bytes, is_dir=False\n- tests.py: file_size=1343 bytes, is_dir=False\n- pkg: file_size=92 bytes, is_dir=True'),
#     ('calculator', 'pkg',"Result for 'pkg' directory:\n- calculator.py: file_size=1739 bytes, is_dir=False\n- render.py: file_size=768 bytes, is_dir=False\n- __pycache__: file_size=96 bytes, is_dir=True"),
#     ('calculator', '/bin',"Result for '/bin' directory:\nError: Cannot list \"/bin\" as it is outside the permitted working directory"),
#     ('calculator', '../', "Result for '../' directory:\nError: Cannot list \"../\" as it is outside the permitted working directory"),
# ]
#
# def test(input1, input2, expected_output):
#     print('-----------------------')
#     print('Input:')
#     print(f'{input1} \n')
#     print(f'Expected: \n{expected_output} \n')
#     result = get_files_info(input1, input2)
#     print(f'Actual: \n{result}\n')
#     if result == expected_output:
#         print("Pass")
#         return True
#     else:
#         print("Fail")
#         return False
#
# def main():
#     passed = 0
#     failed = 0
#     for input in inputs:
#         correct = test(*input)
#         if correct:
#             passed += 1
#         else:
#             failed += 1
#     if failed == 0:
#         print("============= PASS ==============")
#     else:
#         print("============= FAIL ==============")
#     print(f"{passed} passed, {failed} failed")
#
# main()
from functions.get_files_content import get_file_content


def test():
    print(get_file_content('pkg', 'morelorem.txt'))
    

if __name__ == "__main__":
    test()
