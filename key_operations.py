# key handler
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from pathlib import Path
import shutil
import os
from dotenv import load_dotenv

load_dotenv()

class keys:
    def generate_keys():
        private_key = rsa.generate_private_key(
        public_exponent=65537, #default value
        key_size=4096
        )
        pem_private = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format = serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.BestAvailableEncryption(os.getenv("KEY_FILE_PASSWORD").encode())
        )
        public_key = private_key.public_key()
        pem_public = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        pem_private.splitlines()[0]
        pem_public.splitlines()[0]
        return pem_private , pem_public

class key_file_handler:
    pub_key_path = application_folder/"keys/pub_key.pem"
    priv_key_path = application_folder/"keys/priv_key.pem"
    def load_keys(private_key, public_key): #params are bytes
        with open (priv_key_path, 'w') as file:
            file.write(private_key)
        with open (pub_key_path, 'w') as file:
            file.write(public_key)
        
        if os.path.getsize(priv_key_path) > 0:
            print("private key loading: [success]")
        elif os.path.getsize(pub_key_path) > 0:
            print("public key loading : [success]")
        else: 
            print("key loading : [error]")

    def check_keypair_corruption():
        if pub_key_path.exists() and priv_key_path.exists():
            print("public key : [ok] / private key : [ok]")
        elif not pub_key_path.exists():
            print("public key : [bad] / private key : [ok]")
            self.corruption_message()
            self.generate_keys_folder()
        else:
            print("public key : [ok] / private key : [bad]")
            corruption_message()
            generate_keys_folder()

    def corruption_message():
            print("found key pair corruption :")
            print("\t- deleting old keys & generating new ones")

    print(f"\t- creating private key file @ {priv_key_path}")
    print(f"\t- creating public key file @ {pub_key_path}")


class key_folder_handler:
    application_folder = Path(__file__).resolve().parent
    folder_path = application_folder/"keys"

    def generate_folder():
        if folder_path.exists():
            shutil.rmtree(folder_path)

        print(f"keys folder : [not found]\n\t- creating keys folder @ {folder_path}")

        folder_path.mkdir(exist_ok=True)
        priv_key_path.touch()
        pub_key_path.touch()

        if pub_key_path.exists() and priv_key_path.exists():
            print("key files : [creation success]")
        else:
            print(f"error: delete {folder_path} and try again.")
        generate_keys()

    def keys_state_check():
        if folder_path.exists():
            print("keys folder : [ok]")
            keys.check_keypair_corruption()
        else:
            key_folder_handler.generate_folder()

#hybrid encryption
#RSA key generation (asymmetric encryption (handshake))

# if keys in key files, load keys in files as keys?
#def get_keys():
# else: generate keys and load into files

"""
this is for loading already generated keys as private key
with open(priv_key_file, "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
    )
"""


