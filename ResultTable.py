"""
Gabriella Soares
gsoa420
"""

def bubble_sort(results):
	for pass_num in range(len(results) - 1, 0, -1):
		for i in range(0, pass_num):
			
			#sorts based on higher team points
			if int(results[i][1]) < int(results[i + 1][1]): 
				results[i], results[i + 1] = results[i + 1], results[i]
		
			#if the points are the same, sort on higher goal difference
			if results[i][1] == results[i + 1][1]: 
				if (int(results[i][2]) - int(results[i][3])) < (int(results[i + 1][2]) - int(results[i + 1][3])):
					results[i], results[i + 1] = results[i + 1], results[i]

			#if points are the same and goal difference is the same, sort on goals scored
			if (results[i][1] == results[i + 1][1]) and (int(results[i][2]) - int(results[i][3])) == (int(results[i + 1][2]) - int(results[i + 1][3])):
				if results[i][2] < results[i + 1][2]:
					results[i], results[i + 1] = results[i + 1], results[i]

def result_table():
	#processing file
	infile = open('table1.txt', "r")
	table = infile.read()
	infile.close()
	table_list = table.split('\n')

	#fomatting output
	print('    {0:30} {1:5}   {2:7}  {3:2}'.format('Team', 'Points', 'Diff', 'Goals'))
	results = []
	number = 0
	
	for info in table_list:
		info = info.split(',')
		results.append(info) 
	bubble_sort(results)
	
	#splits elements and formats output
	for item in results:
		name = item[0]
		points = item[1]
		goals_scored = item[2]
		goals_against = item[3]
		diff_goals = int(goals_scored) - int(goals_against)
		number += 1
		print('{0:2}. {1:26}  {2:7}  {3:5}  {4:5} : {5:2}'.format(int(number), name, int(points), int(diff_goals), int(goals_scored), int(goals_against)))

def main():
	print("Results table by gsoa420")
	print()
	print(result_table())

main()
