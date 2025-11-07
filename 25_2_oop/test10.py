from typing import Any
from collections import OrderedDict
import random

class Module:
    _parameters:OrderedDict
    
    def __init__(self, input:int, output:int) -> None:
        object.__setattr__(self, "_parameters", OrderedDict())
        self.weight = [random.gauss(0, 1) for _ in range(input)]
        self.bias = [random.gauss(0, 1) for _ in range(output)]
    
    def __setattr__(self, name: str, value: Any) -> None:
        if name in ["weight", "bias"]:
            self._parameters[name] = value
            
        object.__setattr__(self, name, value)
        
    def __getattribute__(self, name: str) -> Any:
        if name in ["weight", "bias"]:
            return self._parameters[name] 

        return self.name
    
    def parameters(self):
        
        
module = Module(3, 1)

for w, b in module.