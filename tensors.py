import torch 
import numpy as np

#=========================================================#
# Basically following the 1 hour blitz tutorial on the 
# pytorch website. 
# link : 
# https://pytorch.org/tutorials/beginner/blitz/tensor_tutorial.html#sphx-glr-beginner-blitz-tensor-tutorial-py
#=========================================================#

#=========================================================#
# Basically is tensor is kind of a matrix or you can say 
# that it is a vector.
#=========================================================#

#=========================================================#
# Making an uninitialised tensor.
#=========================================================#
x = torch.empty(5, 3)
print(x)
#=========================================================#

#=========================================================#
# Random number
# basically i don't understand difference between 
# torch.rand and torch.empty
#=========================================================#
x = torch.rand(5, 3)
print(x)
#=========================================================#

#=========================================================#
# torch.zeros gives you a tensor made up of zeros
#=========================================================#
x = torch.zeros(5, 3, dtype=torch.long)
print(x)
#=========================================================#

#=========================================================#
# Directly use tensor method to set the values
#=========================================================#
x = torch.tensor([[5.5, 3], [5, 3]])
print(x)
#=========================================================#

#=========================================================#
# Change the existing tnsor
#=========================================================#
x = x.new_ones(5, 3, dtype=torch.double)
print(x)
#=========================================================#

#=========================================================#
# Change the data type of the existing data type
#=========================================================#
x = torch.rand_like(x, dtype=torch.float)
print(x)
#=========================================================#


#=========================================================#
# Knowing the size of the tensor.
#=========================================================#
print(x.size())
#=========================================================#

#=========================================================#
# Operations on tensors!!
# Note : follow the general rules of matrix operations. 
#=========================================================#
y = torch.rand(5, 3)
print(x + y)
#=========================================================#

#=========================================================#
# Storing the result in a variable. 
#=========================================================#
result = torch.empty(5, 3)
torch.add(x, y, out=result)
print(result)
#=========================================================#

#=========================================================#
# Simply update a y
#=========================================================#
y.add(x)
print(y)
#=========================================================#

#=========================================================#
# Numpy like bells and whistles. 
#=========================================================#
print(y[1:3])
#=========================================================#

#=========================================================#
# Converting numpy array to torch tensor.
#=========================================================#
a = np.ones(5)
b = torch.from_numpy(a)
print(a)
print(b)
#=========================================================#