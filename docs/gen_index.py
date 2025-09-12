#!/usr/bin/env python3
"""
从 list.md 读取表格，生成每行对应的 <tbody> 片段。
视频顺序：gt, BiTCAM_L_16k, BiTCAM_S_16k, MMAudio_L_44k
"""

import re
import html
from pathlib import Path

# 配置区：按你指定的顺序（注意这里直接包含 gt）
model_dirs = ["gt", "BiTCAM_L_16k", "BiTCAM_S_16k", "MMAudio_L_44k"]
video_root = "video"  # 生成 src="{video_root}/{model}/{file}"

# 输入 / 输出
md_path = Path("list.md")
out_path = Path("videos_snippets.html")

if not md_path.exists():
    raise SystemExit(f"找不到 {md_path.resolve()}，请把脚本放在 list.md 同目录或修改 md_path。")

lines = md_path.read_text(encoding="utf-8").splitlines()

# 收集所有以 '|' 开头的表格行（保留 header）
table_lines = [ln for ln in lines if ln.strip().startswith("|")]

# 跳过 header（通常 header + 分隔 行），表格数据从第三行开始
if len(table_lines) < 3:
    raise SystemExit("检测到的表格行太少，无法解析。请确认 list.md 中包含 Markdown 表格。")

data_lines = table_lines[2:]  # 从第三行开始是数据行

def parse_row(row_line: str):
    """把一行 | a | b | c | d | 解析成四元组（strip 后）"""
    parts = [p.strip() for p in row_line.split("|")[1:-1]]  # 去掉首尾空段
    if len(parts) < 4:
        parts += [""] * (4 - len(parts))
    return parts[0], parts[1], parts[2], parts[3]

snippets = []
for row in data_lines:
    dataset, prompt, file_name, duration = parse_row(row)
    esc_prompt = html.escape(prompt)
    esc_file = html.escape(file_name)
    # 生成 video 元素，顺序使用 model_dirs
    video_tags = []
    for m in model_dirs:
        src = f"{video_root}/{m}/{esc_file}"
        tag = f'<video controls>\n<source src="{src}" type="video/mp4">\n</video>'
        video_tags.append(tag)

    videos_html = "\n".join(video_tags)
    tbody = (
        "<tbody><tr><td colspan=\"4\">\n"
        f'<span style="display:block; text-align:left;"><b>Prompt:</b> {esc_prompt}</span>\n'
        '<div class="video-row">\n'
        f"{videos_html}\n"
        "</div>\n"
        "</td></tr></tbody>\n"
    )
    snippets.append(tbody)

out_path.write_text("".join(snippets), encoding="utf-8")
print(f"已生成 {out_path.resolve()}，共 {len(snippets)} 个 <tbody> 片段。")
