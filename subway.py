"""An App that specializes selling subway products"""
import random
Questions={"sandwich":"Do you like to have sandwiches? ",
            "salad"  :"Do you like to have salads? ",
            "drinks" :"Do you like to have drinks? ",
            "cookies":"Do you like to have cookies?  "
          }
          
Menu     = {"sandwich":["spicy italian","classic tuna","veggie delite","cold combo"],
           "salad":["chicken sald","roasted beef","sweet onion","carved turkey"],
           "drinks":["coffee","milk","apple","orange"],
           "cookies":["donuts","chocolate cookie","bagel","carmel cookie"]
          }
          
chc ={} 
customers={}
stock={}

for s in Menu:
    for ing in Menu[s]:
        stock[ing] = random.randint(1, 4)
  
adjectives = ["yummy", "juicy", "greasy", "delicious"]
nouns = ["jack", "dream", "dip", "down",]

def cust_choice():
    for i in Questions.keys():
        res=input(Questions[i]+"")
        chc[i]=res.lower()in ('y','yes')
    return chc
    
def construct_sub(chc):
    sub=[]
    for j in chc.keys():
        if chc[j]==True:
            sub.append(random.choice(Menu[j]))
    return sub

def serve(name):
    while True:
        if customers[name]["count"] >4:
            print("please wait product needs refill")
            break
        if len(customers[name]["sub_ingrediants"]) >= 1:
            customers[name]["count"] += 1
            print ('\nHere you have', customers[name]["product"])
            for i in customers[name]["sub_ingrediants"]:
                print(i)
        if len(customers[name]["sub_ingrediants"]) ==0:
            print("thank you")
            
        if customers[name]["count"] in range(2,5):
            print ("\n you have got 10% off ")
            
        while True:
            another = input('Would you like try again? type / for no ')
            if another.lower():
                break
        if another.lower()=="/":
            print ("\nThank you!")
            break
    return
    
if __name__=='__main__':
    while True:
        name=input("Customer name ")
        if name not in customers:
            print ("\nHello "+name+"..let's find a sub for you")
            customers[name]={}
            customers[name]["count"]=0
            customers[name]["product"]=random.choice(adjectives)+" "+random.choice(nouns)
            customers[name]["sub_ingrediants"]= construct_sub(cust_choice())
        serve(name)
        
        while True:
            another = input('is there another customer? ')
            if another.lower():
                break
        if another.lower()=="/":
            print ("\nThank you!")
            break
            
    
    
    