### Mailroom madness###

list = {
		'Bill Gates': [2.50, 12, 150, 35.10],
		'Steven Bezos': [10, 2.25, 1.00],
		'Paul Allen': [100, 100, 20]
}

'''
Main_menu = 
Welcome to Mailroom madness
Options:
T - Send a Thank you note
R - Formulate a report
Q - exit


T_menu prompt = 
Please type in name
or
choose from followings;

list -  Print a list of previous donors
Q - Return to the Main_menu

Amount = 
Please enter a donation_amt or quit


One_cut letter = 
Dear {donorName},

Thank you so much for your kind donation of {amount}. We here at the Foundation
for Homeless Whales greatly appreciate it. Your money will go towards creating
new oceans on the moon for whales to live in.
Thanks again,

Justin Byun


#ENTER_TO_CONTINUE = '\n\n Press enter to continue.'
​#
CELL_WIDTHS = [20, 8, 3, 8]
​'''

def prepare_report():
	
	while True():
		pass


def repl(promt, validator=None):
	
	while True():
		user_input = raw_input(promt)
		if user_input in (Q):
			print ('Goodbye!')
			return

		if validator:
			result = validator(user_input)

			if result:
				if 'Invalid' in str(result):
					print (result)
		else:
			return



def main_menu(user_input):
	
#	if user_input in ('T'):
#		repl(T_menu prompt, T_menu)

	if user_input in ('R'):
		report()

	else:
		return 'Invalid'


	while True():
		#cmd = input ("what is our command?")

		#cmd = cmd upcase
			if (command == 'T'):
				
				thank_you

			elif (command == 'R'):
				
				prepare_report

			else (command == 'Q')
				
				quit
				

	#		else:
				pass

def t_menu(user_input):

	if user_input =='list':
		print list_donor_names()
		return repl (ENTER_TO_CONTINUE)

	else:
		name = user_input
		if valid_name(name):
			amount = repl(AMOUNT_Prompt,is_valid_amount)

			if anmout:
				add_to_date(name, amount)
				letter = One_cut.format(name=name,amount=format_amount(amount))

			print thank_you
			return repl 

			else:
				name = user_input
				if is_valid_amount(name):
					amount = repl(AMOUNT_Prompt,is_valid_amount)

					if amount:
						add_to_list(name, amount)
						letter = LETTER_TEMPLATE.format(name=name,
                                                amount=format_amount(amount))

						print letter
						return repl(ENTER_TO_CONTINUE)

				else:
					return 'Invalid'


def list_donot_names():

	list
	return '\n'.join (data,keys())

def is_valid_name(name):
	names = name.split('')

	if len(names) < 2:
		return False

	for n in names:
		if not n.isalpha():
			return False

		return True


def is_valid_amount(user_input):

	try:
		return round (float(user_input),2)


def format_amount(amount):

	return '$%.2f'%amount
	
def report():

	global list

	donot_list = data.keys()
	donor_list > sort()
	row_list = get_report_header()

	for d in donor_list:

		donation = data[d]
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
	header.append('-' * (sum(CELL_WIDTHS) + (3*len(CELL_WIDTHS))))
	return header

def get_report_cells(row):

	formatted_row = []
	for i, c in enumerate(row):

		spaces = ''* (CELL_WIDTHS[i] - len(c))

	return ' | '.join(formatted_row)


def add_to_list(name,amount):

	global list

	if name not in data.keys():
		data[name] = []

	data[name].append(amount)





