#!/bin/bash

# Exit on error
set -e

# Function to increment version
increment_version() {
    local version=$1
    local major minor patch

    # Split version into major.minor.patch
    IFS='.' read -r major minor patch <<< "$version"

    # Increment patch version
    patch=$((patch + 1))

    echo "$major.$minor.$patch"
}

# Get the current version from pyproject.toml
current_version=$(grep '^version = ' pyproject.toml | sed 's/version = "\(.*\)"/\1/')
echo "Current version: $current_version"

# Calculate new version
new_version=$(increment_version "$current_version")
echo "New version: $new_version"

# Update version in pyproject.toml
sed -i "s/^version = \"$current_version\"/version = \"$new_version\"/" pyproject.toml

# Stage and commit the version change
git add pyproject.toml
git commit -m "Release version v$new_version"

# Create and push the new tag
git tag "v$new_version"
git push origin main "v$new_version"

echo "Successfully bumped version to $new_version and pushed to GitHub" 