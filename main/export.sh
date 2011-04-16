#!/bin/bash

WWW="/var/www/nightreading"

git pull
git archive  | tar -C $WWW -xf -

