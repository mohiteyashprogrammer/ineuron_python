
name = "yash mohite"
print(name.replace("yash", "isha"))# replaceing the string 
print(name.replace(" ", "."))
print(len(name))

name = "yash raju mohite"
print(name[5])#string index
print(name[:9])#string slicing
print(name[::2])# string skipping
print(name[::-1])#string riversing
print(name.replace(" ","."))
print(len(name))

text = "i am yash mohite and im a good boy and i can do whatever fuck i want"
print(text.count("i"))#count function to count string
print(text.split(" "))#split function to split string


#data = input("Enter the date of birth: DD/MM/YYYY")

#date, month, year = data.split("/")
#print(f"you were born in this month {month} on this date {date} on this year {year}")
print(text.capitalize())
print(text.lower())
print(text.upper())
print(text.title())
print(text.startswith("yash"))


print("|".join(name))
print(reversed(name))

num = "2356858"
print(num.isdigit())
print(num.startswith("2"))
print(num.endswith("8"))