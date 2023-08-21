#!/bin/bash

cd ..
# Project root
mkdir -p instage

# instage.api structure
mkdir -p instage/instage.api/src/{controllers,models,routes,middlewares,gateways,utils}
# touch instage/instage.api/src/index.js
# touch instage/instage.api/package.json
touch instage/instage.api/.gitignore
touch instage/instage.api/Dockerfile

# DMX Service structure
mkdir -p instage/instage.service/src/
# mkdir -p instage/instage.service/src/{mqtt,dmx,poller}
# touch instage/instage.service/src/mqtt/listener.js
# touch instage/instage.service/src/dmx/controller.js
# touch instage/instage.service/src/poller/index.js
# touch instage/instage.service/src/index.js
# touch instage/instage.service/package.json
# touch instage/instage.service/.gitignore
# touch instage/instage.service/Dockerfile

# Frontend structure
mkdir -p instage/instage.app
# mkdir -p instage/instage.app/{public,src/components,src/scenes}
# touch instage/instage.app/src/App.js
# touch instage/instage.app/src/index.js
# touch instage/instage.app/package.json
# touch instage/instage.app/.gitignore
# touch instage/instage.app/Dockerfile

# Other root files
touch instage/docker-compose.yml
touch instage/README.md

echo "Folder structure created successfully!"
