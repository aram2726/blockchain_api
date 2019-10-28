import os
import hashlib

BLOCKCHAIN_DIR = os.path.join(os.path.dirname(__file__), "blockchain/")


def get_blockchain_files():
    files = os.listdir(BLOCKCHAIN_DIR)
    return sorted([int(i) for i in files])


def get_blockchain_file(name):
    return os.path.join(BLOCKCHAIN_DIR, str(name)) or None


def get_hash(file_name):
    file = open(os.path.join(BLOCKCHAIN_DIR, file_name), "rb").read()
    return str(hashlib.sha1(file).hexdigest())
