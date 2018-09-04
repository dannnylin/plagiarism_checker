from synonym_service import *
from string import punctuation

DEFAULT_TUPLE_SIZE = 3

class PlagiarismDetector(object):
  """PlagarismDetector class for doing heavy lifting of finding similarity percentage of 2 texts."""

  def __init__(self, file1, file2, syns, tuple_size):
    """Loads all of the necessary filepaths for the class.
    
    Args:
        file1      (str) : File path for first text file 
        file2      (str) : File path for second text file
        syns       (str) : File path for syns file
        tuple_size (int) : Tuple size for words in files
    """

    if tuple_size == None:
      tuple_size = DEFAULT_TUPLE_SIZE

    if tuple_size <= 0:
      raise Exception("Tuple size cannot be less than or equal to 0")

    self.file1 = file1
    self.file2 = file2
    self.tuple_size = tuple_size
    self.syn_service = SynonymService(syns)
  
  def get_words_from_file(self, file_path):
    """Parses words from a given file path.
    
    Args:
        file_path  (str) : File path for text file 
    """

    with open(file_path, 'r') as file:
      text = file.read().replace('\n', ' ')
      words = text.split()
      return words
  
  def get_tuples_from_words(self, words, target=False):
    """Given a list of words, generate tuples from it.
    
    Args:
        words   (list) : List of words
        target  (bool) : Flag for whether file is the target text file
    """

    if len(words) < self.tuple_size:
      raise Exception("Tuple size greater than the total number of words in file")

    tuples = set()
    for i in range(len(words) - self.tuple_size + 1):
      tup = words[i:i+self.tuple_size]
      tuples.add(tuple(tup))
      if target:
        for i in range(len(tup)):
          if tup[i] in self.syn_service.syns_map:
            for syn in self.syn_service.get_synonyms_for_word(tup[i]):
              tup[i] = syn
              syn_tuple = tuple(tup)
              tuples.add(syn_tuple)
              
    return tuples
  
  def get_similarity_percentage(self):
    """Use generated tuples to count occurrences of tuples in file2 in file1."""

    # Remove punctuation from words and make them lowercase
    translator = str.maketrans('', '', punctuation)
    source_words = [(word.lower()).translate(translator) for word in self.get_words_from_file(self.file1)]
    target_words = [(word.lower()).translate(translator) for word in self.get_words_from_file(self.file2)]

    source_tuples = self.get_tuples_from_words(source_words)
    target_tuples = self.get_tuples_from_words(target_words, True)

    similarity_count = 0
    for tup in source_tuples:
      if tup in target_tuples:
        similarity_count += 1

    return int(similarity_count/len(source_tuples) * 100)
