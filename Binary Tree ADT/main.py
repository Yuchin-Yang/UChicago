# Nahom Ayele, Yuqin Yang
from brailletree import BrailleTree

def is_yes(response):
  '''Was it a yes response?'''
  return response == "yes" or response=="y" or response=="Yes" or response == "Y"

def main():
  ''' Run Braille Translator
  '''
  # see if printing tree as we go
  debug_mode = input("Print tree as you go?")
  debug = is_yes(debug_mode)

  # Assemble initial tree
  braille_tree = BrailleTree()
  # read values from file
  braille_tree.read_file("alphabet.txt")
  if debug:
    braille_tree.print()
  # write traversal of tree
    '''Uncomment to run your write_values function'''
  braille_tree.write_values("traversal.txt")
  interactive_translator(braille_tree, debug)



def interactive_translator(braille_tree, debug):
  # interactive translator
  while True:
    braille = input("Give a braille sequence of 0's and 1's to translate.\n")
    
    # Check input braille sequence
    if len(braille) % 6 != 0:
      raise ValueError("Invalid length of number of 0 and 1!")
      
    for i in braille:
      if i not in '01':
        raise ValueError("Cannot contain number except 0 and 1!")

    n = 6
    full_words = [braille[i:i + n] for i in range(0, len(braille), n)]
    translation = ''
    for i in full_words:
      translation += braille_tree.check_braille(i)

    if translation != None:
      print("Braille Translation: ", translation)
    else:
      print("Braille sequence", braille, "not in tree.")

    if debug:
      braille_tree.print()
      print()

    response = input("Enter another sequence? ")
    if not is_yes(response):
      break


if __name__=="__main__":
  main()