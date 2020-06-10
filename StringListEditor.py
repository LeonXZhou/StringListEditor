def StringEditor(OriginalList,AddList,DeleteList):
    #The string list editor function implemented using hash tables (Dictionaries in pythn)
    OriginalListDict = {}

    #Constructs a hashmap of the Original string list
    for S in OriginalList:
        OriginalListDict[S] = len(S)

    # checks for uniqueness of the addlist element and inserts into OriginalList dictionary (Original string list remains unchanged)
    for i in range(len(AddList)):
        if not OriginalListDict.get(AddList[i]):
            OriginalListDict[AddList[i]] = 'exists'
    # checks for existences of deletelist element in originallist dictionary and removes it
    for i in range(len(DeleteList)):
        if OriginalListDict.get(DeleteList[i]):
            del OriginalListDict[DeleteList[i]]

    UnsortedOutputList = list(OriginalListDict.keys()) #convert keys to a list

    OutputList = sorted(UnsortedOutputList,reverse = True) #sorts list by reverse alphabetical first (tie breakers first since python sort is a stable sort)
    OutputList = sorted(OutputList, key = len,reverse = True) # sort by lenght next
    print(OutputList)

OL = ['one', 'two', 'three','four']
AL = ['one', 'two', 'five', 'six','a','b','c', 'six']
DL = ['two', 'five']
StringEditor(OL,AL,DL)
