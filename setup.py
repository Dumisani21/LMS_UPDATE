# import os, subprocess

# def check_path(path: str) -> tuple:
#     path = os.path.join("/home", os.getlogin(), path)
#     x = os.path.exists(path)
#     return x, path

# def make_repo(path: str) -> bool:
#     os.mkdir(path)
#     return True

# def check_shell() -> str:
#     shell = os.environ["SHELL"]
#     return shell


# def setup_shell(shell: str, path: str) -> bool:
#     if shell == "usr/bin/zsh":
#         os.system(f"echo 'alias update_lms=\"python3 {path}update_wtc-lms.py\"' >> ~/.zshrc")
#         return True
#     elif shell == "usr/bin/bash":
#         os.system(f"echo 'alias update_lms=\"python3 {path}update_wtc-lms.py\"' >> ~/.bashrc")
#         return True
#     else:
#         print("Please setup the alias yourself!")
#         return False


# if __name__ == "__main__":
#     state, path = check_path(".lms_update/")
#     if not state:
#         make_repo(path)
#     else:
#         # move the update_wtc-lms.py file to the path
#         os.system(f"mv update_wtc-lms.py {path}")
#         # setup config in the shell I am using
#         shell = check_shell()
#         status_shell_setup = setup_shell(shell, path)
#         # print success message
#         if status_shell_setup:
#             print("Setup complete! Please restart your shell to use the alias!")
#         else:
#             print("Setup complete! Please add the following line to your shell config file:")
#             print("alias update_lms=\"python3 {path}update_wtc-lms.py\\")
