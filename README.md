Instructions on running application:

Plagiarism Detection Tool
=========================
required arguments:
  -f file1 file2    files for checking plagiarism
  -s synonyms file  synonyms file

optional arguments:
  -n tuple size     size of tuples

Examples:
python app.py -f file1.txt file2.txt -s syns.txt -n 2 
(tuple size is set to 2)

OR

python app.py -f file1.txt file2.txt -s syns.txt
(tuple size is defaulted to 3)
