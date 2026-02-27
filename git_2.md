### вывести в файл логи с датими создания пять штук
git log --oneline --format="%h %ad %s" --date=iso --max-count=5>master_02.gitlog 


##### извлечь файлы из последнего коммита
git show --name-only --pretty="" HEAD | zip update.zip -@

посмтотерть архив 
zipinfo update.zip

#### перейти в проект
unzip update.zip

