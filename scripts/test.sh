#!/bin/bash
# Activate virtual environment
. /appenv/bin/activate

# download requirements to build cache
pip3 download -d /build -r requirements_test.txt --no-input

# Install application test requirements
pip3 install --no-index -f /build -r requirements_test.txt


# Run test.sh arguments
exec $@
