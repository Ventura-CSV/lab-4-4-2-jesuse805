def main():
    """
    ########################################
    Code Your Program here
    """
    #Via Slide 25
    while True:
        user_input = input('')
        try:
            number = int(user_input)
        except ValueError:
            print('Input must be numeric')
            continue
        else:
            print(number)
            break
    
    
    """
    ########################################
    """

    ########################################
    # Do not delete the return statement
    ########################################
    return number


if __name__ == '__main__':
    main()
