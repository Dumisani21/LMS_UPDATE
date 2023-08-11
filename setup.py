import os, getpass

def check_path(path: str) -> tuple:
    path = os.path.join("/home", getpass.getuser(), path)
    x = os.path.exists(path)
    return x, path

def make_repo(path: str) -> bool:
    os.mkdir(path)
    return True

def check_shell() -> str:
    shell = os.environ["SHELL"]
    return shell


def setup_shell(shell: str, path: str) -> bool:
    shell_config = os.path.expanduser("~/.zshrc") if shell == "/usr/bin/zsh" else os.path.expanduser("~/.bashrc")
    alias_command = f"alias update_lms=\"python3 {path}update_wtc-lms.py\""

    try:
        with open(shell_config, "a") as file:
            file.write(f"\n{alias_command}\n")
        return True
    except Exception as e:
        print(f"An error occurred while setting up the alias: {str(e)}")
        return False

if __name__ == "__main__":
    state, path = check_path(".lms_update/")
    if not state:
        make_repo(path)
    else:
        # move the update_wtc-lms.py file to the path
        os.system(f"cp update_wtc-lms.py {path}")
        # setup config in the shell I am using
        shell = check_shell()
        print(shell)
        status_shell_setup = setup_shell(shell, path)
        # # print success message
        if status_shell_setup:
            print("Setup complete! Please restart your shell to use the alias!")
            print("To update lms, type update_lms in your shell")
        else:
            print("Setup complete! Please add the following line to your shell config file:")
            print("alias update_lms=\"python3 {path}update_wtc-lms.py\\")
            print("and restart your shell to use the alias!")
            print("\nTo update lms, type update_lms in your shell")
