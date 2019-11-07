#!/bin/bash

yarn test

# TODO: Rename all directories so that they are valid Python module names,
# which should make it possible to run unittest in Discovery mode.
find Python -name '*.py' -print0 | xargs -0 -n 1 python3
