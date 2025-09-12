import os
import subprocess

with open("list.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

table_lines = []
for line in lines:
    if line.strip().startswith("|"):
        table_lines.append(line.strip())

table_data = table_lines[2:]

target_dir = "/proj/inf-scaling/csl/BiTCAM/BiTCAM"
os.chdir(target_dir)

video_root = "/proj/inf-scaling/csl/BiTCAM/datasets/VGGSound/video"

for row in table_data:
    parts = [col.strip() for col in row.split("|")[1:-1]]
    dataset, prompt, file_name, duration = parts

    video_path = os.path.join(video_root, file_name)

    cmd = [
        "python", "demo.py",
        "--video", video_path,
        "--prompt", prompt,
        "--no-download",
        "--num-steps", "4",
        "--variant", "large_16k_v2"
    ]

    print("Running:", " ".join(cmd))
    subprocess.run(cmd)
