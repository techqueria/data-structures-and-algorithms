#!/bin/bash

DIRECTORY="$(git rev-parse --show-toplevel)"

if [[ $# -lt 1 ]]; then
  echo "Usage: bash createDirectories.sh <programming language>" >&2
  exit 1
fi

programmingLanguage="$1"
rsync --archive --include='*/' --exclude='*' "${DIRECTORY}/Python/" \
      "${DIRECTORY}/${programmingLanguage}/"