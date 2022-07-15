import torch
from .Token import tokenizer,ids_to_labels
from .model import BertNER
weights='D:/ModelWeights/NER/BERTNER/weights5.bin'
model=BertNER()
model.load_state_dict(torch.load(weights,map_location='cpu'))
def token_classify(s):
    encoding=tokenizer(
        s,
        padding=True,
        truncation=True,
        return_tensors="pt"
    )
    out=model(encoding)
    out=torch.argmax(out,dim=-1)
    res={}
    for ans in out:
        for i,val in enumerate(ans):
            if val!=0 and encoding.token_to_word(i)!=res.keys() :
                id=encoding.token_to_word(i)
                start,end=encoding.word_to_chars(id)
                res[encoding.token_to_word(i)]=[start,end,ids_to_labels[val.item()][2:]]
    #print(res)
    return res

def parse_token(s,token):
    ans=''
    colors={
        'ORG':'#E0FFFF','LOC':'#FFE4C4','PER':'#F0FFF0','T':'#E3E3E3'
    }
    span='<span style="background-color:{};">{}</span>'
    next=0
    tags={}
    for key in token.keys():
        start,end,tag=token[key]
        if tag not in tags.keys():
            tags[tag]=colors[tag]
        #print(start)
        ans+=s[next:start]
        ans+=span.format(colors[tag],s[start:end])
        next=end
    if next<len(s):
        ans+=s[next:]
        #print(ans)
    return  ans,tags



















