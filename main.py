import os
import sys

TEXT = "Nothing here is waiting on you. The cursor has stopped blinking so hard. Somewhere a fan hums on, steady as breathing, and the next task will still be there tomorrow, patient as weather. You have read enough. The screen dims toward its edges. It is allowed to rest."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)

output_path = os.path.join(output_dir, "entry.txt")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(TEXT)

char_count = len(TEXT)
print(f"Wrote {char_count} characters to {output_path}")
print(open(output_path, encoding="utf-8").read())
