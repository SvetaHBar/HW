import json
import sys

Data_file = "C:\\Users\\svetah\\Desktop\\py\\parcer-for-log2\\picnic_list.json"
#meat_per_adult = float(0.5)   #kg # params for hardcoded instead of json
#meat_per_child = float(0.2)  #kg # params for hardcoded instead of json
#bear_per_adult = int(2) #bottle # params for hardcoded instead of json
#bear_per_child = int(0) # params for hardcoded instead of json
#soft_drink_per_adult = float(0.5) #litr # params for hardcoded instead of json
#soft_drink_per_child = float(0.5) #litr # params for hardcoded instead of json
#meat_price_per_kg # params for hardcoded instead of json
#bear_price_per_botle # params for hardcoded instead of json
#drink_price_per_botle # params for hardcoded instead of json



elements_from_json = []  # empty dict for keep all relevant params from json file
def read_from_file():
    with open(Data_file, 'r') as basic_info:
        read_data = json.load(basic_info)  #convert the json string to a dict
        iner_dict = read_data['data_per_oreah'] #because of json is a list of lists , will use only params from data_per_oreh list
        return iner_dict


def is_food_drink_in_dict(iner_dict):
    return iner_dict


def enter_number_of_participants_adults():
    input_num_of_adults = int(raw_input("Please enter num of adults:"))
    return input_num_of_adults

def enter_number_of_participants_children():
    input_num_of_children = int( raw_input("Please enter num of children:"))
    return input_num_of_children

def calculation(input_num_of_adults, input_num_of_children , iner_dict):
        meat_for_adults = (input_num_of_adults * iner_dict['meat_per_adult'])
        print('Meat for adults is :' , meat_for_adults, 'kg')
        meat_for_children = input_num_of_children * iner_dict['meat_per_child']
        print ("Meat for children is :" , meat_for_children, 'kg')
        meat_total  = meat_for_adults + meat_for_children
        print ("Total meat is: ", meat_total, 'kg')
        bears_for_adults = (input_num_of_adults * iner_dict['bear_per_adult'])
        print ("Total bears_for_adults is: ", bears_for_adults, 'bottle')
        bears_for_children = (input_num_of_children * iner_dict['bear_per_child'])
        print ("Total bears_for_children is: ", bears_for_children, 'bottle')
        bears_total = bears_for_adults + bears_for_children
        print ("Total bears is: ", bears_total, 'bottle')
        softdrink_for_adults = (input_num_of_adults * iner_dict['soft_drink_per_adult'])
        print('Soft Drink for adults is :', softdrink_for_adults, 'litr')
        softdrink_for_children = input_num_of_children * iner_dict['soft_drink_per_child']
        print ("Soft Drink for children is :", softdrink_for_children)
        softdrink_total = softdrink_for_adults + softdrink_for_children
        print ("Total Soft Drink is :",softdrink_total)




def main():
    a =  read_from_file()
    is_food_drink_in_dict(a)
    x = enter_number_of_participants_adults()  # meahsenim parametr 'num of adults' in x she machil returned ereh
    y = enter_number_of_participants_children()
    z = is_food_drink_in_dict(a)
    calculation(x,y,z)

if __name__ == '__main__':
   main()