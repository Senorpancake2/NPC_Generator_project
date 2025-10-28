import random #USED FOR RANDOM ATRIBUTE SELECTION


number_of_NPC = int(input("# of NPC's you want to generate: "))


Gender_of_NPC = ["Male","Female"]
Female_name_of_NPC = ["Emily","Sofia","Abby","Jane","Mary","Sarah"]   #ATRIBUTE SECTION
Male_Name_of_NPC = ["John","Mark","Bob","James","Frank","Odin","Cole"]
Social_status_of_NPC = ["Peasent","Poor","Middle Class","Noble",]


for i in range(number_of_NPC):
    if random.choice(Gender_of_NPC) == "Male":          #PRINTS FINAL PRODUCT OF NPCs
        print(random.choice(Male_Name_of_NPC),"\nAge:",random.randint(1,100),"\n")
    else: print(random.choice(Female_name_of_NPC),"\nAge:",random.randint(1,100),"\n")