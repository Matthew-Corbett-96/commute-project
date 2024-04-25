#!/bin/bash

echo "Starting server..."
python -m guniicorn flaskr.run:app