def string_function():
    my_list = ['aba', 'xyz', 'aa', 'x' ,'bbb']  #list of strings
    for element in my_list:
        if len(element) >= 2 and element[0] == element[-1]:  # check the len for every string in the my list and if len >= 2 print it
                                                            # AND if first letter in string == to the last letter
            return element
            print element



def main():
    string_function()
if __name__ == '__main__':
   main()