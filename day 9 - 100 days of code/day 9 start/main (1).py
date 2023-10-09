programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
  "loop": "doing something over and over again."
}
# print(programming_dictionary["Bug"])

for key in programming_dictionary:
  # print(key)
  print(programming_dictionary[key])
programming_dictionary={}
print(programming_dictionary)
dept={
  "cse":{"staffs":["thyagu", "alagu"], "students":["vasanth","sanjay"]}
  
}
for i in dept:
  print (dept)

def inp_func():
  name = input("What is your name?: ")
  bid = input("What is your bid?: $")