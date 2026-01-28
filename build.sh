#!/usr/bin/env bash
curl -LsSf --proto '=https' https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env

make install && make collectstatic && make migrate
