def kodaikkanal():
    print("******welcom to kodaillanal tour******")
    print("option > 1.BOOMBARAI VILLAGE")
    print("option > 2.PILLAR ROCKS")
    print("option > 3.PINE FOREST")
    place=int(input("choose your no to place:"))
    if place==1:
        print("boombarai village 2 days package to 2000rs")
    elif place==2:
        print("pillar rocks 2 days package is 2500rs")
    elif place==3:
        print("pine forest 2 days package is 3000rs")        
    else:
        print("3 packages only")
        var=input("do you watnt to continue yes:")
        if var=="yes":
            main_function()
        else:
            print("thanks for visite")    
  
  
def arcadu():
    print("******welcom to arcadu tour******")
    print("option > 1.BIG LAKE")
    print("option > 2.PEEKU PARK")
    print("option > 3.KILIYUR FALS")
    place=int(input("choose your no to place:"))
    if place==1:
        print("big lake 2 days package to 2000rs")
    elif place==2:
        print("peeku park 2 days package is 2500rs")
    elif place==3:
        print("kiliyur fals 2 days package is 3000rs")        
    else:
        print("3 packages only")
        var=input("do you watnt to continue yes:")
        if var=="yes":
            main_function()
        else:
            print("thanks for visite")    
        
def ooty():
    print("******welcom to ooty tour******")
    print("option > 1.OOTY LAKE")
    print("option > 2.PYKARA FALLS")
    print("option > 3.GOVERNMENR ROSE GARDEN")
    place=int(input("choose your no to place:"))
    if place==1:
        print("ooty lake 2 days package to 2000rs")
    elif place==2:
        print("pykara falls 2 days package is 2500rs")
    elif place==3:
        print("government rose garden 2 days package is 3000rs")        
    else:
        print("3 packages only")
        var=input("do you watnt to continue yes:")
        if var=="yes":
            main_function()
        else:
            print("thanks for visite")
            
def main_function():
    print("****welcome to tour plaze")
    print("#####1.kodaikkanal ####")
    print("#####2.arcadu ####")
    print("#####3.ooty ####")  
    place=int(input("pla enter your tour place enter the number:"))
    if place==1:
        kodaikkanal()
    elif place==2:
        arcadu()
    elif place==3:
        ooty()
    else:
        print("3 pakages only")
main_function()                                     
                