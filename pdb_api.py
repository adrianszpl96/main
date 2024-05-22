import requests
def Download(pdb):
    url = f"https://files.rcsb.org/download/{pdb}.pdb"
    response = requests.get(url)
    if response.status_code == 200:
        with open(f"{pdb}.pdb", "wb") as file:
            file.write(response.content)
            print("File downloaded succesfully!")
    else:
        print("Failed to download the file.")
Download("4gd2")


