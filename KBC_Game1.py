question_list=["how many continents are there?","what is the capital of india","NG mai konse corse padaye jate hai"]
options_list=[["1.Four","2.nine","3.seven","4.Eight"],
                ["1.chandigarh","2.bhopal","3.chennai","4. Delhi"],
                ["1.software engineering","2.counseling","3.Tourirsm","4.agriculture"]
                ]


solution_list=[3,4,1]
life_line_list=[[2,3],[3,4],[3,1]]

row=0
while row<len(question_list):
    colomn=0
    print question_list[row]
    while colomn<=len(options_list):
        print options_list[row][colomn]
        colomn=colomn+1

    enter_your_ans=input("enter your ans")
    if enter_your_ans==solution_list[row]:
        print "good guess"
        print " "
    elif enter_your_ans==5050:
        b=0
        count=0
        while count<len(life_line_list):
            print question_list[row]
            countA=0
            number=1
            while countA<len(life_line_list[count]):
                g=life_line_list[count][countA]
                print number,g
                countA=countA+1
                number=number+1
            break
            count=count+1
        enter_input=input("enter which one number in 2 option")
        if enter_input == solution_list[row]:
            print "your sucess you win this question"
            print " "
        else:
            print "again you miss question"
            print " "
        b=b+1
        
    else:
        print "bad guess"
    row=row+1

    # print "sorry you are exit this game"