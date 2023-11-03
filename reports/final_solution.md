## Report about final solution

### Model
The final solution is chosen to be fine-tuned t5-small transformer on the dataset provided.\
### Metrics
As a metrics I used BLEU and gen_len\
### Training
The model was trained for 5 epochs in 6 hours with batch size = 16, lr = 0.00002.\
The final score of BLEU I achieves is __25.39__ that is good for sequence to sequence model.\
Of course the BLEU is not perfect metric, since it cannot properly evaluate the sentences with exact meanings but different words. Only human can...\
Here are the metrics during training:\
![scores](/reports/figures/scores1.png)

\
\
Here are some examples of model work that show the correct behaviour of the model:
- Input : __oh, I have fucked up, sorry. what can I do for you, fucking nerd?__
- Output: I'm sorry, what can I do for you, nerd?
-----------------------------------------
- Input: __I don't know how you eat pancakewiches. they look so awful__
- Output: I don't know how you eat pancakes, they look terrible
