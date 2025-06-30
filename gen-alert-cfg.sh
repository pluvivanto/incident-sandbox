#!/usr/bin/env bash

set -euo pipefail

export $(grep -v '^#' .env | xargs)
envsubst <alertmanager/alertmanager.yml.tmpl >alertmanager/alertmanager.yml
