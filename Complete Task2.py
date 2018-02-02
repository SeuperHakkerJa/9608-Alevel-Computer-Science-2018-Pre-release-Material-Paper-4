
        class Toy:

          def __init__(self,name,ID,price,age):
            if age > 18:
              print("the age has to be under 18")
              return 

            self.__ToyName = name  
            self.__ToyID = ID
            self.__Price = price
            self.__MinimumAge = int(age)
            self.__all_info = [name,ID,price,age]

          def SetToyName(self,p):
            self.__ToyName = p
          def SetToyID(self,d):
            self.__ToyID = d 
          def SetPrice(self,i):
            self.__Price = i
          def SetMinimumAge(self,i):
            self.__MinimumAge = int(i) 
          def GetToyName(self):
            return (self.__ToyName)
          def GetToyID(self):
            return (self.__ToyID)
          def GetPrice(self):
            return (self.__Price)
          def GetMinimumAge(self):
            return (self.__MinimumAge)

          def getAll(self):
            return self.__all_info

        class ComputerGame(Toy):
          def __init__(self,name,ID,price,age,catogory,console):
            Toy.__init__(self,name,ID,price,age)
            self.__Catogory = catogory
            self.__Console = console
            self.__all_info = [name,ID,price,age,catogory,console]

          def SetCatogory(self,c):
            self.__Catogory = c
          def SetConsole(self,c):
            self.__Console = c
          def GetCatogory(self):
            return (self.__Catogory)
          def GetConsole(self):
            return (self.__Console)

          def getAll(self):
            return (self.__all_info)

        class Vehicle(Toy):

          def __init__(self,name,ID,price,age,Type,Height,Length,Weight):
            Toy.__init__(self,name,ID,price,age)
            self.__Type = Type
            self.__Height = int(Height)
            self.__Length = int(Length) 
            self.__Weight = int(Weight) 
            self.__all_info = [name,ID,price,age,Type,Height,Length,Weight]

          def SetType(self,p):
            self.__Type = p
          def SetHeight(self,d):
            self.__Height = d 
          def SetLength(self,i):
            self.__Length = i
          def SetWeight(self,i):
            self.__Weight = i 
          def GetType(self):
            return (self.__Type)
          def GetHeight(self):
            return (self.__Height)
          def GetLength(self):
            return (self.__Length)
          def GetWeight(self):
            return (self.__Weight)

          def getAll(self):
            return (self.__all_info)

        def find_data(Data):
          print("enter the id of the toy")
          ToyID = input()
          for i in range(len(Data)):
            if Data[i][1] == ToyID:
              a,b,c,d = Data[i][0],Data[i][1],Data[i][2],Data[i][3]
              print("ToyID {1} has following property:\nName: {0}\nPrice: {2}\nAge: {3}".format(a,b,c,d))

        def discount(Data):
          print("please input the discount number: ")
          d_rate = int(input())
          if d_rate == "":
            print("no discount")
          else:
            if 1 <= d_rate <=99:
              for i in range(len(Data)):
                Data[i][2] *= (100-d_rate)/100
            else: print("wrong discount number")

        def sorting(Data):
          for i in range(len(Data)):
            for j in range(len(Data)-1):
              if Data[j][2] > Data[i][2]:
                Data[j],Data[i] = Data[i],Data[j]




        def main():
          nG1 = ComputerGame("A","A1",20,5,"AAA","whatever")
          nG2 = ComputerGame("B","B2",35.2,16,"BBB","whatever")
          nG3 = ComputerGame("C","C3",2.43,2,"CCC","whatever")
          nG4 = ComputerGame("D","D4",1000,2,"DDD","whatever")
          nG5 = ComputerGame("E","E5",333,3,"EEE","whatever")
          nG6 = ComputerGame("F","F6",0,17,"FFF","whatever")

          AllGame = []
          AllGame.append(nG1.getAll())
          AllGame.append(nG2.getAll())
          AllGame.append(nG3.getAll())
          AllGame.append(nG4.getAll())
          AllGame.append(nG5.getAll())
          AllGame.append(nG6.getAll())

          nV = Vehicle("car","kkk444",20,5,"toycar",10,2,3)

          nT1 = Toy("A","A1",100,14)
          nT2 = Toy("B","B2",243,2)
          nT3 = Toy("C","C3",23,2)
          nT4 = Toy("D","D4",232.2,2)
          nT5 = Toy("E","E5",99.8,2)
          nT6 = Toy("F","F6",1001,2)
          nT7 = Toy("G","G7",35,2)
          nT8 = Toy("H","H8",2,2)


          AllToy = []
          AllToy.append(nT1.getAll())
          AllToy.append(nT2.getAll())
          AllToy.append(nT3.getAll())
          AllToy.append(nT4.getAll())
          AllToy.append(nT5.getAll())
          AllToy.append(nT6.getAll())
          AllToy.append(nT7.getAll())
          AllToy.append(nT8.getAll())
          discount(AllToy)
          find_data(AllToy)
          sorting(AllGame)
          print(AllGame)

        main()
































