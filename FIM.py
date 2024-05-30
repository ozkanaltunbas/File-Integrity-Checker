import hashlib 
import time 
import os 


print("""
********************************************************************************
*######## #### ##       ########   ######  ##     ## ########  ######  ##    ##*
*##        ##  ##       ##        ##    ## ##     ## ##       ##    ## ##   ## *
*##        ##  ##       ##        ##       ##     ## ##       ##       ##  ##  *
*######    ##  ##       ######    ##       ######### ######   ##       #####   *
*##        ##  ##       ##        ##       ##     ## ##       ##       ##  ##  *
*##        ##  ##       ##        ##    ## ##     ## ##       ##    ## ##   ## *
*##       #### ######## ########   ######  ##     ## ########  ######  ##    ##*
********************************************************************************
""")

hash_dict = {} 

def get_file_hash(file_path): 
    try:
        with open(file_path, 'rb') as file_hash: 
            return hashlib.sha256(file_hash.read()).hexdigest() 
    except FileNotFoundError:
        print(f"{file_path} not found!")
        return None
    except PermissionError:
        print(f"Permission denied: {file_path}")
        return None

def initialize_hashes(file_path): 
    if file_path not in hash_dict:
        file_hash = get_file_hash(file_path)
        if file_hash is not None:
            hash_dict[file_path] = file_hash

def check_integrity(): 
    for file_path, initial_hash in hash_dict.items(): 
        current_hash = get_file_hash(file_path) 
        if current_hash is None:
            continue
        if current_hash != initial_hash: 
            print(f"A change has been detected in {file_path}!")
            print("Initial Hash:", initial_hash)
            print("Current Hash:", current_hash)
            hash_dict[file_path] = initial_hash


def get_file_path_from_user():
    while True:
        file_path = input("Please enter the file path to monitor: ")
        if os.path.exists(file_path):
            return file_path
        else:
            print("File not found. Please enter a valid file path.")


file_path = get_file_path_from_user()
initialize_hashes(file_path)

while True:
    check_integrity() 
    time.sleep(1800)
