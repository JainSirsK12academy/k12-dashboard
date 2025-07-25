# generate_labels_json.py
import os
import json

labels = []

for folder in os.listdir():
    if os.path.isdir(folder):
        labels.append(folder)

with open("labels.json", "w") as f:
    json.dump(labels, f)

print(f"✅ labels.json created with {len(labels)} labels.")
