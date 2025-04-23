import torch
import numpy as np

#Tensors created directly from data. The data type is automatically inferred.
data = [[1, 2],[3, 4], [5,100]]
x_data = torch.tensor(data)

#Tensors created from NumPy arrays
np_array = np.array(data)
x_np = torch.from_numpy(np_array)


#The new tensor retains the properties (shape, datatype) of the argument tensor, unless explicitly overridden.
x_ones = torch.ones_like(x_data) # retains the properties of x_data
print(f"Ones Tensor: \n {x_ones} \n")

x_rand = torch.rand_like(x_data, dtype=torch.float) # overrides the datatype of x_data
print(f"Random Tensor: \n {x_rand} \n")