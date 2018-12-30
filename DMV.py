#Zach Moskovitz
#HW 5-3
#DMV.py
#The program asks the user for their password and if entered correctly gives them a menu to either generate a random license plate number,
#calculate ticket fees, or to calculate registration fees. The menu also gives the user the option to quit.

#import the random module to be used for generating license plates
import random
#import the datetime module to use later in the program
import datetime
#import get_num which holds the int_val function to validate the data later in the program
import get_num
#define the main function
def main():
    #call the pass_validation function and use an if statement to determine if the program should continue
    if pass_validation()==False:
        print('You have failed to enter the correct password.')
        end_prgrm=input('Press Enter to continue') #if the user doesn't enter the password correctly after the third try then the program ends
    else:  #if the password was entered correctly then the run_menu function will run
        run_menu()

        
#define the pass_validation function
def pass_validation():
    password='password' #set the password
    counter=1  #create the accumulator to limt the amount of times the user can try to enter the password correctly
    pass_input=input('Enter your password: ')
    if pass_input==password: #if the password entered matches the set passwrod the  it will returna True boolean expression
        return True
    while pass_input != password:  #if the entered password doesn't match up then it will print an error message and request the password again
        counter+=1
        print('ERROR! You must enter the correct password!')
        if counter==3:
            print('WARNING! You have one more chance to enter the correct password!')
        pass_input=input('Enter your password: ')
        if counter==3: #if the user doesn't get t in 3 tries then it returns a False boolean expression 
            return False

#define the run_menu function
def run_menu():
    loop_menu()
    
        
#define loop_menu function
def loop_menu():
    print() #create the menu that will be displayed
    print('          MENU')
    print('         ------')
    print('1) Generate Random License Plate')
    print('2) Calculate Registration Fees')
    print('3) Calculate Ticket Fees')
    print('4) Quit')
    draw_menu() #call the draw_menu function to recieve user's choice
    
#define the draw_menu function
def draw_menu():
    print()
    #recieve the choice from the user using int_val to validate the number inputted by the user if it is a valid menu option or not
    user_choice=get_num.int_val(1,4,'Choose an option from the menu: ','ERROR! You must choose a valid option from the menu!!!') 
    print()
    #create if else statement to determine which function to run based on the user's choice
    if user_choice==1:
        gen_license_plate()
    elif user_choice==2:
        calc_reg_fee()
    elif user_choice==3:
        calc_ticket_fee()
    elif user_choice==4:
        print('Goodbye!')
        

#define the gen_license_plate function
def gen_license_plate():
    print()
    print('     Random License Plate Number')
    print('     -----------------------------')
    print(chr(random.randint(65,90)),end='')
    print(chr(random.randint(65,90)),end='')
    print(chr(random.randint(65,90)),end='')
    print('-',end='')
    print(random.randint(0,9),end='')
    print(random.randint(0,9),end='')
    print(random.randint(0,9),end='')
    print(random.randint(0,9),end='')
    print()
    run_menu() #run the menu again so the user can choose another option
#define the calc_reg_fee function
def calc_reg_fee():
    car_age=car_year() #call the car_year function to calculae how old the car is
    driver_age=driver_birth_year() #call the driver_birth_year function to calculate how old the driver is
    base_fee=175 #set a base fee
    discount=20 #set a discount to subtract from base fee if car_age fits the requirements
    extra_fee_5yr=25 #set the extra fee for f car is over 5 yrs old
    extra_fee_10yr=75 #set the extra fee for if car is over 10 yrs old
    extra_fee_over65=50 #set the fee for if the driver is over 65 yrs old
    #create if elif statements to determine the discount or extra fee given based on the information input by the user
    if car_age<=3:
        base_fee-=discount
    elif car_age>5 and car_year<=10:
        base_fee+=extra_fee_5yr
    elif car_age>10:
        base_fee+=extra_fee_10yr
    if driver_age>65:
        base_fee+=extra_fee_over65
        for  fee in range(70,driver_age+1,5):
            base_fee+=25
    print('Your registration fee is: $',base_fee)
    run_menu() #run the menu again so the user can choose another option
        

#define car_year function
def car_year():
    caryear=get_num.int_val(1920,2019,'In what year was your car manufactured? ','ERROR! You must enter a valid year of manufacturation!!!') #use int_val to validate the year of the car so user cannot put in an invalid 
    car_age=((datetime.datetime.now().year)-caryear) #determine how old the car is in number of years
    #return the car's age to the calc_reg_fee function to use the data
    return car_age

#define the driver_age function using the same method as car_year
def driver_birth_year():
    driver_birth_year=int(input('Enter your birth year: '))
    driverage=((datetime.datetime.now().year)-driver_birth_year) #determine how old the driver is in number of years
    while  (driverage<17 and driverage>120): #vaildate whether or not the driver is underage or should not be alive
        print('ERROR! You must enter a valid  year of birth!')
        driver_birth_year=int(input('Enter your birth year: '))
        #return the driver's age to the calc_reg_fee function to use the data
    return driverage

#define the function calc_ticket_fee. similar to the cal_reg_fee function
def calc_ticket_fee():
    total_owed=total_ticket_fees()
    print('Your total amount of ticket fees is: $',format(total_owed, '.2f'))
    run_menu() #run the menu again so the user can choose another option

#define total_ticket_fees function
def total_ticket_fees():
    ticket_amount_total=0
    number_of_tckts=get_num.int_val(1,999,'How many tickets are you caculating? ','You must have a least one ticket to use this service!')
    for counter in range(1,number_of_tckts+1):
        ticket_amount=float(input("How much does ticket #"+str(counter)+" cost?  $"))
        ticket_age=int(input('How many years old is ticket #'+str(counter)+' ?  '))
        #create if elif statement to determine what fees (if any) the user has added onto the the original valueof the ticket
        if ticket_age<2:
            ticket_amount_total+=ticket_amount
        elif ticket_age>2 and ticket_age<=4:
            ticket_amount_total+=((ticket_amount*0.12)+ticket_amount)
        elif ticket_age>4 and ticket_age<=6:
            ticket_amount_total+=((ticket_amount*0.25)+ticket_amount)
        elif ticket_age>6:
            ticket_amount_total+=(ticket_amount*2)
    #return the total money owed to the calc_ticket_fees function
    return ticket_amount_total

#call the main function to run the program
main()
