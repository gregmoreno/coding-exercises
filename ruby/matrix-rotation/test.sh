#!/bin/bash
cat input01-matrix-rotation.txt | ruby matrix-rotation.rb | diff - output01-matrix-rotation.txt
cat input04-matrix-rotation.txt | ruby matrix-rotation.rb | diff - output04-matrix-rotation.txt
cat input05-matrix-rotation.txt | ruby matrix-rotation.rb | diff - output05-matrix-rotation.txt

# To measure
# time cat input05-matrix-rotation.txt| ruby matrix-rotation.rb | diff - output05-matrix-rotation.txt
