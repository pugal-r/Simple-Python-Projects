
print("="*50)
print("      PYTHON E-COMMERCE SYSTEM")
print("="*50)

# main menu
def menu():

    print("\n------ MAIN MENU ------")
    print("1. View Categories")
    print("2. View Products")
    print("3. Search Product")
    print("4. Admin Panel")
    print("5. Cart")
    print("6. Exit")


  

#categories menu
def view_categories():

    print("\nCategories")
    print("----------------")
    print("1. Electronics")
    print("2. Mens Clothes")
    print("3. Womens Clothes")
    print("4. Footwear")
    print("5. Grocery")
    print("6. Books")

    cat = int(input("\nSelect Category : "))

    products = load_products()

    print("\nProducts")

    for product in products:

        p = product.strip().split(",")

        if cat == 1 and p[2] == "Electronics":
            print(f"ID : {p[0]}")
            print(f"Name : {p[1]}") 
            print(f"Price: ₹{p[3]}")
        elif cat == 2 and p[2] == "Mens Clothes":
            print(f"ID : {p[0]}")
            print(f"Name : {p[1]}") 
            print(f"Price: ₹{p[3]}")

        elif cat == 3 and p[2] == "Womens Clothes":
            print(f"ID : {p[0]}")
            print(f"Name : {p[1]}") 
            print(f"Price: ₹{p[3]}")

        elif cat == 4 and p[2] == "Footwear":
            print(f"ID : {p[0]}")
            print(f"Name : {p[1]}") 
            print(f"Price: ₹{p[3]}")

        elif cat == 5 and p[2] == "Grocery":
            print(f"ID : {p[0]}")
            print(f"Name : {p[1]}") 
            print(f"Price: ₹{p[3]}")

        elif cat == 6 and p[2] == "Books":
            print(f"ID : {p[0]}")
            print(f"Name : {p[1]}") 
            print(f"Price: ₹{p[3]}")

    while True:

                print("\n------ CART MENU ------")
                print("1. Add To Cart")
                print("2. View Cart")
                print("3. Remove Cart Item")
                print("4. Checkout")
                print("5. Back")

                cart_choice = int(input("Enter Choice : "))

                if cart_choice == 1:
                    add_to_cart()

                elif cart_choice == 2:
                    view_cart()

                elif cart_choice == 3:
                    remove_cart()

                elif cart_choice == 4:
                    checkout()

                elif cart_choice == 5:
                    break

                else:
                    print("Invalid Choice")

      

def load_products():

            file = open("products.txt","r")

            data = file.readlines()

            file.close()

            return data
        
def view_products():

            products = load_products()

            print("\nProducts")
            print("-"*70)

            for product in products:

                p = product.strip().split(",")

                print(f"ID : {p[0]}")
                print(f"Name : {p[1]}")
                print(f"Category : {p[2]}")
                print(f"Price : {p[3]}")
                print(f"Stock : {p[4]}")
                print("-"*70)

    
def search_product():

        name=input("Enter Product Name : ").lower()

        products=load_products()

        found=False

        for product in products:

            p=product.strip().split(",")

            if p[1].lower()==name:

                print()

                print("Product Found")

                print("ID :",p[0])
                print("Name :",p[1])
                print("Category :",p[2])
                print("Price :",p[3])
                print("Stock :",p[4])

                found=True

        if not found:
            print("Product Not Found")
        
    
def admin_menu():

        print("\nADMIN PANEL")

        print("1.Add Product")
        print("2.Update Product")
        print("3.Delete Product")
        print("4.Back")

    

def add_product():

        id=input("Enter ID : ")

        name=input("Enter Name : ")

        category=input("Enter Category : ")

        price=input("Enter Price : ")

        quantity=input("Enter Quantity : ")

        file=open("products.txt","a")

        file.write(f"\n{id},{name},{category},{price},{quantity}")

        file.close()

        print("Product Added Successfully")


    
def update_product():

        id=input("Enter Product ID : ")

        products=load_products()

        file=open("products.txt","w")

        for product in products:

            p=product.strip().split(",")

            if p[0]==id:

                price=input("Enter New Price : ")

                quantity=input("Enter New Quantity : ")

                p[3]=price

                p[4]=quantity

            file.write(",".join(p)+"\n")

        file.close()

        print("Updated Successfully")

    
def delete_product():

        id=input("Enter Product ID : ")

        products=load_products()

        file=open("products.txt","w")

        for product in products:

            p=product.strip().split(",")

            if p[0]!=id:

                file.write(",".join(p)+"\n")

        file.close()

        print("Deleted Successfully")



    
def add_to_cart():

        id=input("Enter Product ID : ")

        qty=input("Enter Quantity : ")

        products=load_products()

        for product in products:

            p=product.strip().split(",")

            if p[0]==id:

                file=open("cart.txt","a")

                file.write(f"{p[0]},{p[1]},{qty},{p[3]}\n")

                file.close()

                print("Added To Cart")
    


def view_cart():

        total=0

        file=open("cart.txt","r")

        items=file.readlines()

        file.close()

        for item in items:

            p=item.strip().split(",")

            subtotal=int(p[2])*int(p[3])

            total+=subtotal

            print()

            print("ID : ",p[0])

            print("Product :",p[1])

            print("Quantity :",p[2])

            print("Price :",p[3])

            print("Subtotal :",subtotal)

        print()

        print("Grand Total :",total)
    

def remove_cart():

        id=input("Enter Product ID : ")

        file=open("cart.txt","r")

        items=file.readlines()

        file.close()

        file=open("cart.txt","w")

        for item in items:

            p=item.strip().split(",")

            if p[0]!=id:

                file.write(",".join(p)+"\n")

        file.close()

        print("Item Removed")
    

def checkout():

        view_cart()

        print()

        print("Order Placed Successfully")

        file=open("cart.txt","w")

        file.close()

while True:

    menu()

    try:
        choice = int(input("Enter Choice : "))

        if choice == 1:
            print("choose 1")
            view_categories()

        elif choice == 2:
            view_products()

        elif choice == 3:
            search_product()

        elif choice == 4:

            while True:

                admin_menu()

                ch = int(input("Enter Choice : "))

                if ch == 1:
                    add_product()

                elif ch == 2:
                    update_product()

                elif ch == 3:
                    delete_product()

                elif ch == 4:
                    break

                else:
                    print("Invalid Choice")

        elif choice == 5:

            while True:

                print("\n------ CART MENU ------")
                print("1. Add To Cart")
                print("2. View Cart")
                print("3. Remove Cart Item")
                print("4. Checkout")
                print("5. Back")

                cart_choice = int(input("Enter Choice : "))

                if cart_choice == 1:
                    add_to_cart()

                elif cart_choice == 2:
                    view_cart()

                elif cart_choice == 3:
                    remove_cart()

                elif cart_choice == 4:
                    checkout()

                elif cart_choice == 5:
                    break

                else:
                    print("Invalid Choice")

        elif choice == 6:
            print("Thank You")
            break

        else:
            print("Invalid Choice")

    except ValueError:
        print("Enter Numbers Only")