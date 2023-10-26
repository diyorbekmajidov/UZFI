#!/bin/bash

# Ask for the file to add
echo "Enter the file you want to add to git:"
read file

# Check if file exists
# if [ ! -f "$file" ]; then
#     echo "$file does not exist."
#     exit 1
# fi

# Add the file to git
git add $file

# Ask for commit message
echo "Enter commit message:"
read message

# Commit to git
git commit -m "$message"

# Push to git
git push origin HEAD
