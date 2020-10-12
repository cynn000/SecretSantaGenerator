# October 10, 2020
# Secret Santa Generator based off of https://www.youtube.com/watch?v=GhnCj7Fvqt0

# import random module
import random

finallist = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
buyinglist = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
namelist= ["Cynthia", "Danielle", "Dell", "Maddison", "Oscar", "Brandon", "Michelle", "Loann", "Nic"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(numbers)
random.shuffle(namelist)

# hard coded emails in for participants to be used in the send emails function
cyn_email = "cynthia_nguyen25@hotmail.com"
bran_email = "brandontat@hotmail.com"
mich_email = "michelley123_1@hotmail.com"
dan_email = "daniellen08@gmail.com"
dell_email = "dasayson@hotmail.com"
loann_email = "taoloann@gmail.com"
nic_email = "nicolas_belzile@hotmail.com"
ocs_email = "oscarqptao@gmail.com"
madd_email = "cynthia_nguyen25@hotmail.com"
linn_email = "linntao72888@gmail.com"

# main function
def main():

    print()
    idx = 0

    for name in namelist:
        number = numbers[idx]
        if idx == 8: 
            number2 = numbers[0]
        else:
            number2 = numbers[idx + 1]
        print(name, "You are number:", number, "You are buying for number:", number2)
        make_list(name, number)
        make_buying_list(number, number2)
        idx = idx + 1
    
    maddieidx = finallist.index("Maddison")+1
    print("Linn You are number: 10 You are buying for number:", maddieidx)
	
    print()

    for x in range(len(finallist)):
        y = buyinglist[x] - 1
        buyingfor = finallist[y]
        buyingidx = buyinglist[x]
        if buyingfor == "Maddison": 
            buyingfor = "Linn"
            buyingidx = 10
            
        # send emails here
        
        print(x+1, finallist[x], "is buying for" , buyingfor, buyingidx)
    
    print("10 Linn is buying for Maddison", maddieidx)
    
    # send lastt email for mom here

# function to create the list of names        
def make_list(x, y):
    finallist[y-1] = x

# function to create the list of buying for names
def make_buying_list(x, y):
    buyinglist[x-1] = y

# function to start main
if __name__ == "__main__":
    main()
