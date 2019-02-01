#!/bin/bash

PROJECT_NAME=data-and-algorithms
DIRECTORY=${PWD}
BASE_DIRECTORY=$(echo "$DIRECTORY" | rev | cut -d "/" -f1 | rev)

if [[("$1" != "")]]; then
   if [[("$BASE_DIRECTORY" != "$PROJECT_NAME")]]; then
      echo "Make sure you are in $PROJECT_NAME project"
      exit
   fi
   rootfileName=$1
   mkdir ./$rootfileName
   cp -a ./Python/ ./$rootfileName/
   rm ./$rootfileName/*/*/*.py
else
   echo "Missing folder name: sh createFolders.sh <folder_name>"
fi