#!/usr/bin/env bash

set -eu

DOMAIN="dnguyen0304"
NAMESPACE="roomlistwatcher"
VERSION=$(grep -Po "version='\K\d\.\d\.\d" setup.py)
REMOTE_SHARED_VOLUME="/tmp/build"

# Clean up existing packages created by previous builds.
rm --force ${NAMESPACE}*.zip

# Create the buildtime container.
tag=${DOMAIN}/${NAMESPACE}-buildtime:${VERSION}

if [ ! -z $(sudo docker images --quiet ${tag}) ]; then
    docker rmi --force ${tag}
fi
docker build \
    --file docker/buildtime/Dockerfile \
    --tag ${tag} \
    --build-arg COMPONENT=${NAMESPACE} \
    --build-arg SHARED_VOLUME=${REMOTE_SHARED_VOLUME} \
    .

# Create the package.
docker run \
    --rm \
    --volume $(pwd):${REMOTE_SHARED_VOLUME} \
    ${tag} \
    ${NAMESPACE} ${REMOTE_SHARED_VOLUME} ${VERSION}

# Create the container.
tag=${DOMAIN}/${NAMESPACE}:${VERSION}

if [ ! -z $(sudo docker images --quiet ${tag}) ]; then
    docker rmi --force ${tag}
fi
docker build \
    --file docker/Dockerfile \
    --tag ${tag} \
    --build-arg VERSION=${VERSION} \
    --build-arg NAMESPACE=${NAMESPACE} \
    .