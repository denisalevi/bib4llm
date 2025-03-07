#!/bin/bash

# make_release.sh - Version increment and release script
#
# This script automates the process of incrementing the version number in pyproject.toml,
# committing the change, creating a git tag, and pushing to GitHub.
#
# Usage: ./make_release.sh [major|minor|patch|--help]
#   - major: Increments the major version (X.0.0)
#   - minor: Increments the minor version (0.X.0)
#   - patch: Increments the patch version (default, 0.0.X)
#   - --help: Display this help message

# Exit on error
set -e

# Function to display help
show_help() {
    echo "Usage: ./make_release.sh [major|minor|patch|--help]"
    echo ""
    echo "Options:"
    echo "  major    Increments the major version (X.0.0)"
    echo "  minor    Increments the minor version (0.X.0)"
    echo "  patch    Increments the patch version (default, 0.0.X)"
    echo "  --help   Display this help message"
    echo ""
    echo "This script automates the process of incrementing the version number in pyproject.toml,"
    echo "committing the change, creating a git tag, and pushing to GitHub."
    exit 0
}

# Function to increment version
increment_version() {
    local version=$1
    local increment_type=${2:-"patch"}
    local major minor patch

    # Split version into major.minor.patch
    IFS='.' read -r major minor patch <<< "$version"

    # Increment version based on type
    case "$increment_type" in
        "major")
            major=$((major + 1))
            minor=0
            patch=0
            ;;
        "minor")
            minor=$((minor + 1))
            patch=0
            ;;
        "patch")
            patch=$((patch + 1))
            ;;
        *)
            echo "Invalid increment type: $increment_type. Using 'patch' as default."
            patch=$((patch + 1))
            ;;
    esac

    echo "$major.$minor.$patch"
}

# Check for help flag
if [[ "$1" == "--help" ]]; then
    show_help
fi

# Get the increment type from command line argument (default to "patch")
increment_type=${1:-"patch"}

# Get the current version from pyproject.toml
current_version=$(grep '^version = ' pyproject.toml | sed 's/version = "\(.*\)"/\1/')
echo "Current version: $current_version"

# Calculate new version
new_version=$(increment_version "$current_version" "$increment_type")
echo "New version: $new_version"

# Ask for user confirmation
read -p "Do you want to proceed with bumping version from $current_version to $new_version? (y/n): " confirm
if [[ "$confirm" != "y" && "$confirm" != "Y" ]]; then
    echo "Version bump cancelled."
    exit 0
fi

# Update version in pyproject.toml
sed -i "s/^version = \"$current_version\"/version = \"$new_version\"/" pyproject.toml

# Stage and commit the version change
git add pyproject.toml
git commit -m "Release version v$new_version"

# Create and push the new tag
git tag "v$new_version"
git push origin main "v$new_version"

echo "Successfully bumped version to $new_version and pushed to GitHub" 