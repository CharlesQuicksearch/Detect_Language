#import dependencies
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from languages import Language
from languages_ISO import language_codes

model = AutoModelForSequenceClassification.from_pretrained('Language_Detection_Model/Bert_Detect_Language_Model')
tokenizer = AutoTokenizer.from_pretrained('Language_Detection_Model/Bert_Detect_Language_Tokenizer')

async def detect_language(input_string):

    tokens = tokenizer.encode(input_string, return_tensors='pt')
    result = model(tokens)
    result_logits = result.logits
    result_index = int(torch.argmax(result_logits))

    result_language = Language(result_index).name

    #check for matching rows in languages_ISO
    matching_row = language_codes[language_codes['id'] == result_language]

    #If the languages is not supported, see languages_ISO, return not supported
    if len(matching_row) == 0:
        return ["Not supported", "If supported, try a longer sentence.", "0"]

    language_code = matching_row['code2'][0].item()
    score = str(round(result_logits[0][result_index].item()))

    return [result_language, language_code, score]
