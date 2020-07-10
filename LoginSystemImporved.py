f = open("Dtabase.txt", "x")
'''
have username and pass stored in a txt file and recall that 
'''



username = ["Joe"];
password = ["Kris"];
inuser = ("");
inpass = ("");
iuser = 0;
ipass = 0;

have_account = input("Do you have an account registered? ");
#have_account = have_account.lower;

if(have_account == "yes"):
    inuser = input("What is your username? ");
    #username.append(inuser);
    inpass = input("What is your password? ");
    #password.append(inpass);

elif(have_account == "no"):
   insuer = input("What would you like to make your username? ")
   inpass = input("What would you like to make your password? ")
   username.append(inuser);
   print("Account Created");
   #password.append(inpass);
else:
    print("Error");
#checks username and password

if(inuser in username and inpass in password):
    iuser = username.index(inuser);
    ipass = password.index(inpass);
    if (iuser == ipass):

        print("Congrats you loged in!")

else:
    print("Process Failed");
'''
you need to create code that searches the username and password lists to 

have account- if it exists, if the username and password are in the same index

new account- find index of username and password then check if they match 
'''