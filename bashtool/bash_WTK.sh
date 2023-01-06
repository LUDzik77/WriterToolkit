#!/bin/bash

# Check if the first argument is "add" or "remove"
if [ "$1" == "add" ]; then
  # Check if a name was provided
  if [ -z "$2" ]; then
    echo "Error: No name provided"
  else
    # Check if a feature was provided
    if [ -z "$3" ]; then
      echo "Error: No feature provided"
    else
      # Check if the name already exists in the file
      grep -q "$2" names.txt
      if [ $? -eq 0 ]; then
        # Name already exists, append feature to the existing line
        sed -i "s/$2.*/$2 $3/g" names.txt
      else
        # Name does not exist, add new line with name and feature
        echo "$2 $3" >> names.txt
      fi
      echo "Added $3 to $2 in the names file"
    fi
  fi
elif [ "$1" == "remove" ]; then
  # Check if a name was provided
  if [ -z "$2" ]; then
    echo "Error: No name provided"
  else
    # Check if a feature was provided
    if [ -z "$3" ]; then
      # No feature provided, remove entire line with name
      sed -i "/$2/d" names.txt
      echo "Removed $2 from the names file"
    else
      # Feature provided, remove only the specified feature from the line
      sed -i "s/$2 $3/ /g" names.txt
      echo "Removed $3 from $2 in the names file"
    fi
  fi
else
  echo "Error: Invalid command"
fi
