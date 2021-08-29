#!/bin/bash

echo "command: [chmod]"
echo "========================================================================"
echo "change only \"user\"  rights:             \$chmod -u=+wrx"
echo "change only \"group\" rights:             \$chmod -g=+wrx"
echo "change only \"other\" rights:             \$chmod -o=+wrx"
echo "change \"all\"        rights:             \$chmod -ugo=+wrx"
echo "Remove all \"user\" rights:               \$chmod -u=0"
echo "Remove all \"user\" rights (alternative): \$chmod -u=-wrx"
echo "========================================================================"
