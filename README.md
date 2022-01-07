# hugotools


## Quick start:

```
git clone git@github.com:elehcim/hugotools.git
cd hugotools
pip install .
```

## Usage
```
$ hugojot --help
usage: hugojot [-h] [-f FILENAME] [--img IMG] [-t TITLE] [--tags TAGS]
               [-c CATEGORIES [CATEGORIES ...]]

options:
  -h, --help            show this help message and exit
  -f FILENAME, --filename FILENAME
                        New file (default to <TODAY>.md)
  --img IMG             Image file to be moved
  -t TITLE, --title TITLE
                        Title of the post
  --tags TAGS           Tags to be put in the post metadata
  -c CATEGORIES [CATEGORIES ...], --categories CATEGORIES [CATEGORIES ...]
                        Categories to be put in the post metadata
```

The environment variable HUGO_ROOT must be set (e.g. in `~/.bashrc`) to the root folder of the website you want to interact with.
```
export HUGO_ROOT=/path/to/hugo/website/root
```
Otherwise the command assumes the working directory to be the hugo root directory itself (for paths and relative paths).

