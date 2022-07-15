import torch
from Token import labels_to_ids,ids_to_labels
from seqeval.metrics import classification_report
from seqeval.scheme import IOB2
from tqdm.auto import  tqdm
device = 'cuda' if torch.cuda.is_available() else 'cpu'
def train_loop(data,model,loss_fn,optimizer,lr_scheduler,epoch,total_loss):
    process_bar=tqdm(range(len(data)))
    process_bar.set_description(f'loss:{0:>7f}')
    finish_batch_num=(epoch-1)*len(data)

    model.train()
    for batch,(X,y) in enumerate(data,start=1):
        X, y = X.to(device), y.to(device)

        pred=model(X)
        optimizer.zero_grad()

        loss=loss_fn(pred.permute(0,2,1),y.long())
        loss.backward()
        optimizer.step()
        lr_scheduler.step()
        total_loss+=loss.item()
        process_bar.set_description(f'loss:{total_loss/(finish_batch_num+batch):>7f}')
        process_bar.update(1)
    return total_loss


def test_loop(data,model):
    true_labels,true_pred=[],[]
    model.eval()
    with torch.no_grad():
        for X,y in tqdm(data):
            X, y = X.to(device), y.to(device)
            pred=model(X)
            pred=pred.argmax(dim=-1)
            true_labels+=[[ids_to_labels[int(l)] for l in label if l!=-100] for label in y]
            true_pred+=[
                [ids_to_labels[int(p)] for (p,l) in zip(prediction,label) if l !=-100]
                for prediction ,label in zip(pred,y)
            ]

    print(classification_report(true_labels,true_pred,mode='strct',scheme=IOB2))
    return classification_report(
      true_labels,
      true_pred,
      mode='strict',
      scheme=IOB2,
      output_dict=True
    )

def train(train_data,valid_data,model,loss_fn,optimizer,lr_scheduler,epoch_num,total_loss):
    total_loss=0
    best_macro_f1=0
    best_micro_f1=0
    for i in range(epoch_num):
        print(f"Epoch {i+1}/{epoch_num}\n----------------------------------")
        total_loss=train_loop(train_data,model,loss_fn,optimizer,lr_scheduler,i+1,total_loss)
        metrics=test_loop(valid_data,model)
        save_weights=False
        valid_macro_f1, valid_micro_f1 = metrics['macro avg']['f1-score'], metrics['micro avg']['f1-score']
        if valid_macro_f1>best_macro_f1:
            best_macro_f1=valid_macro_f1
            print('saving  new weight ...\n')
            torch.save(
                model.state_dict(),
                f'epoch_{i+ 1}_valid_macrof1_{(100 * valid_macro_f1):0.3f}_microf1_{(100 * valid_micro_f1):0.3f}_weights.bin'
            )
            save_weights = True
        if valid_micro_f1>best_micro_f1:
            best_micro_f1=valid_micro_f1
            if not save_weights:
                print('saving new weights...\n')
                torch.save(
                    model.state_dict(),
                    f'epoch_{i + 1}_valid_macrof1_{(100 * valid_macro_f1):0.3f}_microf1_{(100 * valid_micro_f1):0.3f}_weights.bin'
                )
    print('done')