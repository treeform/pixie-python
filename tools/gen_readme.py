import os

def cut_between(s, a, b):
    ai = s.find(a)
    bi = s.find(b)
    return s[(ai + len(a)):bi]

exampleFiles = [
    "examples/text.py",
    "examples/text_spans.py",
    "examples/square.py",
    "examples/line.py",
    "examples/rounded_rectangle.py",
    "examples/heart.py",
    "examples/masking.py",
    "examples/gradient.py",
    "examples/image_tiled.py",
    "examples/shadow.py",
    "examples/blur.py",
    "examples/tiger.py"
]

md = []

for path in exampleFiles:
    os.system("python " + path)
    name = os.path.splitext(os.path.basename(path))[0]
    name = name.replace("_", " ").capitalize()
    md.append("### " + name)
    md.append("python [" + path + "](" + path + ")")
    code = open(path, "r").read()
    code = cut_between(code, "image.fill(pixie.Color(1, 1, 1, 1))", "image.write_file").strip()
    code = "```py\n" + code + "\n```"
    md.append(code)
    md.append("![example output](" + path.replace(".py", ".png") + ")")
    md.append("")

readme = open("README.md", "r").read()

at = readme.find("## Examples")

readme = readme[0:at]
readme = readme + "## Examples\n\n"
readme = readme + "`git clone https://github.com/treeform/pixie-python` to run examples.\n\n"
readme = readme + "\n".join(md)

open("README.md", "w", newline="\n").write(readme)
