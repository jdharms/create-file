import os

env_keys = list(dict(os.environ).keys())
env_key = "INPUT_FILE_CONTENTS"

out_file = ""

for key in env_keys:
    if key == env_key:
        out_file += os.environ.get(key) + "\n"

with open("/github/workspace/" + str(os.environ.get("INPUT_FILE_NAME")), "w") as text_file:
    text_file.write(out_file)
