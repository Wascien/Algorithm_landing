from  transformers import AutoModel
from .Token import labels_to_ids
from torch import  nn


checkpoint='bert-base-chinese'
class BertNER(nn.Module):
    def __init__(self):
        super(BertNER, self).__init__()
        self.bert_encoder=AutoModel.from_pretrained(checkpoint)
        self.classifier=nn.Linear(768,len(labels_to_ids))


    def forward(self,X):
        value=self.bert_encoder(**X)

        out_put=self.classifier(value.last_hidden_state)

        return out_put

