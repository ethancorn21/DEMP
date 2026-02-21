# state check
# see if there are known keys or not
# if not, generate keys and create new .pem file in /keys
from pathlib import Path
import shutil

application_folder = Path(__file__).resolve().parent
keys_folder_path = application_folder/"keys"
pub_key_file = application_folder/"keys/pub_key.pem"
priv_key_file = application_folder/"keys/priv_key.pem"

def generate_keys_folder():
    print(f"no key folder found : \n\t- creating keys folder @ {keys_folder_path}")
    print(f"\t- creating private key file @ {priv_key_file}")
    print(f"\t- creating public key file @ {pub_key_file}")
    keys_folder_path.mkdir(exist_ok=True)
    priv_key_file.touch()
    pub_key_file.touch()
    if pub_key_file.exists() and priv_key_file.exists():
        print("fresh key files successfully created")
    else:
        print(f"Please delete {keys_folder_path} and try again.")
def check_keypair_corruption():
    if pub_key_file.exists() and priv_key_file.exists():
        print("public key : [ok] / private key : [ok]")
    if not pub_key_file.exists():
        print("public key : [bad] / private key : [ok]")
        generate_keys_folder()
    else:
        print("public key : [ok] / private key : [bad]")
    print("found key pair corruption :")
    print("\t- deleting old keys & generating new ones")
    shutil.rmtree(keys_folder_path)
    generate_keys_folder()

if keys_folder_path.exists():
    print("keys folder : [ok]")
    check_keypair_corruption()
else:
    generate_keys_folder()
