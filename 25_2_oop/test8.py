

from pyexpat import features

from scipy import datasets


class MyDataset:
    def __init__(self, feature:list, label:list)->None:
        self.feature:list = feature
        self.label:list = label
        
    def __iter__(self):
        for x, y in zip(self.feature, self.label):
            yield x, y
dataset = MyDataset([1, 2, 3], [10, 20, 30])

for x, y in dataset: # dataset.__iter()__ -> iterator.__next__()
    print(f"x, y: {x}, {y}")