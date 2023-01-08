#!/bin/bash

# ---> it works  cat test.txt |grep "$1"

dir="WTK"
if [ ! -d "$dir" ]; then
  mkdir "$dir"
fi
  
if [ "$1" == "add" ]; then
  if [ -z "$2" ]; then echo "Error: No name provided"
  else
    if [ -z "$3" ]; then echo "Error: No feature provided"
    else
    touch "$dir/$2.txt"
      echo "$2 $3" >> "$dir/$2.txt"
      echo "Added $3 to $2"
    fi
  fi
  
elif [ "$1" == "remove" ]; then
  if [ -z "$2" ]; then echo "Error: No name provided"
  else
    if [ -z "$3" ]; then sed -i "/$2/d" "$dir/$2.txt"
      echo "$2 removed"
    else
      sed -i "s/$2 $3/ /g" "$dir/$2.txt"
      echo "Removed $3 from $2"
    fi
  fi


elif [ "$1" == "read" ]; then  
  if [ -z "$2" ]; then
    for file in "$dir"/*; do
    #echo "File: $file"
    cat "$file"
    echo "---"
done
  else
    echo "here to change"

  fi

else
  echo "Error: Invalid command"
fi




# to look for 6 first characters of the feature>>
#first_6_chars=$(echo "$3" | cut -c 1-6)
#grep -q "$2 $first_6_chars" names.txt