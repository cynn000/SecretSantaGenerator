# October 10, 2020
# Secret Santa Generator based off of https://www.youtube.com/watch?v=GhnCj7Fvqt0

# import random and person class module
import random
import person_class
import sendEmail

UNKNOWN = "unknown"
SCRIPT_START = "---start---"
SCRIPT_END = "---end---"

# create two list of letters for placeholders
finallist = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
buyinglist = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

# name list of all participants, minus Linn because she will be hardcoded who she buys for
namelist= ["Cynthia", "Danielle", "Dell", "Maddison", "Oscar", "Brandon", "Michelle", "Loann", "Nic"]

# number list of corresponding to all participants
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# randomly shuffle name and number lists
random.shuffle(namelist)
random.shuffle(numbers)

# hard coded emails in for participants to be used in the send emails function
cyn_email = "cynthia_nguyen25@hotmail.com"
bran_email = "brandontat@hotmail.com"
mich_email = "michelley123_1@hotmail.com"
dan_email = "daniellen08@gmail.com"
dell_email = "dasayson@hotmail.com"
loann_email = "taoloann@gmail.com"
nic_email = "nicolas_belzile@hotmail.com"
ocs_email = "oscarqptao@gmail.com"
linn_email = "linntao72888@gmail.com"

<<<<<<< HEAD
# main function to do all the magic
def main():
    
    # print new line
    # print()
    
    # set index to 0
    idx = 0
    
    # creating a new person class with name, email, and unknown buying for until determined
    # hardcoded in who Linn is buying for
    cynthia = person_class.Person("Cynthia", cyn_email, UNKNOWN)
    danielle = person_class.Person("Danielle", dan_email, UNKNOWN)
    dell = person_class.Person("Dell", dell_email, UNKNOWN)
    maddison = person_class.Person("Maddison", cyn_email, UNKNOWN)
    oscar = person_class.Person("Oscar", ocs_email, UNKNOWN)
    brandon = person_class.Person("Brandon", bran_email, UNKNOWN)
    michelle = person_class.Person("Michelle", mich_email, UNKNOWN)
    loann = person_class.Person("Loann", loann_email, UNKNOWN)
    nic = person_class.Person("Nic", nic_email, UNKNOWN)
    linn = person_class.Person("Linn", linn_email, "Maddison")


    personList = []
    personList.append(cynthia)
    personList.append(danielle)
    personList.append(dell)
    personList.append(maddison)
    personList.append(oscar)
    personList.append(brandon)
    personList.append(michelle)
    personList.append(loann)
    personList.append(nic)
    personList.append(linn)

    # for each name in list
    for name in namelist:
    
        # assign a number from the numbers list
        number = numbers[idx]
        
        # if the number chosen is 8
        if idx == 8:  
            # set number2 (which is the number of the person who we are buying for) to the very first number in the list
            # this means that the very last person will buy for the very first person (watch video for reference)
            number2 = numbers[0]
        else:
            # else then set number2 to the next number in the number list
            number2 = numbers[idx + 1]
            
        # printing for testing    
        # print(name, "You are number:", number, "You are buying for number:", number2)
        
        # create the name list by passing in the name and their own number`
        make_list(name, number)
        
        # create the buying for list with the number and number2 (which is the number of the person they will be buying for)
        make_buying_list(number, number2)
        
        # increase index to move on to the next number in the number list
        idx = idx + 1
    
    # calculate Maddion's number
    maddieidx = finallist.index("Maddison")+1
    
    # printing for testing. Hardcoded Linn to buy for Maddison. 
    # print("Linn You are number: 10 You are buying for number:", maddieidx)
	
    # print new line
    # print()
    
    # loop through the finalist length to list out the names and who they are buying for
    for x in range(len(finallist)):
    
        # set y as the number of who they are buying for minus 1 due to index
        y = buyinglist[x] - 1
        
        # participant name
        participant = finallist[x]
        
        # buying_for name obtained from the final list which is the next person in the list
        buyingfor = finallist[y]
        
        # buying_for person's number
        buyingidx = buyinglist[x]
        
        # if the buying for name is equal to Maddison
        if buyingfor == "Maddison": 
        
            # set it so whoever has Maddison will now have Linn
            buyingfor = "Linn"
            buyingidx = 10
=======
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
>>>>>>> 59776d4136f3c812d1f505b84d8c7a566f807a6b
            
            print(x+1, finallist[x], "is buying for" , buyingfor, buyingidx)
        
<<<<<<< HEAD
        # print(x+1, participant, "is buying for" , buyingfor, buyingidx)
        
        # setting the buying_for variable as it is now determined
        if participant == "Cynthia": cynthia.buying_for = buyingfor
        if participant == "Danielle": danielle.buying_for = buyingfor
        if participant == "Dell": dell.buying_for = buyingfor
        if participant == "Maddison": maddison.buying_for = buyingfor
        if participant == "Oscar": oscar.buying_for = buyingfor
        if participant == "Brandon": brandon.buying_for = buyingfor
        if participant == "Michelle": michelle.buying_for = buyingfor
        if participant == "Loann": loann.buying_for = buyingfor
        if participant == "Nic": nic.buying_for = buyingfor
    
    # hardcoded Linn to buy for Maddison. We baaaaaaad
    # print("10 Linn is buying for Maddison", maddieidx)
    
    print(SCRIPT_START)
    message=''
    mailClient=sendEmail.MailClient()
    for buyer in personList:
    	message=mailClient.getMessage(buyer.name, buyer.buying_for)
    	if (buyer==dell or buyer==danielle or buyer==cynthia):
    		mailClient.send(buyer.email, message)
    	print('sent to: '+buyer.name)
    	message=''
    print(SCRIPT_END)

    # send last email for Linn here
=======
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
>>>>>>> 59776d4136f3c812d1f505b84d8c7a566f807a6b

# function to create the list of names        
def make_list(x, y):
    # numbering is from 1 - 10, y is the number the participant has
    # to add it to the final list we put y - 1 because the index of the list
    # starts from 0 - 9
    finallist[y-1] = x

# function to create the list of buying for names
def make_buying_list(x, y):
    # numbering is from 1 - 10, y is the number the participant has
    # to add it to the final list we put y - 1 because the index of the list
    # starts from 0 - 9
    buyinglist[x-1] = y

# function to start main
if __name__ == "__main__":
    main()
