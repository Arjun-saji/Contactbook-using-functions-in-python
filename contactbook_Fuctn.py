contatbook = {"abc":789156,"brdh":412356,"sdef":896354}
def Addcontact(name,Phonenumber):
	if name in contatbook:
		print('Name already Exists')
	else:
		contatbook[name]=Phonenumber
		print("Contact Added")
def UpdateContact(xname,uname,unum):
    if xname in contatbook:
    	contatbook.update({uname:unum})
    	print("Contact updated succesfully..!")
    else:
    	print("Contact not found..!")
def DeleteContact(dname):
    if dname in contatbook:
   	   contatbook.pop(dname)
   	   print("Deleted contact succesfully..!")
    else:
   		print("Contact doesn't Exists")

while True:
	 print("1.Add contact\n2.Update contact\n3.Delete contact\n4.Display")
	 choice =int(input("Enter your Choice"))
	 if choice==1:
		 name = input('Enter the Name:')
		 Phonenumber=int(input('Enter the Phone number: '))
		 Addcontact(name,Phonenumber)
	 elif choice==2:
		 xname= input("Enter the contact to be updated :")
		 uname=input('Enter the name to updated:')
		 unum= int(input("Enter the new number: "))
		 UpdateContact(xname,uname,unum)
	 elif choice==3:
    	  dname=input("enter the contact to Delete")
    	  DeleteContact(dname)
     elif choice==4 :
     	  for i,j in contatbook.items():
    	         print(i,":",j)
     else:
    	exit()    
     



