from torch.utils.data import Dataset
categories = set()
default_data_file='./data/solve.txt'
class PeopleDaily(Dataset):
    def __init__(self,data_file=default_data_file):
        self.data=self.load_data(data_file)

    def load_data(self,datafile):
        Data={}
        with open(datafile,'rt',encoding='utf-8') as f:
            for idx,line in enumerate(f.read().strip().split('\n\n')):
                if not line:
                    break
                sentence,tags='',[]
                for i ,c in enumerate(line.split('\n')):
                    word,tag=c.split(' ')
                    sentence+=word
                    if tag[0]=='B':
                        tags.append([i,i,word,tag[2:]])
                        categories.add(tag[2:])
                    elif tag[0]=='I':
                        tags[-1][1]=i
                        tags[-1][2]+=word
                Data[idx]={
                    'sentence':sentence,
                    'tags':tags
                }

            return Data


    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]


