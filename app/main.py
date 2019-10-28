import os
import json

from .utils import (
    BLOCKCHAIN_DIR, get_blockchain_files, get_blockchain_file, get_hash
)


def write_block(name, amount, to_whom):
    last_file = get_blockchain_files()[-1]
    file_name = str(last_file + 1)
    prev_hash = get_hash(str(last_file))

    data = {
        "id": file_name,
        "name": name,
        "amount": amount,
        "to_whome": to_whom,
        "hash": prev_hash
    }

    with open(BLOCKCHAIN_DIR + file_name, "w") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def check_compatibility():
    results = []

    for file in get_blockchain_files()[1:]:
        _hash = json.load(open(BLOCKCHAIN_DIR + str(file)))['hash']

        prev_file = str(file - 1)
        actual_hash = get_hash(prev_file)

        if _hash == actual_hash:
            res = "OK"
        else:
            res = "Corrupted"

        results.append({
            "block": prev_file,
            "result": res
        })
    return results


def get_block(name):
    return json.loads(open(get_blockchain_file(name), "rb").read())


def remove_block(name):
    try:
        os.remove(get_blockchain_file(name))
    except FileExistsError:
        raise ValueError(f"Invalid value {name}")


def edit_block(pk, name, amount, to_whom, _hash):

    data = {
        "id": pk,
        "name": name,
        "amount": amount,
        "to_whom": to_whom,
        "hash": _hash
    }

    with open(BLOCKCHAIN_DIR + str(pk), "w") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
