Plagiarism Detection Tool
=========================
Instructions on running application:

<b>required arguments:</b>
<blockquote>
-f file1 file2    files for checking plagiarism
  -s synonyms file  synonyms file
</blockquote>

<b>optional arguments:</b>
<blockquote>
  -n tuple size     size of tuples
</blockquote>

<b>Examples:</b>
<blockquote>python app.py -f file1.txt file2.txt -s syns.txt -n 2</blockquote> 
(tuple size is set to 2)

OR

<blockquote>python app.py -f file1.txt file2.txt -s syns.txt</blockquote>
(tuple size is defaulted to 3)
