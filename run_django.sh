#!/bin/bash
port=8000
project_dir=/Users/julialocamuz/Desktop/RUFUS/rufus_menu

# Change to the project directory
cd $project_dir

# Check if a process is running on the port
if [[ $(lsof -i :$port) ]]; then
  echo "Killing processes running on port $port"
  # Kill processes running on the port
  kill $(lsof -t -i :$port)
fi

# Start Django on the specified port
echo "Starting Django on port $port"
python manage.py runserver $(ifconfig | grep "inet " | grep -v 127.0.0.1 | awk '{print $2}'):$port
