#!/bin/bash

# Credentials
REMOTE_USER="your_username"
PASSWORD="your_password"


# Remote machine details
REMOTE_HOST="ppr.cse.iitk.ac.in"
REMOTE_DIR="/users/phd/$REMOTE_USER"


# Check if the correct number of arguments is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 Invalid file path."
    exit 1
fi

# Variables
FILE_PATH=$1
REMOTE_FILE="$REMOTE_DIR/$(basename "$FILE_PATH")"


# KD Second Floor, Network Room
PRINT_COMMAND="ppr -d lp2 --feature Duplex=DuplexNoTumble $REMOTE_FILE"

# KD Ground Floor Lab
# PRINT_COMMAND="ppr -d lp1 --feature Duplex=DuplexNoTumble $REMOTE_FILE"




# Step 1: Copy the file to the remote machine
echo "|-Copying file to $REMOTE_USER@$REMOTE_HOST:$REMOTE_DIR..."
sshpass -p "$PASSWORD" scp "$FILE_PATH" "$REMOTE_USER@$REMOTE_HOST:$REMOTE_DIR"
if [ $? -ne 0 ]; then
    echo "|-Error: Failed to copy file."
    exit 1
fi
echo "|-File copied successfully."

# Step 2: SSH into the remote machine and execute the print command
echo "|-Connecting to $REMOTE_USER@$REMOTE_HOST to print the file..."
sshpass -p "$PASSWORD" ssh -T "$REMOTE_USER@$REMOTE_HOST" <<EOF
$PRINT_COMMAND
if [ \$? -eq 0 ]; then
    echo "|-Print command executed successfully."
else
    echo "|-Error: Print command failed."
    exit 1
fi
rm "$REMOTE_FILE"
if [ \$? -eq 0 ]; then
    echo "|-File removed successfully."
else
    echo "|-Error: Failed to remove file."
    exit 1
fi
EOF

# Step 3: Done
echo "|-Disconnected from the remote machine. Task completed."
