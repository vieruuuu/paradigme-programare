#!/usr/bin/env bash
#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
GRAAL_BIN=$SCRIPT_DIR/../graalvm/bin

$GRAAL_BIN/javac $SCRIPT_DIR/src/Polyglot.java -d $SCRIPT_DIR/dist/
$GRAAL_BIN/java -cp $SCRIPT_DIR/dist Lab2/src/Polyglot
 