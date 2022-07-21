#implementation of xor through neurons
import numpy as np
def calculate_layer1(x,w1):
    x = X.reshape(1,3) #reshape x
    wt = np.transpose(w1) #find the transpose of w
    layer1 = np.dot(x,wt) # find the net
    layer1[layer1>0] = 1 #use bipolar discrete activation function
    layer1[layer1<=0] = -1
    return layer1


def calculate_layer2(out,w2):
    aug_out = np.append(out,[1]) #append 1 to the output of layer1
    layer2 = calculate_layer1(aug_out,w2)
    return layer2


