#!/bin/bash

work_repo=~/2600/Exos/math/turingtoy-base


cd /tmp
rm -rf /tmp/test_turingtoy
git clone https://gitlab.com/maths-2600/turingtoy-base.git test_turingtoy
cd test_turingtoy
source .devenv/bash_init.sh
cp $work_repo/src/turingtoy/__init__.py src/turingtoy/__init__.py
nox -s tests
rm -rf test_turingtoy
