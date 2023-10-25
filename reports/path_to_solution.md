## Report about how I came up with the final model I have

### Baseline model
The first model I created was the following: \
- Model takes the input, and masks all swear phrases using large predefined set of constructions. The data can be accesed from __/data/external__
- Then model propogated the masked sentence to BERT that tries to fill those masks.
- Algorithm checks the variants BERT proposes, and takes not toxic ones.

Example of how model works:\
Input: __You are fucking nothing in talking to people__\
Output: You are absolutely nothing in talking to people

This model has obvious problems: 
1. it cannot rephrase some part of the sentence, it can only replace some words by another.
2. it cannot detect some swear words from young slang, so they go unsees through the model

While the second problem cannot be solved by any model (even human do not know every word in slang), the first can be easily solved by the following model.
### Training a transformer
After a baseline, I decided to train a transformer right after, since transformer would be better than RNN and other models.\
I chose the t5-small transformer since it was powerful enough and small enough to train in few hours. The results of training were great, they can be seen in the second report
