from transformers import AutoTokenizer
import torch
import numpy as np
import json
import os
checkpoint='bert-base-chinese'
tokenizer=AutoTokenizer.from_pretrained(checkpoint)
labels_path= './data/label.json'
def get_labels(labels_path):
    with open(labels_path, 'r', encoding='utf-8') as f:
        labels = json.loads(f.read())
    id_to_labels,label_to_ids={},{}
    for key in labels.keys():
        id_to_labels[int(key)] =labels[key]
    for key in labels.keys():
        label_to_ids[labels[key]]=int(key)

    return id_to_labels,label_to_ids



ids_to_labels,labels_to_ids=get_labels(labels_path)

def batch_process_fn(batch):

    batch_sentences,batch_tags=[],[]

    for item in iter(batch):
        batch_sentences.append(item['sentence'])
        batch_tags.append(item['tags'])

    batch_input=tokenizer(
        batch_sentences,
        padding=True,
        truncation=True,
        return_tensors='pt'
    )
    batch_label=np.zeros(batch_input['input_ids'].shape,dtype=int)
    for s_idx, sentence in enumerate(batch_sentences):
        encoding = tokenizer(sentence, truncation=True)
        batch_label[s_idx][0] = -100
        batch_label[s_idx][len(encoding.tokens()) - 1:] = -100
        for char_start, char_end, _, tag in batch_tags[s_idx]:
            token_start = encoding.char_to_token(char_start)
            token_end = encoding.char_to_token(char_end)

            if token_start==None or char_start==None:
                continue
            batch_label[s_idx][token_start] = labels_to_ids[f"B-{tag}"]
            batch_label[s_idx][token_start + 1:token_end + 1] =labels_to_ids[f"I-{tag}"]

    return batch_input, torch.tensor(batch_label)