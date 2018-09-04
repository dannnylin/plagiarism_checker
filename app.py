from argparse import *
from plagiarism_detector import *

def main():
  """Uses an ArgumentParser to parse all of the given command line arguments for the program.

  Args:
      -f (str) : File paths for both of the text files
      -s (str) : File path for the synonyms file
      -n (int, optional) : Optional argument for choosing tuple size, defaulted to 3 if not set.
  """ 

  parser = ArgumentParser(description='Plagiarism Detection Tool')
  parser._action_groups.pop()
  required = parser.add_argument_group('required arguments')
  optional = parser.add_argument_group('optional arguments')
  required.add_argument('-f', required=True, nargs=2, metavar=('file1', 'file2'), type=FileType('r'), help='files for checking plagiarism')
  required.add_argument('-s', required=True, metavar='synonyms file', type=FileType('r'), help='synonyms file')
  optional.add_argument('-n', type=int, metavar='tuple size', help='size of tuples')
  args = parser.parse_args()
  
  file1, file2 = [file.name for file in args.f]
  syns = args.s.name
  tuple_size = args.n

  pd = PlagiarismDetector(file1, file2, syns, tuple_size)

  print("Plagiarism Detection Tool")
  print("==========================")
  print("File 1:", file1)
  print("File 2:", file2)
  print("Synonyms:", syns)
  print("Tuple Size:", tuple_size)
  print("==========================")
  print("Similarity Percentage:")
  print("%s%%" % (pd.get_similarity_percentage()))

if __name__ == "__main__":
  main()
