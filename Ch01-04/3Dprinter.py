#Practice for initial parameter

def threePrint(nozzleTemp,bedTemp,raft = True):
    print("Heat nozzle to {temp}".format(temp=nozzleTemp))
    print("Heat bed to {temp}".format(temp=bedTemp))
    if raft is True:print("Make raft...")
    print("Printing...")

threePrint(210,50,False)
