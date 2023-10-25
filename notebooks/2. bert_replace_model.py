
import pandas as pd
import numpy as np
from transformers import pipeline
from typing import List
import pickle
import argparse

parser = argparse.ArgumentParser(description='Detoxification')
parser.add_argument('input', type=str, help='String to detoxificate')
args = parser.parse_args()

class SwearWordsRemover():
  def __init__(self, unmasker, word_of_censor : str, list_of_swear_phrases : List) -> None:
    '''
    Unmasker is the model to use while replacing swear words
    word_of_censor is the word to use instead of swear words, when model cannot replace the swear word by non swear one
    list_of_swear_phrases - words and phrases in blacklist. Added to basin dictionary of better_profanity library
    '''
    from better_profanity import profanity
    self.unmasker = unmasker # pipeline('fill-mask', model='bert-large-uncased-whole-word-masking')
    self.word_of_censor = word_of_censor
    profanity.add_censor_words(list_of_swear_phrases)
    self.profanity = profanity
      
  def __call__(self, input_string) -> str:
    masked_input = self.profanity.censor(input_string).replace("****", "[MASK]")
    number_of_masks = masked_input.count("[MASK]")
    variants_to_replace = self.unmasker(masked_input)
    for mask_number in range(number_of_masks): # look at recomendation for every mask
      variants = variants_to_replace[mask_number] if number_of_masks >1 else variants_to_replace
      for proposed_dict in variants: #iterate over words BERT has given
        proposed_word = proposed_dict["token_str"]  # get word
        if proposed_word.isalpha() and not self.profanity.contains_profanity(proposed_word): # check is it word and is it not swear
          masked_input = masked_input.replace("[MASK]", proposed_word, 1) # only the first mask to replace.
          break
        masked_input = masked_input.replace("[MASK]", self.word_of_censor, 1)
    return masked_input

with open('./../models/remover.pkl', 'rb') as f: 
    remover = pickle.load(f) # already created remover. 

print(remover(args.input))

