#!/bin/bash
# Create the data directory
mkdir -p data
# Download the data file
poetry run kaggle datasets download -d mjshri23/life-expectancy-and-socio-economic-world-bank
# Unzip the data file
unzip life-expectancy-and-socio-economic-world-bank.zip -d data
# Rename the data file
mv data/life\ expectancy.csv data/life_expectancy.csv
# Remove the zip file
rm life-expectancy-and-socio-economic-world-bank.zip
