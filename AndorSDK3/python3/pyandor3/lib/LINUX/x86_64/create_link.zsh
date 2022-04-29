#!/usr/bin/env zsh

local version="3.13.30001.0"

for f in `ls *$version`; do
  ln -sf $f ${f//\.$version/} 
done
