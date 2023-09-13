#!/bin/bash
# Create the data directory
mkdir -p data
# Download the data file
poetry run kaggle datasets download -d mjshri23/life-expectancy-and-socio-economic-world-bank
# Unzip the data file
unzip life-expectancy-and-socio-economic-world-bank.zip -d data
# Remove the zip file
rm life-expectancy-and-socio-economic-world-bank.zip
