#!/bin/bash

set -e

cd src-ui
git pull
npm install
./node_modules/.bin/ng build --prod
