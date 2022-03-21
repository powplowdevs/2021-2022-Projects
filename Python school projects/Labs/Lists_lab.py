#task 1
names = ["jessie","nick","jack","dani","kyle"]

#task 2
guest_list = ["joe","john","jack"]
print("\n".join(str(person + " Is invited to the party") for i, person in enumerate(guest_list)))
#useing f str and indexing
print(f"On no {guest_list[2]} cant make it")
#use of list edting
guest_list.remove(guest_list[2])
new_person = input("Invited somebody new: ")
guest_list.append(new_person)
print(f"{guest_list[len(guest_list)-1]} Is invited to the party")
#ading +1s
plus_1 = []
for index, person in enumerate(guest_list):
    plus_1.append(input(f"Who will {person} bring as a plus one? "))
#2nd guests +1 cant come
print(f"Sorry {guest_list[2]} but you cant come as your +1 {plus_1[2]} is not able to come")
guest_list.remove(guest_list[2])
plus_1.remove(plus_1[2])
print("\nFinal invite list:\n")
print("\n".join(str(person + f" Is invited to the party, there plus one is {plus_1[i]}") for i, person in enumerate(guest_list)))


#task 3

print("\n")

bucket_list = ["uk","paris","canada","japan"]
print(f"List unorderd: {bucket_list}")
print(f"List orderd {sorted(bucket_list)}")
print(f"List unorderd again: {bucket_list}")

print("\n")

bucket_list.reverse()
print(f"List reved {bucket_list}")
bucket_list.reverse()
print(f"List un-reved {bucket_list}")

print("\n")

bucket_list.sort()
print(f"List orderd {bucket_list}")
bucket_list.sort(reverse=True)
print(f"List orderd backwards {bucket_list}")