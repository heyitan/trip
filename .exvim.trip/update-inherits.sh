#!/bin/bash
export DEST="./.exvim.trip"
export TOOLS="/Users/heyitan/.vim/tools/"
export TMP="${DEST}/_inherits"
export TARGET="${DEST}/inherits"
sh ${TOOLS}/shell/bash/update-inherits.sh
