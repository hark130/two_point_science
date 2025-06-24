#!/bin/sh

# This script was made to help automate how Pylint runs against the code base.
# This script will execute all commands regardless of how many fail and exit with a non-zero value.
#
# This script uses the following exit codes:
#   0 on success
#   1 if any Pylint command exits with a non-zero value


# GLOBAL VARIABLES
EXIT_CODE=0                # Value to exit with
ORIGINAL_DIRECTORY=$(pwd)  # Current working directory
# TEST_DIR=test              # Directory containing the project test code
SOURCE_DIR=tps             # Directory containing the project source code
DEVOPS_DIR=devops          # Directory containing the devops scripts


# PYLINT COMMANDS
# 1. Test Code
# cd $TEST_DIR
# if [ $? -ne 0 ]
# then
#     EXIT_CODE=1
#     exit $EXIT_CODE  # No need to go further if the directory is missing
# else
#     find ./ -type f -name "*.py" -not -name "__init__.py" | xargs python -m pylint --score=no --disable=import-error --disable=duplicate-code
#     if [ $? -ne 0 ]
#     then
#         EXIT_CODE=1
#     fi
# fi
# cd $ORIGINAL_DIRECTORY

# 2. TPS
cd $SOURCE_DIR
if [ $? -ne 0 ]
then
    EXIT_CODE=1
    exit $EXIT_CODE  # No need to go further if the directory is missing
else
    find ./ -type f -name "*.py" -not -name "__init__.py" | xargs python -m pylint --score=no --disable=duplicate-code
    if [ $? -ne 0 ]
    then
        EXIT_CODE=1
    fi
fi
cd $ORIGINAL_DIRECTORY

# 4. Devops Scripts
cd $DEVOPS_DIR
if [ $? -ne 0 ]
then
    EXIT_CODE=1
    exit $EXIT_CODE  # No need to go further if the directory is missing
else
#    find ./ -type f -name "*.py" -not -name "__init__.py" | xargs python -m pylint --score=no --disable=import-error
    if [ $? -ne 0 ]
    then
        EXIT_CODE=1
    fi
fi
cd $ORIGINAL_DIRECTORY

# DONE
cd $ORIGINAL_DIRECTORY
echo ""
exit $EXIT_CODE
