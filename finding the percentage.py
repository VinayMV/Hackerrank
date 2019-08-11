if __name__ == '__main__':
    n = int(input())
    sum1=0
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for key in student_marks:
        if key == query_name:
            for j in student_marks[key]:
                sum1+=j
    print ('%.2f'%(sum1/3),end='') 

