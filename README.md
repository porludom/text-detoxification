## Text detoxification
### Roman Voronov
### ro.voronov@innopolis.university
### Group b21-DS-02
    
Here is the repository for the first assignment about Text detoxification.

The examples how my best model performs detoxification:

First: \
Input: __This shit reminded me too much of my shit past when I was killing people for damn nothing__ \
Output: This reminded me too much of my past when I killed people for nothing \
  
Second: \
Input: __I don't know how you eat pancakewiches. they look so awful__\
Output: I don't know how you eat pancakes, they look terrible \

So, the model can easily rephrase many swear phrases to more polite ones.
### Model I will describe next
Next sections I will be talking about trained on detoxofication task t5-small model.
This repository also contains other model in __notebooks/2.bert_replace_model__. This is the model that looks for swear words in the sentence, masks them and asks BERT language model to replace those masks by more polite words. Obviously, this model not more than baseline model that gives poor results in comparison to transformer trained to the detoxification task

### Running the model
Do the following to run the model
1. Download the repository. For example. using __git clone https://github.com/porludom/text-detoxification.git__
2. Run the __src/models/t5_use.py__ file with arguments specified below

When running t5_use.py, you should specify the following arguments:

The input string. What to detoxificate, like "Holly shit, it was a mistake"
--model_path. The path to model. By default it is "./../../models/modelka", the pretrained model by me
--tokenizer_path. The path to tokenizer. By default it is "./../../models/tokenizer", the official tokenizer for t5-small

### The structure of repository
- __data__ folder contains all the data used.

- __models__ folder contains models, tokenizers trained or used

- __notebooks__ folder contains all the .py and .ipynb files used

- __reports__ folder contains reports for the course purposes

- __src__ folder contains all about final model (t5-small trained)

- - __models__ folder contains all the files to train and run t5-small models on detoxification task
