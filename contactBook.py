contacts={}
while True:
    print("\n1.ADD CONTACT\n2.VIEW CONTACT LIST\n3.SEARCH CONTACT\n4.UPDATE CONTACT\n5.DELETE CONTACT\n")
    ch=input("Enter your choice:")
    if ch=="1":
        name=input("Enter the name:")
        ph_no=input("Enter the phone number:")
        email=input("Enter the email:")
        address=input("Enter the address:")
        contacts[name]={"phone_number":ph_no,"email":email,"address":address}
        print("Contacts added successfully.....")

    elif ch=="2":
            if not  contacts:
                print("invalid contact")
            else:
                print("contact list")
                for name,info in contacts.items():
                    print("name:", name,"phone_number:",info['phone_number'])
    elif ch=="3":
            search=input("Enter a name or phone number to search:")
            found=False
            for name,info in contacts.items():
                if search in name or search==info['phone_number']:
                    print("name:",name,"\nphone_number:",info['phone_number'],"\nemail:",info['email'],"\naddress:",info['address'])
                    found =True
            if not found:
                print("contact not found")
    elif ch=="4":
            name=input("Enter the name of the contact to update:")
            if name in contacts:
                ph_no=input("Enter the new phone number:")
                email=input("Enter the new email:")
                address=input("Enter the new address:")
                contacts[name]["phone_number"]=ph_no
                contacts[name]["email"]=email 
                contacts[name]["address"]=address
                print("contacts updated successfully")
            else:
                print("contacts not found")
    elif ch=="5":
            name=input("Enter the name of the contact to delete:")
            if name in contacts:
                del contacts[name]
                print("contact deleted successfully")
            else:
                print("contact not found")
    elif ch=="6":
            break
    else:
            print("invalid choice.Please choose a valid choice.")
            
        
