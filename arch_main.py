import d_input  as inp
import random

class Tache:
    def __init__(self, pt,num=0):
        self.num = 0
        self.pt = pt
        self.cj = 0




class Cromosome:
  def __init__(self):
    self.tabcj=[]
    self.n_tch = inp.n_tch
    self.lstch =[]
    self.fo=0
  
    
    self.get_new_tache()
   
  def update(self):
    self.tabcj=[]
    self.fo=0
    self.calc_fo()
    
  def get_new_tache (self):
    for ind_tache in range(inp.n_tch):
      pt = inp.list_pt[ind_tache]
      tache = Tache(pt)
      tache.num = ind_tache
      self.lstch.append(tache)
      self.calc_fo() 
  def calc_cj_tach(self):
    s=0
    for tache in self.lstch:
        s=s+tache.pt
        tache.cj=s
        self.tabcj.append(s)

  def calc_fo(self) :
    self.calc_cj_tach() 
    s=0
    for tache in self.lstch:
      s=s+tache.cj
    self.fo=s

class Population_Init:
  def __init__(self):
    self.n_crom=inp.n_crom
    self.tab_crom=[]
    self.get_new_coromosome()
    

  def get_new_coromosome(self):
    crom = Cromosome()
    for ind_crom in range (inp.n_crom):
      random.shuffle(crom.lstch)
      crom.update()
      print('*********')
  
      st="t-num:"
      st1=" cj  :"
      st2=""
      for t in crom.lstch:
        st+=str(t.num) +" | "
        st1+=str(t.cj)+" | "
        st2+=" tnum - "+str(t.num) +" - cj : "+str(t.cj)+" || "
      # print(st)
      # print(st1)
      print(st2)
      
      # print(crom.tabcj)
      print(crom.fo)
      # self.tab_crom.append(crom)
      
      
  

def test():
  # s0 = Cromosome()
  # print(s0.tabcj)
  
  # for tch in s0.lstch:
  #   print(" tache num : ",tch.num," with pt : ",tch.pt,'the cj =',tch.cj)
  # print("fo :",s0.fo)
        
  Population_Init()
# s1.get_new_coromosome()
# print(s1.crom)
test()
