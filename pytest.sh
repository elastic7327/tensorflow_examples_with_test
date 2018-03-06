#!/bin/sh

# pytest -s -v

pytest -s -v tests/chapter_2
# pytest -s -v tests/chapter_3

find . -name \*.pyc -delete
