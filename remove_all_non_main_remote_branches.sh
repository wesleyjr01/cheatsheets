git branch -r | sed 's/origin\///g' | awk -F/ '!/main$/ {if ($1) system("git push origin --delete " $1 "/" $2)}'
