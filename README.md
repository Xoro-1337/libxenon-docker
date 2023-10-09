# Libxenon Docker

This Dockerfile will build and configure a libxenon environment. This is using [Octal450](https://github.com/Octal450/)'s modified [libxenon](https://github.com/Octal450/libxenon).

## Installation

```bash
git clone https://github.com/Xoro-1337/libxenon-docker.git
cd libxenon-docker
docker build -t libxenon .
```

## Usage

```bash
docker run -ti -v "[Project Directory]:/mnt/share" libxenon:latest /bin/sh -c "su - libxenon"
```
