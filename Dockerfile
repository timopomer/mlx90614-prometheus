FROM python:3.9
RUN python3.9 -m pip install build --user
COPY /src /tmp/build
WORKDIR /tmp/build
RUN python -m build --sdist --wheel --outdir dist/ .