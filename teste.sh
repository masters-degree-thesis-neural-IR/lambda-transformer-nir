#!/bin/sh

pip install --target ./package -r requirements.txt

#cp -rp package built
cp -rp model built
cp main.py built
cp main.py built