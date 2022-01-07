#!/usr/bin/env python

import sys
import argparse
import datetime
import os
import yaml
import subprocess

HUGO_ROOT = os.getenv("HUGO_ROOT", default="")

TODAY = datetime.date.today().strftime("%Y-%m-%d")

DEFAULT_IMG_PATH = "static/img/jots"
DEFAULT_IMG_NAME = f"{TODAY}.svg"

def parse_args(cli=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", help=f"New file (default to {TODAY}.md)", default=None)
    parser.add_argument("--img", help="Image file to be moved", default=None)
    parser.add_argument("-t", "--title", help="Title of the post")
    parser.add_argument("--tags", help="Tags to be put in the post metadata", default=None)
    parser.add_argument("-c", "--categories", nargs='+', help="Categories to be put in the post metadata", default=["jots"])
    args = parser.parse_args(cli)
    return args


def create_post(filename):
    post_name = os.path.join("post", filename)
    subprocess.run(f"hugo new {post_name}", shell=True, cwd=HUGO_ROOT, check=True)


def split_post_text(text, delimiter):
    # It's a yaml
    # https://gohugo.io/content-management/front-matter/
    first_line = text.find(delimiter)
    second_line = text.find(delimiter, first_line+len(delimiter))

    frontmatter = text[first_line + len(delimiter) : second_line]
    rest_content = text[second_line + len(delimiter) :]
    return frontmatter, rest_content

def get_image_text(img_path):
    return (
f"""{{{{< imgRel
pathURL="{img_path}"
alt=""
>}}}}\n""")

def move_image(img_path, target_path=DEFAULT_IMG_PATH, name=DEFAULT_IMG_NAME):
    raise NotImplementedError
    # target = os.path.join(HUGO_ROOT, target_path, name)
    # os.move(img_path, target)

def main(cli=None):
    args = parse_args(cli)

    if args.filename is None:
        filename = f"{TODAY}.md"
    else:
        filename = args.filename

    full_path = os.path.join(HUGO_ROOT, "content/post", filename)
    if args.img is not None:
        move_image(args.img)

    create_post(filename)
    img_text = get_image_text(os.path.join(DEFAULT_IMG_PATH, DEFAULT_IMG_NAME))

    with open(full_path, "r") as original:
        text = original.read()

    with open(full_path + ".bak", "w") as backup:
        backup.write(text)

    delimiter = "---\n"
    frontmatter, rest_content = split_post_text(text, delimiter)
    metadata = yaml.safe_load(frontmatter)

    metadata["categories"] = args.categories
    metadata["title"] = args.title

    output_metadata = yaml.safe_dump(metadata)

    with open(full_path, "w") as new:
        new.write(delimiter)
        new.write(output_metadata)
        new.write(delimiter)
        new.write("\n")

        new.write(img_text)
        new.write(rest_content)


if __name__ == "__main__":
    # cli=None
    main()