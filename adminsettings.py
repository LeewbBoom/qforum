class User:
  menber= {}
  name= []
  def __init__(self,name,password):
    self.name= name
    self.password= password
    
    pass
  def check(self):
    if self.name!="" and len(list(str(self.password)))>= 8 and not " " in list(self.password) and not ":" in list(self.name) and not ":" in list(self.password): 
      return True
    else :
      return False
  def if_in(self):
    if self.name in User.name:
      return True
    else:
      return False
      
  def rgst(self):
    User.menber[self.name]= self.password

  def true_pw(self):
    if self.password== User.menber[self.name]:
      return True
    else:
      return False

  @staticmethod
  def save():
    with open("./log/admins.txt","w") as f:
      txt= ""
      for n in User.menber:
        txt+="%s:%s\n"%(n,User.menber[n])
      f.write(txt)

  @staticmethod
  def init():
    with open("./log/admins.txt","r") as f:
      txt=f.read()
      adms= txt.splitlines()
      nbase= []
      mbase= {}
      for adm in adms:
        nm,pw= adm.split(":")
        nbase.append(nm)
        mbase[nm]= pw
      User.name= nbase
      User.menber= mbase
      print(txt)
      print(adms)
      print("[ O ]menber:",User.menber)
      print("[ O ]name:",User.name)