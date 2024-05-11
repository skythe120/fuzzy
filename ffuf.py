import subprocess

def run_words(url):
    # Define the FUFF command
    ffuf_command = [
        "ffuf",
        "-w", "small.txt",  # Replace this with the path to your wordlist
        "-u", f"{url}/FUZZ",             # FUZZ will be replaced with each directory in the wordlist
        "-fc", "404"                     # Filter out 404 responses
    ]

    # Run FfUF command
    try:
        subprocess.run(ffuf_command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return

def run_dir(url):
    # Define the FUFF command
    ffuf_command = [
        "ffuf",
        "-w", "find-dir.txt",  # Replace this with the path to your wordlist
        "-u", f"{url}/FUZZ",             # FUZZ will be replaced with each directory in the wordlist
        "-fc", "404"                     # Filter out 404 responses
    ]

    # Run FfUF command
    try:
        subprocess.run(ffuf_command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return

def run_recursive(url):
    # Define the FUFF command
    ffuf_command = [
        "ffuf",
        "-w", "small.txt",  # Replace this with the path to your wordlist
        "-u", f"{url}/FUZZ",             # FUZZ will be replaced
        "-recursion",
        "-recursion-depth", "1",
        "-e", ".php",
        "-v",
        "-fc", "404"                     # Filter out 404 responses
    ]

    # Run FfUF command
    try:
        subprocess.run(ffuf_command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return
        
def run_subdom(url):
    # Define the FUFF command
    ffuf_command = [
        "ffuf",
        "-w", "subdom.txt",  # Replace this with the path to your wordlist
        "-u", f"http://FUZZ.{url}",             # FUZZ will be replaced
        "-fc", "404"                     # Filter out 404 responses
    ]

    # Run FfUF command
    try:
        subprocess.run(ffuf_command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return


while True:
	target_url = input("Enter the target URL: ")
	print("Options \n")
	print("1. Basic ffuf \n")
	print("2. Directory search \n")
	print("3. Recusion 1 level \n")
	print("4. Sub Domain \n")
	opt = input("Please choose: ")
	try:
		opt = int(opt)
	except:
		print("invalid")
	if(opt == 1):
		run_words(target_url)
	elif(opt == 2):
		run_dir(target_url)
	elif(opt == 3):
		run_recursive(target_url)
	elif(opt == 4):
		run_subdom(target_url)
	else:
		break
	

