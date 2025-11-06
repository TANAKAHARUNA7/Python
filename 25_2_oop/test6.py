

class MyDataset:
    def __init__(self, feature:list, label:list)->None:
        self.feature:list = feature
        self.label:list = label

    # def __str__(self):
    #     return f"Dataset: \nfeature: {self.feature}\
    #         \nlabel: {self.label}"
            
    def __getitem__(self, index)->tuple:
        return self.feature[index], self.label[index]
            
    def __setitem__(self, index:int, value:tuple[list,list])->None:        
        self.feature[index] = value[0]
        self.label[index] = value[1]
        
    def __len__(self):
        return len(self.feature)
    
        
    # __repr__ → 開発者がデバッグ（動作確認）するときに見るための“正式な表示方法”
    def __repr__(self):
        return "For log, debug and Doc"
            
dataset = MyDataset([1, 2, 3,], [10, 20, 30])

print(dataset) # get -> 0番目sampleの値(feature, labels)

# dataset[2] = ([5], [50])

# print(dataset[2]) # get -> 0番目sampleの値(feature, labels)
