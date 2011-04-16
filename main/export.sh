#!/bin/bash

WWW="/var/www/nightreading"

git update
git archive  | tar -C $WWW -xf -

