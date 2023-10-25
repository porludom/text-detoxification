from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import argparse

parser = argparse.ArgumentParser(description='Detoxification')
parser.add_argument('input',
                    type=str, 
                    help='The string to detoxificate')
parser.add_argument('--model_path',
                    type = str,
                    default = "./../../models/modelka",
                    help = 'The path to language model. Downloaded with this notebook')
parser.add_argument("--tokenizer_path", 
                    type = str, 
                    default = "./../../models/tokenizer",
                    help = "The path to tokenizer. downloaded with this notebook.")
args = parser.parse_args()

model_path = args.model_path
tokenizer_path = args.tokenizer_path
model = AutoModelForSeq2SeqLM.from_pretrained(model_path, local_files_only = True)
tokenizer = AutoTokenizer.from_pretrained(tokenizer_path, local_files_only = True)

text = args.input
tokenized_text = tokenizer(text, return_tensors = "pt")
out = model.generate(input_ids = tokenized_text["input_ids"], attention_mask = tokenized_text["attention_mask"], max_length = 128)
preds = [
        tokenizer.decode(gen_id,
        skip_special_tokens = True,
        clean_up_tokenization_spaces=True)
        for gen_id in out ]

print(preds[0])

