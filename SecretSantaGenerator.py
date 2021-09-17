# October 10, 2020
# Secret Santa Generator based off of https://www.youtube.com/watch?v=GhnCj7Fvqt0

# import random module
import random

finallist = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
buyinglist = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
namelist= ["Cynthia", "Danielle", "Dell", "Maddison", "Oscar", "Brandon", "Michelle", "Loann", "Nik"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(numbers)
random.shuffle(namelist)

# main function
def main():

    # [   ] TODO record matches last time
    # [   ] TODO print last secret santa matches
    # [   ] TODO remove special case for Maddison
    # [   ] TODO check new matches are different from the previous matches
    # [   ] TODO check new matches don't overlap
    #   [ Y ] TODO make sure each buyer appears once
    #   [ Y ] TODO make sure each receiver appears once
    #   [   ] TODO make sure no one has themselves

    buyersAppearOnce=False
    receiversAppearOnce=False
    while not buyersAppearOnce and not receiversAppearOnce:
        print('last time')
        print('---------')

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
        
        buyersAppearOnce=item_appears_once(finallist)
        receiversAppearOnce=item_appears_once(buyinglist)

        buyerList=finallist
        receiverList=[buyerList[receiverIndex-1] for receiverIndex in buyinglist] # note buyerList!
        print("buyers:", buyerList)
        print("receivers:", receiverList)

    print('Matches Valid')

def item_appears_once(inputList):
    testSet=set()
    for item in inputList:
        if item in testSet:
            return False
        testSet.add(item)
    if len(testSet) == len(inputList):
        return True

# function to create the list of names        
def make_list(x, y):
    finallist[y-1] = x

# function to create the list of buying for names
def make_buying_list(x, y):
    buyinglist[x-1] = y

# function to start main
if __name__ == "__main__":
    main()
