#implementation of simple neuron using Activation Function 
def artificial_neuron(inputs,weights,bias):
    weighted_sum=0
    
    for i in range(len(inputs)):
        weighted_sum+=inputs[i]*weights[i]
        weighted_sum+=bias
       
    output = 1 if weighted_sum>0 else 0

    return output

inputs = [2,3]
weights=[0.5,0.8]
bias=-1.5

output=artificial_neuron(inputs,weights,bias)
print("neuron output:",output)
