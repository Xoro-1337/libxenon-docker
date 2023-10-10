# Libxenon Docker

This Dockerfile will build and configure a libxenon environment. This is using [Octal450](https://github.com/Octal450/)'s modified [libxenon](https://github.com/Octal450/libxenon).

## Installation

```bash
git clone https://github.com/Xoro-1337/libxenon-docker.git
cd libxenon-docker
docker build -t libxenon .
```

## Usage

- DEFAULT METHOD

*NOTE: Modify the command with your desired project directory. Typically where the `Makefile` is.  
You may also `cd` there after booting the image if you choose a parent directory such as `C:/`.*

```bash
docker run -ti -v "[Project Directory]:/mnt/share" libxenon:latest /bin/sh -c "su - libxenon"
```

- PYTHON METHOD

*NOTE: The current working directory will automatically be mounted for you.*
     
```bash
cd [PROJECT DIRECTORY]
python3 build.py
```

## Compiling Your Project
1. Boot the Docker image using a method from above.
2. Once booted into the Docker, simply run `make`.
