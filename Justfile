image := "trustial-dev"
port := "1313"

# Build the devcontainer image
docker-build:
    docker build -t {{image}} .devcontainer/

# Start dev server with drafts at localhost:1313
dev: _ensure-image
    docker run --rm -v "$(pwd):/src" -w /src -p {{port}}:{{port}} {{image}} \
        bash -c "npm install && hugo server --bind 0.0.0.0 -D"

# Production build
build: _ensure-image
    docker run --rm -v "$(pwd):/src" -w /src {{image}} \
        bash -c "npm install && npm run build"

# Production preview at localhost:1313
preview: _ensure-image
    docker run --rm -v "$(pwd):/src" -w /src -p {{port}}:{{port}} {{image}} \
        bash -c "npm install && hugo server --bind 0.0.0.0 --disableFastRender -e production --minify"

# Format content and templates
format:
    npm run format

_ensure-image:
    #!/usr/bin/env bash
    if ! docker image inspect {{image}} > /dev/null 2>&1; then
        echo "Image '{{image}}' not found, building..."
        docker build -t {{image}} .devcontainer/
    fi
