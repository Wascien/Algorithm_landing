from train_ner import train,device
from model import BertNER
from torch import nn
from Token import batch_process_fn
from DataModel import PeopleDaily
from torch.utils.data import Dataset, DataLoader
from transformers import AdamW, get_scheduler
import torch
from transformers import logging
def main():
    logging.set_verbosity_error()
    train_data=PeopleDaily(data_file='./data/solve.train.txt')
    valid_data=PeopleDaily(data_file='./data/solve.valid.txt')
    train_data=DataLoader(dataset=train_data,batch_size=4,shuffle=True,collate_fn=batch_process_fn)
    valid_data = DataLoader(dataset=valid_data, batch_size=4, shuffle=True, collate_fn=batch_process_fn)
    learning_rate = 1e-5
    epoch_num = 3
    loss_fn = nn.CrossEntropyLoss()
    model=BertNER().to(device)
    optimizer =torch.optim.AdamW (model.parameters(), lr=learning_rate)
    lr_scheduler = get_scheduler(
        "linear",
        optimizer=optimizer,
        num_warmup_steps=0,
        num_training_steps=epoch_num * len(train_data),
    )
    total_loss=0
    train(train_data,valid_data,model,loss_fn,optimizer,lr_scheduler,epoch_num,total_loss)


if __name__ == '__main__':
    main()