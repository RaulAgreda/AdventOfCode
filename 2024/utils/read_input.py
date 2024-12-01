from utils.terminal_colors import Colors
	
class ReadState:
	STARTING='starting'
	READING_INPUT='reading_input'
	READING_SOLUTION='reading_solution'	

def read_input(input_file):
	with open(input_file, 'r') as f:
		return f.read()
	
def read_test(input_file):
	input_string = ''
	solution = ''
	with open(input_file, 'r') as f:
		state = ReadState.STARTING
		text = f.read().split('\n')
		# Read all lines
		for line in text:
			if state == ReadState.STARTING:
				if line == 'INPUT:':
					state = ReadState.READING_INPUT
				else:
					return log_error()
			elif state == ReadState.READING_INPUT:
				if line == 'SOLUTION:':
					state = ReadState.READING_SOLUTION
					continue
				input_string += line + '\n'
			elif state == ReadState.READING_SOLUTION:
				solution = line
	return input_string[:-1], solution

def log_error():
	print(Colors.RED+"[ERROR] "+Colors.RESET+"Wrong test input file format")
	print("""The input format must be:
	INPUT:
	[input text]
	SOLUTION
	[solution text]""")
	return None