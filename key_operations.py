# key handler
import os
import shutil

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

application_folder = Path(__file__).resolve().parent
keys_folder_path = application_folder / "keys"
pub_key_path = application_folder / "keys/pub_key.pem"
priv_key_path = application_folder / "keys/priv_key.pem"

def generate_keys_folder():
    if keys_folder_path.exists():
         shutil.rmtree(keys_folder_path)
         print("deleting existing keys folder")
    else:
        print(f"keys folder : [not found]\n\t- creating keys folder @ {keys_folder_path}")
        print(f"\t- creating private key file @ {priv_key_path}")
        print(f"\t- creating public key file @ {pub_key_path}")

    keys_folder_path.mkdir(exist_ok=True)
    priv_key_path.touch()
    pub_key_path.touch()

    if pub_key_path.exists() and priv_key_path.exists():
        print("key files : [creation success]")
    else:
        print(f"error: delete {keys_folder_path} and try again.")
    generate_keys()


def corruption_message():
    print("found key pair corruption :")
    print("\t- deleting old keys & generating new ones")


def keypair_corruption(): # key pair corruption ?
    if keys_folder_exists():
        if pub_key_path.exists() and priv_key_path.exists():
            print("public key : [ok] / private key : [ok]")
            return False
        elif not pub_key_path.exists():
            print("public key : [bad] / private key : [ok]")
            corruption_message()
            return True
        else:
            print("public key : [ok] / private key : [bad]")
            corruption_message()
            return True
    else: 
        print("key folder not found")
        return True


def keys_folder_exists():
    #is it efficient to create a variable in memory for this? if statement?
    if keys_folder_path.exists():
        print("keys folder : [ok]")
        return True
    else:    
        print("keys folder : [not found]")
        return False

# hybrid encryption
# RSA key generation (asymmetric encryption (handshake))
def generate_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537, # default value
        key_size=4096 # make key size variable to user choice?
    )
    pem_private = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption(os.getenv("KEY_FILE_PASSWORD").encode())
    )

    public_key = private_key.public_key()
    pem_public = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # what happens if commented out?
    pem_private.splitlines()[0] # keep eye on
    pem_public.splitlines()[0] # keep eye on
    return pem_private, pem_public


def load_keys(pem_private, pem_public): # params are bytes from generate_keys
    priv_key_size = os.path.getsize(priv_key_path)
    pub_key_size = os.path.getsize(pub_key_path)

    if priv_key_size > 0 and pub_key_size > 0:
        print("keys already in file")
    elif priv_key_size == 0 and pub_key_size == 0:
        try:
            with open(priv_key_path, 'wb') as file:
                file.write(pem_private)
            with open(pub_key_path, 'wb') as file:
                file.write(pem_public)
            print("keys loaded into file : [success]")
            return True
        except IOError:
            print(f"error please delete {keys_folder_path} and try again")
            return False
    else:
        print("file loading error in key_operations.load_keys() | loading new keys")
        return False
    

def get_keys():
    try:
        with open(priv_key_path, "rb") as key_file:
            private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=os.getenv("KEY_FILE_PASSWORD").encode(),
            )
        print("private key loading: [success]")

        with open(pub_key_path, "rb") as key_file:
            public_key = serialization.load_pem_public_key(
                key_file.read()
            )
        print("public key loading : [success]")

        return private_key, public_key
    
    except IOError:
        print("file loading error in key_operations.load_keys() | loading existing keys")
        return 