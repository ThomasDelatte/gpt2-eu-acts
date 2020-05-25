#!/usr/bin/env bash

wget -O data/datasets/datasets.zip http://nlp.cs.aueb.gr/software_and_datasets/EURLEX57K/datasets.zip
unzip data/datasets/datasets.zip -d data/datasets/EURLEX57K
rm data/datasets/datasets.zip
rm -rf data/datasets/EURLEX57K/__MACOSX
mv data/datasets/EURLEX57K/dataset/* data/datasets/EURLEX57K/
rm -rf data/datasets/EURLEX57K/dataset