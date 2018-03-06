#!/bin/sh

pytest -s -v
find . -name \*.pyc -delete
