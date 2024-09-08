import os
import pathlib
import re
import time
from pathlib import Path
from typing import Optional

BAT_FILE_PATH = Path("./git_push.bat")

if __name__ == '__main__':
    with open(BAT_FILE_PATH, "r", encoding="utf-8") as file:
        content = file.read()

    today = time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime())
    content = re.compile(r"(git commit -m )(.+)").sub(lambda m: f"{m.group(1)}\"{today}\"", content)

    with open(BAT_FILE_PATH, "w", encoding="utf-8") as file:
        file.write(content)

    os.system(str(BAT_FILE_PATH))
