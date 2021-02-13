#!/bin/bash
export nombre_cont="ejemplo_app_rest"
export version=":v0.0.1"
docker build --network=host --tag $nombre_cont$version .;

docker run -it --entrypoint /bin/bash --network=host -v $PWD:/app 63693a563da4;