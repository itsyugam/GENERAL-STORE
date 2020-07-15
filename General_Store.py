import pickle
import json

class product:
   
   def add_pr(self):
      ch="y"
      while ch=="y" or ch=="Y":
         try:
            prname=input("Enter the product name:")
            prqty=int(input("Enter quantity of product(gm/ml):"))
            prprice=int(input("Enter price of product(Rs):"))
            prdis=int(input("Discount on this product(%):"))
            stock=int(input("Enter the stock:"))
            key=prname
            value=[prqty,prprice,prdis,stock]
            p = {key:value}
         except:
            p=''
            print("\nwrong input")
         
         
         
         
         f=open("data.txt","rb")
         file=f.read()
         f.close()
         
        
         
         if len(file)!=0 and len(p)!=0:
            f=open("data.txt","rb")   
            p.update(pickle.load(f))
            f.close()
            
          
         if len(p)!=0:
         
            f=open("data.txt","wb")
            pickle.dump(p,f)
            
            f.close()
            print("\nProduct added successfully!\n")
         ch=input("\nDo you want to add more product(y/n):")
        
   def show_pr(self):
      print("Name        Qty(gm/ml)     price(Rs)     Discount(%)   stock\n")
      print("*"*60)
      try:
         f=open("data.txt","rb")
         list=pickle.load(f)
         for k,v in list.items():
            print(k,end="  ")
            n=10-len(k)
            print(" "*n,end="") 
            for i in range(4):
               print(v[i],end="            ")  
            print("\n")
         f.close()
      except:
         print("stock is empty!")
         
   def show_spr(self):
      prname=input("Enter product name:")
      try:
         f=open("data.txt","rb")
         list=pickle.load(f)
         print(f"\nproduct name:{prname}\nQty:{list[prname][0]}(gm/ml)\nPrice:{list[prname][1]}Rs\nDiscount:{list[prname][2]}%\nstock:{list[prname][3]}")
         f.close() 
      except:
         print("No such product exist!")
   
   def modify_pr(self):
      self.show_pr()
      ch="y"
      while ch=="y" or ch=="Y":
         pr=input("\nEnter product name:")
         try:
            f=open("data.txt","rb")
            list=pickle.load(f)
         except:
            list=[]
         
         if pr in list:
            print(f"\nproduct name:{pr}\nQty:{list[pr][0]}(gm/ml)\nprice:{list[pr][1]}Rs\nDiscount:{list[pr][2]}%\nstock:{list[pr][3]}")
            try:
               mod=int(input("\nWhat you want to modify:\n1.Quantity\n2.Price\n3.Discount\n4.Stock\n"))
               if mod==1:
                  nqty=int(input("\nEnter new quantity:"))
                  list[pr][0]=nqty
               elif mod==2:
                  npr=int(input("\nEnter new price:"))
                  list[pr][1]=npr
               elif mod==3:
                  ndis=int(input("\nEnter new discount"))
                  list[pr][2]=ndis
               elif mod==4:
                  nst=int(input("\nEnter new stock:"))
                  list[pr][3] = list[pr][3] + nst
               else:
                  print("\nWrong input!")
                  
               f=open("data.txt","wb")
               pickle.dump(list,f)
               f.close()
               print("\nSuccessfully modified!")
                  
               
            except:
               print("\nWrong input!")   
               
            
         else:
            print("\nNo such item is in the store!")
            
         ch=input("\nWant to modify more product(y/n):")
           
   def delete_pr(self):
      self.show_pr()
      c="y"
      while c=="y" or c=="Y":
         pr=input("\nEnter the product name:")
         try:
            f=open("data.txt","rb")
            list=pickle.load(f)
         except:
            list=[]
         
         if pr in list:
            del list[pr]
            f=open("data.txt","wb")
            pickle.dump(list,f)
            f.close()
            print("\nProduct removed successfully")
         else:
            print("\nproduct is not in the list!")
         
         c=input("\nWant to delete more(y/n):")
   
         
      
   def billing(self):
      self.show_pr()
      buy={}
      name=input("\nEnter customer name:")
      address=input("\nEnter address:")
      
      ch="y"
      while ch=="y" or ch=="Y":
         try:
            f=open("data.txt","rb")
            list=pickle.load(f)
         except:
            list=[]
         pr=input("\nEnter product name:")
         qty=int(input("\nEnter the number of pack:"))
         if pr in list and list[pr][3]>=qty:
            tp=list[pr][1]*qty
            dis=tp*(list[pr][2]/100)*qty
            fp=tp-dis
            buy[pr]=[list[pr][0],qty,list[pr][1],tp,list[pr][2],fp,dis]
            list[pr][3]=list[pr][3]-qty
         else:
            print("\nInput wrong item or enough item is not in stock")
         ch=input("\nDo you want to add more(y/n):")
         try:
            f=open("data.txt","wb")
            pickle.dump(list,f)
            f.close()
         except:
            pass
         
      print(f"\n\nCustomer Detail:-\nName:{name}\nAddress:{address}\n\n")
         
      amm=0
      disc=0
      total=0
      print("*"*25,"invoice","*"*25)
      print("\nName    weight     Qty     MRP      Total   Dis(%)   ammount\n")
      for k,v in buy.items():
         print("\n")
         print(k,end="")
         print(" "*(10-len(k)),end="")
         for i in range(6):
            print(v[i],end="       ")
            
         amm=amm+(v[2]*qty)
         disc=disc+v[6]
         total=total+v[5]
      print("\n")
      print("*"*60)
        
      print(f"\n\nTotal MRP Price={amm}\nTotal discount={disc}\nTotal Amount:{total}")
         
      
      
   def complaint(self):
      name=input("Enter your name:")
      complaint=input("Tell your problem:")
      p={name:complaint}
      
      f=open("complaint.txt","rb")
      file=f.read()
      f.close()
      
      if len(file)!=0:
         f=open("complaint.txt","rb")
         p.update(pickle.load(f))
      
      f=open("complaint.txt","wb")  
      pickle.dump(p,f)
      
      f.close()
      print("\nComplaint successfully registered. Thanks for feedback!")
      
   def compbox(self):
      f=open("complaint.txt","rb")
      file=f.read()
      f.close()
      
      
      if len(file)!=0:
         f=open("complaint.txt","rb")
         list=pickle.load(f)
         print("\nName           Complaints")
         print("*"*60)
         
         for k,v in list.items():
            print(k,end="")
            print(" "*(15-len(k)),end="")
            print(v)
      else:
         print("\nComplaint box is empty!")
      
   def admin(self):
      choice=int(input("\nwhat you want to do:\n1.Add product\n2.Display product list\n3.show specific product\n4.Modify product\n5.Delete product\n6.Show customer complaints\n\n"))
      if choice==1:
         self.add_pr()
      elif choice==2:
         self.show_pr()
      elif choice==3:
         self.show_spr()
      elif choice==4:
         self.modify_pr()
      elif choice==5:
         self.delete_pr()
      elif choice==6:
         self.compbox()
      else:
         print("Enter wrong choice!")
         
         
   def customer(self):
      choice=int(input("\nwhat you want to do:\n1.Billing\n2.Complaint\n\n"))
      if choice==1:
         self.billing()
      elif user==2:
         pr.complaint()
      else:
         print("Enter wrong input!")                          
            
pr=product()
while True:
   print("\n___________________Welcome to yugam store___________________\n\n1.Admin\n2.Customer\n3.Exit\n")
   try:
      user=int(input())
   except:
      print("wrong input!")
   if user==1:
      pr.admin()
   elif user==2:
      pr.customer()
   elif user==3:
      exit()
   else:
      print("\nEnter wrong input!")
