
rm -rf docs/
git add --all
git commit -m "Reload Doc - script"
hugo
git add --all
git commit -m "Reload Doc - script"
git push origin master
