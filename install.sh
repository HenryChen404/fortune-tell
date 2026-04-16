#!/bin/bash
set -e

REPO="https://github.com/HenryChen404/fortune-tell.git"
INSTALL_DIR="$HOME/.fortune-tell"
SKILL_LINK="$HOME/.claude/skills/fortune-tell-experts"

# 1. Detect language
if [[ "$LANG" == zh* ]]; then
  LANG_DIR="cn"
else
  LANG_DIR="en"
fi

# 2. Clone or update
if [ -d "$INSTALL_DIR/.git" ]; then
  git -C "$INSTALL_DIR" pull -q
else
  git clone "$REPO" "$INSTALL_DIR"
fi

# 3. Create symlink
mkdir -p "$(dirname "$SKILL_LINK")"
ln -sfn "$INSTALL_DIR/$LANG_DIR" "$SKILL_LINK"

echo "Installed fortune-tell ($LANG_DIR) → $SKILL_LINK"
