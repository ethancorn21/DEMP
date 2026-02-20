# state check
# see if there are known keys or not
# if not, generate keys and create new .pem file in /keys
from pathlib import Path

keys_path = "DEMP/keys"
pub_key_file = "DEMP/keys/pub_key.pem"
priv_key_file = "DEMP/keys/priv_key.pem"
if keys_path.exists():
    print("keys found...")
else:
    open(keys_path, "x") as file:
    open(keys_path, "x") as file: