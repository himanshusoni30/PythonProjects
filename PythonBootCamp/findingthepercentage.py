if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    # print(student_marks)
    query_name = input()
    list_marks = student_marks[query_name]
    # print(list_marks)
    add=0
    count=0
    for nums in list_marks:
    	nums = nums+add
    	add = nums
    	count += 1
    print("%.2f" % (add/count))
    