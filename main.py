import re


if __name__ == '__main__':

    with open("access_log_Jul95") as file:
        num = 0
        for line in file:
            if re.search('01/Jul/1995'
                         '(:[0][5]:[3][9]|:[0][5]:[4-5][0-9]|:[0][6]:[0-5][0-9]|:[0][7]:[0-4][0-9]|:[0][7]:[5][0-5])'
                         '.*GET.*[4-5][0-9][0-9]'
                         '*.html',
                         str(line)):

                num += 1

    print("Number of failed GET requests = ", num)
