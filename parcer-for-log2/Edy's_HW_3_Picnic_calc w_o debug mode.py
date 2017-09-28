import json
import sys

DATA_FILE = "C:\\Users\\svetah\\Desktop\\workspace\\HW\\parcer-for-log2\\picnic_list.json"

def read_picnic_data():
    with open(DATA_FILE, 'r') as f:
        picnic_data = json.load(f)
        return picnic_data['food_and_drinks']


#How to calculate the tests that number of childrens = num of girls+ num of boys ?????


def enter_number_of_participants_adults():
    input_num_of_adults = int(raw_input("Please enter num of adults:"))
    return input_num_of_adults

def enter_number_of_participants_children():
    input_num_of_children = int( raw_input("Please enter num of children:"))
    return input_num_of_children


def enter_number_of_participants_boys():
    input_num_of_boys = int( raw_input("Please enter num of boys:"))
    return input_num_of_boys

def enter_number_of_participants_girls():
    input_num_of_girls = int( raw_input( "Please enter num of girls:" ))
    return input_num_of_girls

def calculation(input_num_of_adults, input_num_of_children , picnic_data):
        meat_for_adults = (input_num_of_adults * picnic_data['meat_per_adult'])
        meat_for_children = input_num_of_children * picnic_data['meat_per_child']
        meat_total = meat_for_adults + meat_for_children
        beers_for_adults = (input_num_of_adults * picnic_data['beer_per_adult'])
        beers_for_children = (input_num_of_children * picnic_data['beer_per_child'])
        beers_total = beers_for_adults + beers_for_children
        softdrink_for_adults = (input_num_of_adults * picnic_data['soft_drink_per_adult'])
        softdrink_for_children = input_num_of_children * picnic_data['soft_drink_per_child']
        softdrink_total = softdrink_for_adults + softdrink_for_children
        cost_meat_for_adults = (input_num_of_adults * picnic_data['cost_meat_per_adults'])

        print('Meat for adults is : %s kg' % (meat_for_adults))
        print ("Meat for children is : %s kg" % (meat_for_children))
        print ("Total meat is: %s kg " % (meat_total))
        print ("Total beers_for_adults is: %s bottles " % (beers_for_adults))
        print ("Total beers_for_children is: %s bottles" %(beers_for_children))
        print ("Total beers is: %s bottles" % (beers_total))
        print('Soft Drink for adults is: %s litrs' % (softdrink_for_adults))
        print ("Soft Drink for children is: %s" % (softdrink_for_children))
        print ("Total Soft Drink is: %s " % (softdrink_total))
        print('Cost of meat for adults is: %s NIS' % (cost_meat_for_adults))


def calculation_presents(input_num_of_boys, input_num_of_girls, picnic_data):
    boys_presents = (input_num_of_boys )
    girls_presents = (input_num_of_girls)
    total_price_present_for_children = ((input_num_of_boys + input_num_of_girls) * picnic_data['cost_present_per_child'])
    print ("Total boys presents is: %s units" % (boys_presents))
    print ("Total girls presents is: %s units" % (girls_presents))
    print( "Total cost for presents is: %s NIS" % (total_price_present_for_children) )



def main():
    a =  read_picnic_data()
    x = enter_number_of_participants_adults()  # meahsenim parametr 'num of adults' in x she machil returned ereh
    y = enter_number_of_participants_children()
    b = enter_number_of_participants_boys()
    g = enter_number_of_participants_girls()
    calculation_presents(b,g,a)
    calculation(x,y,a)

if __name__ == '__main__':
   main()