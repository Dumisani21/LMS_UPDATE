import os
import subprocess


def check_version() -> str:
    command = "wtc-lms --version"
    output = subprocess.check_output(command, shell=True, text=True)
    return output

def is_int(value) -> bool:
    try:
        int(value)
        return True
    except ValueError:
        return False

def update_lms(path_location="Downloads/") -> bool:
    user = os.getlogin()
    path_exists = os.path.exists(os.path.join("/home",user,path_location))
    path = os.path.join("/home",user,path_location)
    downloaded_file = os.path.exists(f"{path}wtc-lms")
    installed_file = os.path.exists(os.path.join("/usr","bin","wtc-lms"))
    if downloaded_file and installed_file:
        check_current_lms = subprocess.check_output("wtc-lms --version", shell=True, text=True)
        check_downloaded_lms = subprocess.check_output(f"source {path}wtc-lms --version")
    else:
        if not downloaded_file:
            print("it seems like you don't have wtc-lms downloaded yet!")
        if not installed_file:
            print("it seems like you don't have wtc-lms installed yet!")
        return
    
    if check_current_lms == check_downloaded_lms:
        print("lms is already up to date!")
        return
    else:
        if path_exists:
            command = "whereis wtc-lms"
            output = subprocess.check_output(command, shell=True, text=True).strip().split(" ")
            output.pop(0)
            if len(output) > 1:
                for i in range(len(output)):
                    print(f"[{i+1}]: {output}")
                selection = input(f"Enter selection: ")
                while not is_int(selection):
                    print("Please enter numbers only")
                    if is_int(selection):
                        if int(selection) > output:
                            print("Please enter the numbers that appear only!")
                            continue
                    selection = input("Enter selection: ")
                output = output[selection]
            else:
                output = output[0]
            print(f"is this your primary location: {output} (y)es/(n)o?")
            response = ""
            while response == "":
                response = input("> ").strip().lower()
                if response == "y":
                    copy = output.split("/")
                    copy.pop(-1)
                    copy = "/".join(copy)
                    if os.path.exists(f"{path}wtc-lms"):
                        os.system(f"cp {path}wtc-lms {copy}")
                        check_version = subprocess.check_output("wtc-lms --version",shell=True, text=True)
                        check_current = subprocess.check_output(f"{path}wtc-lms --version")
                        if check_version == check_current:
                            print("lms updated :\)")
                    else:
                        print("Please download wtc-lms first then run this script again")
                        return
                elif response == "n":
                    print("lms not updated")
                    return

        else:
            print("Path does not exist!")
    return True


update_lms()

