#!/bin/bash


cd /tmp
rm -rf /tmp/test_turingtoy
git clone https://gitlab.com/maths-2600/turingtoy-base.git test_turingtoy
cd test_turingtoy
source .devenv/bash_init.sh
cp ~/2600/Exos/math/turingtoy-base/src/turingtoy/__init__.py src/turingtoy/__init__.py
nox -s tests
rm -rf test_turingtoy
