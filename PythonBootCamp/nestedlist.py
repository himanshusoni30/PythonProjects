new_list=[]
if __name__ == '__main__':
    for n in range(int(input())):
    	name = input()
    	score = float(input())
    	marksheet=[name,score]
    	new_list.append(marksheet)
    	print(new_list)
    second_highest=sorted(list(set([marks for name,marks in new_list])))[1]
    print('\n'.join([a for a,b in sorted(new_list) if b == second_highest]))



'''
# Shortest way:
if __name__ == '__main__':
    n = int(input())
    marksheet = [[input(),float(input())] for _ in range(n)]
    second_highest=sorted(list(set([marks for name,marks in marksheet])))[1]
    print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))
'''
