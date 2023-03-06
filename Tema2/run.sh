#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
GRAAL_BIN=$SCRIPT_DIR/../graalvm/bin

$GRAAL_BIN/js --polyglot $SCRIPT_DIR/src/pb2.js
$GRAAL_BIN/js --polyglot $SCRIPT_DIR/src/pb3.js
