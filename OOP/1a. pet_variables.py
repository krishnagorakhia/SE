name = 'Bonnie'
animal_category = 'Cat'
age = 3
vaccinated = True
ccard = '3423 2326 7543 1234'
billing_address = '17 Park Drive, The Shire 2695'
owner_name = 'Alex Ngyuen'
account_balance = 129.95

# ACTIVITIES:
#Theere are many ways to complete these tasks. How will you do them?
#1 Increase age by 1 year
#2 Change the address to 17 Park Street
#3 No longer vaccinated (change state of vaccinated)
#4 Prompt user for updated credit card number and save new number
#5 Change owner name to Alex Jones
#6 Subtract $25 from account balance

name = 'Bonnie'
animal_category = 'Cat'
age = 4
vaccinated = False
ccard = input('Enter a new credit card number, please. ')
billing_address = '17 Park Street, The Shire 2695'
owner_name = 'Alex Jones'
account_balance = 129.95 -25

print(name,type(age))
print(animal_category,type(animal_category))
print(billing_address,type(billing_address))
print(vaccinated,type(vaccinated))
print(owner_name,type(owner_name))
print(account_balance,type(account_balance))
