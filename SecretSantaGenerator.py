# October 10, 2020
# Secret Santa Generator based off of https://www.youtube.com/watch?v=GhnCj7Fvqt0

# September 18, 2021
# Updated Secret Santa Generator for 2021

# import random and person class module
import random
import person_class
import sendEmail
import base64

UNKNOWN = "unknown"
SCRIPT_START = "---start---"
SCRIPT_END = "---end---"

# name list of all participants, minus Linn because she will be hardcoded who she buys for
namelist = []
with open("participant_list.txt", "r") as source:
    for line in source:
        line = line.strip()
        namelist.append(line)

# number list of corresponding to all participants
numbers = list(range(len(namelist)))

# create two list of letters for placeholders
finallist = []
buyinglist = []
for letter in list('abcdefghijklmnop')[:len(numbers)]:
    finallist.append(letter)
    buyinglist.append(letter)

# hard coded emails in for participants to be used in the send emails function
cyn_email = "cynthia_nguyen25@hotmail.com"
bran_email = "brandontat8@gmail.com" # 2021 - changing Brandon's email to another email
mich_email = "michelley123_1@hotmail.com"
dan_email = "daniellen08@gmail.com"
dell_email = "dasayson@hotmail.com"
'''
loann_email = "taoloann@gmail.com"
nic_email = "nicolas_belzile@hotmail.com"
'''
ocs_email = "taooscar08@gmail.com"	# 2021 - changing Oscar's email to another email
linn_email = "linntao72888@gmail.com"
madd_email = "hinata.maddi@gmail.com"   # 2021 - added email for Maddison

# main function to do all the magic
def main():
    
    # TODO FOR 2021
    # [ Y ] TODO add Linn to the namelist
    # [ Y ] TODO remove Linn and Maddison hardcoding
    # [ Y ] TODO record matches last time
    # [ Y ] TODO print last secret santa matches
    # [ Y ] TODO remove special case for Maddison
    # [ Y ] TODO check new matches are different from the previous matches
    # [ Y ] TODO check new matches don't overlap
    # [ Y ] TODO ensure each participant only appears once (one person isn't buying for two or more people)
    # [ Y ] TODO ensure each receiver only appears once (one person isn't receiving from more than one person) [ACTUALLY HAPPENS]
    # [ Y ] TODO ensure each participant is not buying for themselves
    # [ Y ] TODO ensure Linn does not have Maddison

    # TODO FOR 2022
    # [   ] TODO move emails to a config file
    # [   ] TODO set current year to config file
    # [   ] TODO move previous year matches to an archive file
    # [   ] TODO create an encoded output file to allow resending
    # [   ] TODO allow resending using output file
    # [   ] TODO create a list in person_class for all the matches
    # [   ] TODO add match to the person_class so we don't have to manually enter in matches each year

    # TODO ACTUALLY
    # [   ] Make a list of all previous matches

    # 2021 - prints out last years secret santa matches x -> y where x is the buy and y is the receiver
    print('Matches from 2020')
    print('Cynthia -> Danielle')
    print('Danielle -> Linn')
    print ('Linn -> Maddison')
    print('Maddison -> Dell')
    print('Dell -> Brandon')
    print('Brandon -> Nic')
    print('Nic -> Cynthia')
    print('Oscar -> Loann')
    print('Loann -> Michelle')
    print('Michelle -> Oscar')

    print()

    everyoneHasSomeoneNew=False
    everyoneIsBuyingForSomeoneElse=False
    allBuyersAppearOnce=False
    allReceiversAppearOnce=False
    while not everyoneHasSomeoneNew or not everyoneIsBuyingForSomeoneElse or not allReceiversAppearOnce or not allBuyersAppearOnce:
        # randomly shuffle name and number lists
        random.shuffle(namelist)
        random.shuffle(numbers)
        
        # set index to 0
        idx = 0
        
        # creating a new person class with name, email, and unknown buying for until determined
        # hardcoded in who Linn is buying for
        # 2021 - added another variable which is the person the participant bought for last year in the person class
        cynthia = person_class.Person("Cynthia", cyn_email, UNKNOWN, ["Danielle", "Brandon"])
        danielle = person_class.Person("Danielle", dan_email, UNKNOWN, ["Linn", "Dell"])
        dell = person_class.Person("Dell", dell_email, UNKNOWN, ["Brandon", "Cynthia"])
        maddison = person_class.Person("Maddison", madd_email, UNKNOWN, ["Dell", "Michelle"])  # 2021 - changed Maddison email to madd_email since she has an email now
        oscar = person_class.Person("Oscar", ocs_email, UNKNOWN, ["Loann", "Danielle"])
        brandon = person_class.Person("Brandon", bran_email, UNKNOWN, ["Nic", "Maddison"])
        michelle = person_class.Person("Michelle", mich_email, UNKNOWN, ["Oscar", "Loann"])
        #loann = person_class.Person("Loann", loann_email, UNKNOWN, ["Michelle", "Linn"])
        #nic = person_class.Person("Nic", nic_email, UNKNOWN, ["Cynthia", "Oscar"])
        linn = person_class.Person("Linn", linn_email, UNKNOWN, ["Maddison", "Nic"])  # 2021 - NOT hardcording for Linn this year, changing from Maddision to UNKNOWN

        personList = []
        personList.append(cynthia)
        personList.append(danielle)
        personList.append(dell)
        personList.append(maddison)
        personList.append(oscar)
        personList.append(brandon)
        personList.append(michelle)
        #personList.append(loann)
        #personList.append(nic)
        personList.append(linn)

        # for each name in list
        for name in namelist:
        
            # assign a number from the numbers list
            number = numbers[idx]

            # if the number chosen is len -1
            if idx == len(numbers)-1:
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

            # print(x+1, finallist[x], "is buying for" , buyingfor, buyingidx)

            # setting the buying_for variable as it is now determined
            if participant == "Cynthia": cynthia.buying_for = buyingfor
            if participant == "Danielle": danielle.buying_for = buyingfor
            if participant == "Dell": dell.buying_for = buyingfor
            if participant == "Maddison": maddison.buying_for = buyingfor
            if participant == "Oscar": oscar.buying_for = buyingfor
            if participant == "Brandon": brandon.buying_for = buyingfor
            if participant == "Michelle": michelle.buying_for = buyingfor
            #if participant == "Loann": loann.buying_for = buyingfor
            #if participant == "Nic": nic.buying_for = buyingfor
            if participant == "Linn": linn.buying_for = buyingfor   # 2021 - added buying_for variable for Linn

        print()

        everyoneHasSomeoneNew=True
        everyoneIsBuyingForSomeoneElse=True
        allBuyersAppearOnce=True
        allReceiversAppearOnce=True
        buyersFound = {}
        receiversFound = {}
        messageForChecking = 'Matches for Secret Santa 2022' + '\n'
        for person in personList:
            print(person.get_name(), "is buying for", base64.b64encode(str.encode(person.get_buying_for())))
            messageForChecking += person.get_name() + " is buying for " + str(base64.b64encode(str.encode(person.get_buying_for()))) +'\n'
            if person.get_buying_for() in person.get_previous_match_list():
                everyoneHasSomeoneNew=False
                print('!!! Errror: {0} got a previous match: {1}'.format(person.get_name(), person.get_previous_match_list()))
                print()
                break

            if person.get_name() == person.get_buying_for():
                everyoneIsBuyingForSomeoneElse=False
                print('!!! Error: {0} is buying for themselves({1})'.format(person.get_name(), person.get_buying_for()))
                print()
                break

            if person.get_name() in buyersFound:
                allBuyersAppearOnce=False
                print('!!! Error: The buyer {0} appeared more than once. Already Found: [{1}]'.format(person.get_name(), buyersFound.keys()))
                break
            buyersFound[person.get_name()]=True

            if person.get_buying_for() in receiversFound:
                allReceiversAppearOnce=False
                print('!!! Error: The receiver {0} appeared more than once. Already Found: [{1}]'.format(person.get_buying_for(), receiversFound.keys()))
                break
            receiversFound[person.get_buying_for()]=True

        if not set(buyersFound) == set(namelist):
            allBuyersAppearOnce=False
        print('[ OK ] all buyers appear once')
        messageForChecking += '[ OK ] all buyers appear once' + '\n'

        if not set(receiversFound) == set(namelist):
            allReceiversAppearOnce=False
        print('[ OK ] all receivers appear once')
        messageForChecking += '[ OK ] all receivers appear once' + '\n'

    print('--- All Valid ---')

    print(SCRIPT_START)
    message=''
    mailClient=sendEmail.MailClient()
    for buyer in personList:
        message+=mailClient.getMessage(buyer.name, buyer.buying_for)
        #if (buyer==dell or buyer==cynthia):
        mailClient.send(buyer.email, message)
        print('sent to: '+buyer.name)
        message=''
    mailClient.send('ssg.dobby@gmail.com', messageForChecking)
    print('sent debug email to dobby')
    print(SCRIPT_END)

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
