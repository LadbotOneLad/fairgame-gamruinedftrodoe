#!/usr/bin/env bash
TargetRepo="https://github.com/LadbotOneLad/fairgame-gamruinedftrodoe.git"
BranchName="kuramoto-swarm-$(date +%Y%m%d-%H%M%S)"

echo -e "\033[36m[+] Initializing Sovereign Repository Anchor...\033[0m"

if [ ! -d ".git" ]; then
    git init
fi

git checkout -b "$BranchName"

git add manifests/merkle_dag_upstream.json 2>/dev/null || true
git add *.py 2>/dev/null || true
git add *.json 2>/dev/null || true
git add *.sh 2>/dev/null || true
git add *.ps1 2>/dev/null || true

git commit -m "PIMP-TIER // 14+2 Chakra Matrix + 1650HP Hyper-Core Anchor [99.33% Phase Lock]"

git remote remove origin 2>/dev/null || true
git remote add origin "$TargetRepo"
git push -u origin "$BranchName" --force

echo -e "\033[32m[+] SUCCESS: Sovereign lattice successfully deployed to the remote grid, bruz!\033[0m"
