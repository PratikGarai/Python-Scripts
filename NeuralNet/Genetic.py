import warnings
import random
class Population:

    def __init__(self):
        self.struct = []   #storage of error and weights
        self.target = None #the y value
        self.inputs = None #tuple of inputs
        self.set = False
        self.length = None #length of weights
        self.min_error = []
        self.generation = 0

    def set_params(self,target,inputs):
        self.target = target
        self.inputs = inputs
        self.length = len(inputs)
        self.set = True
    
    def add(self,weights):
        assert self.set==True, 'Parameters not set yet'
        assert len(weights)==self.length, 'Length of input doesn\'t match the weights'

        s = (self.calc(weights),weights)
        if(s in self.struct):
            # warnings.warn('Ignoring weight, already present')
            return

        self.struct.append(s)
        self.struct = sorted(self.struct,reverse = True)

    def calc(self,weights):
        return 1/abs(sum([weights[i]*self.inputs[i] for i in range(self.length)])-self.target)

    def generate(self , n_parents = 3, n_children = 6, mutate = False):
        assert n_parents <= self.length, 'n_parents cannot be more than the population'
        assert n_children <= self.length, 'n_children cannot be more than the population'
        # another assert for max

        parents = self.struct[:n_parents]
        for i in range(n_parents-1):
            for j in range(i+1,n_parents):
                child  = parents[i][1][:int(self.length/2)]+parents[j][1][int(self.length/2):]
                if(mutate==True):
                    child[int(random.random()*self.length)] /= int(random.random()*3)+1
                self.add(child)

        self.struct = self.struct[:n_children]
        self.generation += 1

    def get_best(self):
        return self.struct[0]

    def print_struct(self):
        print()
        for i in self.struct:
            print(i)
        print()

def main():
    p = Population()
    p.set_params(44.1,[4,-2,7,5,11,1])
    p.add([2.4,0.7,8,-2,5,1.1])
    p.add([-0.4,2.7,5,-1,7,0.1])
    p.add([-1,2,2,-3,2,0.9])
    p.add([4,7,12,6.1,1.4,-4])
    p.add([3.1,4,0,2.4,4.8,0])
    p.add([-2,3,-7,6,3,3])
    
    p.print_struct()

    error = p.get_best()
    for i in range(10):
        p.generate(mutate=True)
        print(p.get_best())
        # p.print_struct()
    # while(True):
    #     p.generate(mutate = True)
    #     new_error = p.get_best()[0]
    #     print('Generation',p.generation,':',new_error)
        # p.print_struct()
        # if(error==new_error):
        #     print('Convergence')
        #     break
        # if(new_error<0.5):
        #     print('Found')
        #     break
        # error = new_error
main()
