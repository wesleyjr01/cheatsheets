git branch -r | grep -v 'origin/main' | grep -v 'origin/dev' | sed 's/origin\///' | xargs -I {} git push origin --delete {}
