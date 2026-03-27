import json
import os

LEDGER_FILE = "ledger.json"

if os.path.exists(LEDGER_FILE):
    with open(LEDGER_FILE, "r") as f:
        ledger = json.load(f)
else:
    ledger = {}

def save_ledger():
    with open(LEDGER_FILE, "w") as f:
        json.dump(ledger, f, indent=4)

def store_image(image_id, image_hash, filename):
    ledger[image_id] = {
        "hash": image_hash,
        "filename": filename
    }
    save_ledger()

def get_image(image_id):
    return ledger.get(image_id)
