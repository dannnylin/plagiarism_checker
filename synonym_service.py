class SynonymService(object):
  """SynonymService utilizes the synonyms file to map all synonyms."""

  def __init__(self, syns):
    """Loads all of the necessary filepaths for the class.

    Args:
        syns  (str) : File path for synonyms file
    """

    self.syns_map = self.map_synonyms(syns)

  def map_synonyms(self, syns):
    """Maps synonyms and returns a dictionary where each key is a word and the value is a set of synonyms.

    Args:
        syns  (str) : File path for synonyms file
    """

    syns_map = {}
    with open(syns, 'r') as file:
      lines = [x.strip() for x in file.readlines()]
      for line in lines:
        words = line.split()
        word_set = set(words)
        for word in words:
          if word not in syns_map:
            syns_map[word] = word_set
      return syns_map

  def get_synonyms_for_word(self, word):
    """Given a word, return the set of synonyms for that word.

    Args:
        word  (str) : Word to return synonyms for
    """
    return self.syns_map[word]
