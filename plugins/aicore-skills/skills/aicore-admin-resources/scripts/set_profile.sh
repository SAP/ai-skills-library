#!/usr/bin/env bash
# Usage: source set_profile.sh <profile>
#   e.g. source set_profile.sh aws.eu-central-1.prod-eu
#
# Reads credential files from AICORE_HOME (default: ~/.aicore).
# To list available profiles:
#   source set_profile.sh

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    echo "Error: this script must be sourced, not executed."
    echo "  source set_profile.sh <profile>"
    exit 1
fi

_CREDENTIALS_DIR="${AICORE_HOME:-$HOME/.aicore}"

_list_profiles() {
    for f in "$_CREDENTIALS_DIR"/config_*.json; do
        [[ -f "$f" ]] && basename "$f" | sed 's/config_//;s/\.json//'
    done
}

if [[ -z "$1" ]]; then
    echo "Usage: source set_profile.sh <profile>"
    echo ""
    echo "Available profiles (in $_CREDENTIALS_DIR):"
    _list_profiles | sed 's/^/  /'
    unset _CREDENTIALS_DIR
    unset -f _list_profiles
    return 1
fi

_PROFILE="$1"
_CRED_FILE="$_CREDENTIALS_DIR/config_${_PROFILE}.json"

if [[ ! -f "$_CRED_FILE" ]]; then
    echo "Error: credential file not found for profile '$_PROFILE'."
    echo "  Expected: $_CRED_FILE"
    echo ""
    echo "Available profiles (in $_CREDENTIALS_DIR):"
    _list_profiles | sed 's/^/  /'
    unset _CREDENTIALS_DIR _PROFILE _CRED_FILE
    unset -f _list_profiles
    return 1
fi

export AICORE_HOME="$_CREDENTIALS_DIR"
export AICORE_PROFILE="$_PROFILE"

echo "✓ AICORE_HOME=$AICORE_HOME"
echo "✓ AICORE_PROFILE=$AICORE_PROFILE"

unset _CREDENTIALS_DIR _PROFILE _CRED_FILE
unset -f _list_profiles
