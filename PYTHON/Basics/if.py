isEligible= True

if isEligible:
    print("You are eligible to vote")
elif not isEligible:
    print("You are not eligible to vote")

###################################### match  ##################################

day=int(2)

match day:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case _:
        print("default case")

################################### comboine match ##############################

match day:
    case 1|2|3|4|7:
         print("weekdays")
    case _:
         print("other days")