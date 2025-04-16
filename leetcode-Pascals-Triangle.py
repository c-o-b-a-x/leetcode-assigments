import copy

class Solution(object):
    def generate(self, numRows):
        self.base = [1]
        tri_list= self.base
        temp_list=[]
        self.final = [self.base]
        self.row=numRows
        for i in range(self.row-1):
            temp_list= self.add_zeros(tri_list)
            tri_list=[]
            while temp_list != [0]:
                indx1= temp_list[0]
                indx2=temp_list[1]
                tri_list.append (indx1+indx2)
                temp_list.pop(0)
            self.final.append(tri_list)
        return self.final 
    def add_zeros(self,base):
        temp=copy.deepcopy(base)
        temp.insert(0,0)
        temp.append(0)
        return temp
        
                