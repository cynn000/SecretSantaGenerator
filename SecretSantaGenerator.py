# October 10, 2020
# Secret Santa Generator based off of https://www.youtube.com/watch?v=GhnCj7Fvqt0

# September 18, 2021
# Updated Secret Santa Generator for 2021

# import random and person class module
import random
import person_class
import sendEmail

UNKNOWN = "unknown"
SCRIPT_START = "---start---"
SCRIPT_END = "---end---"

# create two list of letters for placeholders
# 2021 - added 10th letter for Linn
finallist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
buyinglist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

# name list of all participants, minus Linn because she will be hardcoded who she buys for
namelist= ["Cynthia", "Danielle", "Dell", "Maddison", "Linn", "Oscar", "Brandon", "Michelle", "Loann", "Nic"]   # 2021 - added Linn to the list because she will NOT be hardcoded any more

# number list of corresponding to all participants
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   # 2021 - added 10th participant for Linn

# hard coded emails in for participants to be used in the send emails function
cyn_email = "cynthia_nguyen25@hotmail.com"
bran_email = "brandontat8@gmail.com" # 2021 - changing Brandon's email to another email
mich_email = "michelley123_1@hotmail.com"
dan_email = "daniellen08@gmail.com"
dell_email = "dasayson@hotmail.com"
loann_email = "taoloann@gmail.com"
nic_email = "nicolas_belzile@hotmail.com"
ocs_email = "taooscar08@gmail.com"	# 2021 - changing Oscar's email to another email
linn_email = "linntao72888@gmail.com"
madd_email = "hinata_maddi@gmail.com"   # 2021 - added email for Maddison

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
    # [   ] TODO ensure each participant only appears once (one person isn't buying for two or more people)
    # [   ] TODO ensure each receiver only appears once (one person isn't receiving from more than one person) [ACTUALLY HAPPENS]
    # [ Y ] TODO ensure each participant is not buying for themselves
    # [ Y ] TODO ensure Linn does not have Maddison

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
    while not everyoneHasSomeoneNew or not everyoneIsBuyingForSomeoneElse:
        # randomly shuffle name and number lists
        random.shuffle(namelist)
        random.shuffle(numbers)
        
        # set index to 0
        idx = 0
        
        # creating a new person class with name, email, and unknown buying for until determined
        # hardcoded in who Linn is buying for
        # 2021 - added another variable which is the person the participant bought for last year in the person class
        cynthia = person_class.Person("Cynthia", cyn_email, UNKNOWN, "Danielle")
        danielle = person_class.Person("Danielle", dan_email, UNKNOWN, "Linn")
        dell = person_class.Person("Dell", dell_email, UNKNOWN, "Brandon")
        maddison = person_class.Person("Maddison", madd_email, UNKNOWN, "Dell")  # 2021 - changed Maddison email to madd_email since she has an email now
        oscar = person_class.Person("Oscar", ocs_email, UNKNOWN, "Loann")
        brandon = person_class.Person("Brandon", bran_email, UNKNOWN, "Nic")
        michelle = person_class.Person("Michelle", mich_email, UNKNOWN, "Oscar")
        loann = person_class.Person("Loann", loann_email, UNKNOWN, "Michelle")
        nic = person_class.Person("Nic", nic_email, UNKNOWN, "Cynthia")
        linn = person_class.Person("Linn", linn_email, UNKNOWN, "Maddison")  # 2021 - NOT hardcording for Linn this year, changing from Maddision to UNKNOWN

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

            # if the number chosen is 9
            if idx == 9:
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
        #maddieidx = finallist.index("Maddison")+1	2021 - maddieidx is not used anywhere else. Taking it out

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
            # 2021 - removing this for 2021 since we are not hardcoded who gets Maddison this year
            #if buyingfor == "Maddison":

                # set it so whoever has Maddison will now have Linn
                #buyingfor = "Linn"
                #buyingidx = 10

            print(x+1, finallist[x], "is buying for" , buyingfor, buyingidx)

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
            if participant == "Linn": linn.buying_for = buyingfor   # 2021 - added buying_for variable for Linn

        print()

        everyoneHasSomeoneNew=True
        everyoneIsBuyingForSomeoneElse=True
        for person in personList:
            print(person.get_name(), "is buying for", person.get_buying_for())
            if person.get_buying_for() == person.get_last_year_buying_for():
                everyoneHasSomeoneNew=False
                print('!!! Errror: {0} got the same person this year({1}) as last year({2})'.format(person.get_name(), person.get_buying_for(), person.get_last_year_buying_for()))
                print()
                break

            if person.get_name() == person.get_buying_for():
                everyoneIsBuyingForSomeoneElse=False
                print('!!! Error: {0} is buying for themselves({1})'.format(person.get_name(), person.get_buying_for()))
                print()
                break

    print('--- All Valid ---')

    '''
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
    '''

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
