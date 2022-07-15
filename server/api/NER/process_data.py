import os
import random
def process(source_file,target_file,out_file='./data/solve.txt'):
    with open(source_file,'r',encoding='utf-8') as f:
        paragraphs=f.read().split('\n')
        paragraphs=[sentence.split() for sentence in paragraphs]
    with open(target_file,'r',encoding='utf-8') as f:
        paragraphs_targets=f.read().split('\n')
        paragraphs_targets = [sentence.split() for sentence in paragraphs_targets]
    ans=[]
    for i in range(len(paragraphs)):
        sentence=[[word,target] for word,target in zip(paragraphs[i],paragraphs_targets[i]) ]
        ans.append(sentence)
    with open(out_file,'w',encoding='utf-8') as f:
        for i in range(len(paragraphs)):
            for word in ans[i]:
                f.write(' '.join(word)+'\n')
            f.write('\n')         

def div_train_and_valid(source,num=None):
    with open(source,'r',encoding='utf-8') as f:
        list=f.read().strip().split('\n\n')
        random.shuffle(list)
    source=source.replace('.txt','')
    max_len=len(list)
    train_num=int(max_len*0.7)
    with open(source+'.train.txt','w',encoding='utf-8') as f:
        train_list=list[:train_num]
        if num==None:
            for paragraph in train_list:
                f.write(paragraph+'\n\n')
        else:
            for i,paragraph in enumerate(train_list):
                f.write(paragraph+'\n\n')
                if i==num-1:
                    break

    with open(source+'.valid.txt','w',encoding='utf-8') as f:
        valid_list=list[train_num:]
        if num==None:
            for paragraph in valid_list:
                f.write(paragraph+'\n\n')
        else:
            for i,paragraph in enumerate(valid_list):
                f.write(paragraph+'\n\n')
                if i==int(num*0.2):
                    break




source_file='./data/source_BIO_2014_cropus.txt'
target_file='./data/target_BIO_2014_cropus.txt'


source_path='./data/solve.txt'

div_train_and_valid(source_path,5000)
