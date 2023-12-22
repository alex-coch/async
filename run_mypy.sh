#!/bin/bash

if [ $# -eq 0 ]; then
  poetry run mypy --strict --explicit-package-bases --ignore-missing-imports .
else
  poetry run mypy --strict --explicit-package-bases --ignore-missing-imports "$@"
fi
