import os
import time
import urllib.request
import subprocess

def setconsoletitle(title):
    if os.name == 'nt':
        os.system(f"title {title}")

art1 = """









                  .__               __           
                  |  |__  _____   _/  |_   ____  
                  |  |  \ \__  \  \   __\_/ __ \ 
                  |   Y  \ / __ \_ |  |  \  ___/ 
                  |___|  /(____  / |__|   \___  >
                       \/      \/             \/ 

                  > welcome to hate | open sourced @github.com/remediated 
"""

art2 = """







 
                  .__               __           
                  |  |__  _____   _/  |_   ____  
                  |  |  \ \__  \  \   __\_/ __ \ 
                  |   Y  \ / __ \_ |  |  \  ___/ 
                  |___|  /(____  / |__|   \___  >
                       \/      \/             \/ 

                       
"""

def check7zipinstalled():
    return os.path.exists("C:\\Program Files\\7-Zip\\7z.exe")

def install7zip():
    url = "https://www.7-zip.org/a/7z2407-x64.exe"
    installer_path = os.path.join(os.getcwd(), "7z_installer.exe")
    urllib.request.urlretrieve(url, installer_path)
    command = [installer_path, "/S"]
    subprocess.run(command, check=True)
    os.remove(installer_path)

def attemptextract(archive, password):
    output_dir = "./cracked"
    command = ["C:\\Program Files\\7-Zip\\7z.exe", "x", f"-p{password}", archive, f"-o{output_dir}", "-y"]
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return result.returncode == 0
    except subprocess.CalledProcessError:
        return False

def readpasswordsfromfile(wordlist):
    with open(wordlist, 'r') as f:
        passwords = [line.strip() for line in f.readlines() if line.strip()]
    return passwords

def main():
    setconsoletitle("hate")
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        print(art1)

        if not check7zipinstalled():
            print("                  7zip isn't installed, installing")
            install7zip()
            if not check7zipinstalled():
                print("                  installation failed, exiting")
                break
            else:
                print("                  7zip installed")

        archive = input("                  archive : ").strip()
        if not os.path.exists(archive):
            print("                  archive not found")
            time.sleep(2)
            continue

        while True:
            wordlist = input("                  wordlist : ").strip()
            if not os.path.exists(wordlist):
                print("                  wordlist not found")
                time.sleep(2)
                continue
            elif not wordlist.endswith('.txt'):
                print("                  .txt wordlist")
                time.sleep(2)
                continue
            else:
                break

        passwords = readpasswordsfromfile(wordlist)
        if not passwords:
            print("                  wordlist empty")
            time.sleep(2)
            continue

        os.system('cls' if os.name == 'nt' else 'clear')

        print(art2)

        total_passwords = len(passwords)
        password_found = False

        for index, password in enumerate(passwords, start=1):
            print(f"                  attempting password {index} of {total_passwords}", end='\r')
            if attemptextract(archive, password):
                print(f"\n                  password found : {password}")
                password_found = True
                time.sleep(4)
                break

        if not password_found:
            print("\n                  password not found")
            time.sleep(4)

        os.system('cls' if os.name == 'nt' else 'clear')

        print(art2)

        choice = input("                  restart : ").strip().lower()
        if choice != 'y' and choice != 'yes':
            break

if __name__ == "__main__":
    main()