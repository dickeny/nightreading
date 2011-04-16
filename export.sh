#!/bin/bash

WWW="/var/www/nightreading"

git pull
git archive  master | tar -C $WWW -xf -

