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
    path = os.path.join("/home", user, path_location)
    downloaded_file = os.path.exists(os.path.join(path, "wtc-lms"))
    installed_file = os.path.exists(os.path.join("/usr/bin", "wtc-lms"))

    if not downloaded_file:
        print("It seems like you don't have wtc-lms downloaded yet!")
        print("Please download wtc-lms first and put it in the downloads folder, then run this script again")
        return False

    check_current_lms = check_version().strip()
    os.system(f"chmod +x {path}wtc-lms")
    check_downloaded_lms = subprocess.check_output(f"{path}wtc-lms --version", shell=True, text=True).strip()

    if check_current_lms == check_downloaded_lms:
        print("lms is already up to date!")
        return True
    else:
        path_exists = os.path.exists(path)
        if path_exists:
            command = "whereis wtc-lms"
            output = subprocess.check_output(command, shell=True, text=True).strip().split(" ")
            output.pop(0)
            if len(output) > 1:
                for i in range(len(output)):
                    print(f"[{i+1}]: {output[i]}")
                selection = input("Enter selection: ")
                while not is_int(selection):
                    print("Please enter numbers only")
                    if is_int(selection):
                        if int(selection) > len(output):
                            print("Please enter the numbers that appear only!")
                            continue
                    selection = input("Enter selection: ")
                output = output[int(selection) - 1]
            elif len(output) == 0:
                # this means that the file is not in the /usr/bin/ folder
                # so we will just provide the path to the file
                output = "/usr/bin/"
            else:
                output = output[0]
            print(f"Is this your primary location: {output} (y)es/(n)o?")
            response = ""
            while response == "":
                response = input("> ").strip().lower()
                if response == "y":
                    copy = output.split("/")
                    copy.pop(-1)
                    copy = "/".join(copy)
                    if os.path.exists(f"{path}wtc-lms"):
                        os.system(f"cp {path}wtc-lms {copy}")
                        current_version = check_version().strip()
                        check_current = subprocess.check_output("wtc-lms --version", shell=True, text=True).strip()
            
                        if current_version == check_current:
                            print("lms updated :)")
                            print(f"Version: {current_version}")
                            return True
                        else:
                            print("Failed to update lms!")
                            return False
                    else:
                        print("Please download wtc-lms first, then run this script again")
                        return False
                elif response == "n":
                    print("lms not updated")
                    return False
        else:
            print("Path does not exist!")
            return False


update_lms()

