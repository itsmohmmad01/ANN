#implementation of AND Operator neuron using Activation Function
def artificial_neuron(inputs,weights,bias):
    weighted_sum=0
    
    for i in range(len(inputs)):
        weighted_sum+=inputs[i]*weights[i]
    weighted_sum+=bias
       
    output = 1 if weighted_sum>0 else 0

    return output

inputs = [1,1]
weights=[1,1]
bias=-1.5

output=artificial_neuron(inputs,weights,bias)
print("neuron output:",output)
