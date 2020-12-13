subjects_list=[]
start_hour=8 #school start at 8.am
next_hout=9 #1st next hour is 9.am
school days=['monday','saturday']
time_slot_list=[] #get list of time slot
subjects_per_slot={}
def ask_hour():
	print(f'subjects list:{subjects_list}')
	print(f'planning time: {start_hour}h-{next_hour}h')
	user_answer input('what subject do u want to put here?')
	return user_answer
def fill_in_timetable():
	global start_hour
	global next_hour

	for day in school days:
	the_hour={}
	time=0
	start_hout=8
	next_hour=9
	print('\n...')
	print(f'{day.capitalize()} timetable')
	print('.....\n')

	