import random #USED FOR RANDOM ATRIBUTE SELECTION


number_of_NPC = int(input("# of NPC's you want to generate: "))


Gender_of_NPC = ["Male","Female"]
Female_name_of_NPC = ["Emily","Sofia","Abby","Jane","Mary","Sarah"]   #ATRIBUTE SECTION
Male_Name_of_NPC = ["John","Mark","Bob","James","Frank","Odin","Cole"]
Social_status_of_NPC = ["Peasent","Poor","Middle Class","Noble",]
Height_of_NPC = [5,5.1,5.2,5.3,5.4,5.5,5.6,5.7,5.8,5.9,6,6.1,6.2,6.3,6.4,6.5,6.6,6.7,6.8,6.9,7,7.1,7.2,7.3,7.4,7.5,7.6,7.7,7.8,7.9,8,8.1,8.2,8.3,8.4,8.5]

for i in range(number_of_NPC):
    if random.choice(Gender_of_NPC) == "Male":          #PRINTS FINAL PRODUCT OF NPCs
        print(random.choice(Male_Name_of_NPC),"\nAge:",random.randint(1,100),"\nSocial Class:",random.choice(Social_status_of_NPC),"\nHeight:",random.choice(Height_of_NPC),"\n")
    else: print(random.choice(Female_name_of_NPC),"\nAge:",random.randint(1,100),"\nSocial Class:",random.choice(Social_status_of_NPC),"\nHeight:",random.choice(Height_of_NPC),"ft\n")