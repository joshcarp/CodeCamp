FROM jupyter/minimal-notebook:2ce7c06a61a1
# Get the latest image tag at:
# https://hub.docker.com/r/jupyter/minimal-notebook/tags/
# Inspect the Dockerfile at:
# https://github.com/jupyter/docker-stacks/tree/master/minimal-notebook/Dockerfile

# install additional package...
RUN pip install nbgitpuller --no-cache-dir astropy

