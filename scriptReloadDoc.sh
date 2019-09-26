
rm -rf docs/
sleep 1
git add --all
sleep 1
git commit -m "Reload Doc - script"
sleep 1
hugo
sleep 1
git add --all
sleep 1
git commit -m "Reload Doc - script"
sleep 1
git push origin master
