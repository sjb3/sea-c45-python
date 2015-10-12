data = {
    'Bill Gates': [1.00, 10.00, 100.00],
    'Steve Bezos': [8.00, 888.00, 8888.00],
    'Paul Allen': [12.00, 2.10]
}


ONE_CUT_LETTER=


'''
Dear {donor},
Thank you so much for your kind donation of {amount}. We here at the Foundation
for Homeless Whales greatly appreciate it. Your money will go towards creating
new oceans on the moon for whales to live in.
Thanks again,
Justin Byun
Director, F.H.W.
'''
MAIN_MENU=
'''
Welcome to Mailroom Madness

T - Send a Thank You mail
R - Formulate a Report
Q - Quit the program
'''
T_MENU=
'''
Please enter a name, or choose from the following:
list - Print a list of previous donors
Q - Return to main menu.
'''

AMOUNT_PROMPT=
'''
Please enter a donation amount or 'Q':

'''

ENTER_TO_CONTINUE = '\n\nPress enter to continue.'

CELL_WIDTHS = [20, 8, 3, 8]

def main_menu (user_input):
    
    if user_input in ('T'):
        repl(T_MENU, t_menu)
    
    elif user_input in ('R'):
        report()
    '''
    elif user_input in ('Q')
        
        return'Quit'
    '''
    else:
        return'Invalid'


def repl(prompt, validator=None):
    
    while True:
        user_input = raw_input(prompt)
        if user_input in ('Q'):
            print 'Goodbye!'
            return

        if validator:
            result = validator(user_input)
            if result:
                
                if 'Invalid' in str(result):
                    print result
                else:
                    return result
        else:
            return



def t_menu(user_input):
    
    if user_input == 'list':
        
        print list_donor_names()
        return repl(ENTER_TO_CONTINUE)
    
    else:
        name = user_input
        
        if is_valid_name(name):
            amount = repl(AMOUNT_PROMPT, is_valid_amount)
            if amount:
                add_to_data(name, amount)
                letter = LETTER_TEMPLATE.format(name=name,
                                    amount=format_amount(amount))
                print letter
                return repl(ENTER_TO_CONTINUE)
        
        else:
            return 'Invalid'


def list_donor_names():
    
    global data
    return '\n'.join(data.keys())


def is_valid_name(name):
    
    names = name.split(' ')
    if len(names) < 2:
        return False
    for n in names:
        if not n.isalpha() or not n.istitle():
            return False
    return True


def is_valid_amount(user_input):
    
    try:
        return round(float(user_input), 2)
    
    except ValueError:
        return 'Invalid Amount'


def format_amount(amount):
    
    return '$%.2f' % amount


def report():
    
    global data

    donor_list = data.keys()
    donor_list.sort()
    row_list = get_report_header()

    for d in donor_list:
        donations = data[d]
        total = sum(donations)
        num = len(donations)
        avg = total / num
        row = [d, format_amount(total), str(num), format_amount(avg)]
        row_list.append(get_report_cells(row))

    print '\n'.join(row_list)
    return repl(ENTER_TO_CONTINUE)


def get_report_header():
    
    header = ['\n']
    header.append(get_report_cells(['Name', 'Total', '#', 'Average']))
    header.append('-' * (sum(CELL_WIDTHS) + (3 * len(CELL_WIDTHS))))
    return header


def get_report_cells(row):
    
    formatted_row = []
    for i, c in enumerate(row):
        spaces = ' ' * (CELL_WIDTHS[i] - len(c))
        formatted_row.append('{}{}'.format(spaces, c))
    return ' | '.join(formatted_row)


def add_to_data(name, amount):
    
    global data
    if name not in data.keys():
        data[name] = []
    data[name].append(amount)


if __name__ == '__main__':
    repl(MAIN_MENU, main_menu)


##################################################    