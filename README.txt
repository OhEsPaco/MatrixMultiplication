Run all
powershell cat example1.txt | python mapper.py | sort | python reducer.py > out.txt

Run mapper
powershell cat example1.txt | python mapper.py