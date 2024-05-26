#more practice function with arguements default arguement, keyword arguement, required arguement, variable -length arguement , return statement 

# def name(fname,mname,lname):
#     print("Hello ",fname,mname,lname)

# name("prachi","thole")

#variablelength arguement example:
'''what this below program is doing 
it is taking any list of values in tuple and calculate there average like if you provide 1,2,3 for avearge calculation
it will do 1+2+3/3 why divided by 3 as we have passed 3 numbers even if you provide any 100 values for caluclation it will 
calculate it in same way , added return statement instaed of print use of return is after calculating the value of function or we can say
once we get the  output from function it will pass back to the calling function and give it to wherever we are calling that function refer below example'''

def average(*num):
    # print(type(num)) #printing which type of data type we are using here we are using tuple
    sum = 0
    for i in num:
        sum= sum + i
        return sum / len(num)
#     print("avarage is: ", sum / len(num))

c= average(1,2,3,5)
print(c)

# for doing same with string value 
'''you can pass values in any sequnce it is easily read by python and arrange then in function sequecne passed we have pass
sequcnec details in print statement '''

# def name(**name):
#      print(type(name)) # printing the type of data type like in this case it is dictionary
#     print("Hello",name["fname"],name["mname"],name["lname"])

# name(lname="jhfj", fname="nafjnfd", mname ="hfjd")







