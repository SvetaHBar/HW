import json
import sys

DATA_FILE = "C:\\Users\\svetah\\Desktop\\py\\parcer-for-log2\\picnic_list.json"

def read_from_file():
    with open(DATA_FILE, 'r') as f:
        picnic_data = json.load(f)  #convert the json string to a dict, where f is basic_info
        #iner_dict = read_data['data_per_oreah'] #because of json is a list of lists , will use only params from food_and_drinks list
        #return iner_dict
        return picnic_data['data_per_oreah']


#def is_food_drink_in_dict(picnic_data):
    #return picnic_data


def enter_number_of_participants_adults():
    input_num_of_adults = int(raw_input("Please enter num of adults:"))
    return input_num_of_adults

def enter_number_of_participants_children():
    input_num_of_children = int( raw_input("Please enter num of children:"))
    return input_num_of_children

def calculation(input_num_of_adults, input_num_of_children , picnic_data):
        meat_for_adults = (input_num_of_adults * picnic_data['meat_per_adult'])
        meat_for_children = input_num_of_children * picnic_data['meat_per_child']
        meat_total = meat_for_adults + meat_for_children
        bears_for_adults = (input_num_of_adults * picnic_data['bear_per_adult'])
        bears_for_children = (input_num_of_children * picnic_data['bear_per_child'])
        beers_total = bears_for_adults + bears_for_children
        softdrink_for_adults = (input_num_of_adults * picnic_data['soft_drink_per_adult'])
        softdrink_for_children = input_num_of_children * picnic_data['soft_drink_per_child']
        softdrink_total = softdrink_for_adults + softdrink_for_children

        print('Meat for adults is : %s kg' % (meat_for_adults))
        print ("Meat for children is : %s kg" % (meat_for_children))
        print ("Total meat is: %s kg " % (meat_total))
        print ("Total beers_for_adults is: %s bottles " % (bears_for_adults))
        print ("Total beers_for_children is: %s bottles" %(bears_for_children))
        print ("Total beers is: %s bottles" % (beers_total))
        print('Soft Drink for adults is: %s litrs' % (softdrink_for_adults))
        print ("Soft Drink for children is: %s" % (softdrink_for_children))
        print ("Total Soft Drink is: %s " % (softdrink_total))




def main():
    a =  read_from_file()
    #is_food_drink_in_dict(a)
    x = enter_number_of_participants_adults()  # meahsenim parametr 'num of adults' in x she machil returned ereh
    y = enter_number_of_participants_children()
   # z = is_food_drink_in_dict(a)
    calculation(x,y,a)

if __name__ == '__main__':
   main()