#!/bin/sh
# Avoid executing out of context
if [ -z "$ZSH" ]; then
  ZSH=~/.oh-my-zsh
fi
mkdir -p "$ZSH"
echo "Cloning Oh My Zsh..."
git clone --depth=1 https://github.com "$ZSH"
if [ $? -eq 0 ]; then
  echo "Successfully cloned! Setting up config..."
  cp "$ZSH/templates/zshrc.zsh-template" ~/.zshrc
  echo "Switching shell to zsh..."
  chsh -s zsh
  echo "Done! Restart Termux."
else
  echo "Git clone failed. Check your connection."
fi
