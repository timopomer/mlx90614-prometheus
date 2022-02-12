FROM python:3.9
RUN python3.9 -m pip install build --user
COPY /pyproject.toml /tmp/build/pyproject.toml
COPY /setup.py /tmp/build/setup.py
COPY /src /tmp/build/src
WORKDIR /tmp/build
RUN python -m build --sdist --wheel --outdir dist/ .