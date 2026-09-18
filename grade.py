student = []
while True:
    print("======成绩管理系统======")
    print("1.录入成绩")
    print("2.查看全部")
    print("3.统计平均分/最高分/最低分")
    print("4.退出")
    choice = input("请选择")
    if choice == "1":
        print("请录入成绩")
        n = int(input("你要录入几份成绩："))
        while n <= 0:
            n = int(input("你输入的数字无效，请重新输入："))
        for i in range(n):
            name = input(f"请输入第{i+1}位学生姓名：")
            while name == "":
                name = input("名字不可为空请重新输入")
            grade = float(input(f"请输入第{i+1}位学生成绩："))
            while grade < 0 or grade >100:
                grade = float(input("请重新输入1-100间的数字"))
            student.append({"name":name,"grade":grade})
        print(f"已录入{n}名学生成绩")
    elif choice == "2":
        if len(student) == 0:
            print("你还未录入成绩")
        else:
            print(f"{'姓名':<8}{'成绩':>6}")
            for stu in student:
                print(f"{stu['name']:<8}{stu['grade']:>6}")
    elif choice == "3":
        if len(student) == 0:
            print("你还未录入数据")
        else:
            scores = []
            for stu in student:
                scores.append(stu["grade"])
            average = sum(scores) / len(scores)
            print(f"总人数为{len(scores)}人")
            print(f"平均成绩为{average:.1f}")
            print(f"最高成绩为{max(scores)}")
            print(f"最低成绩为{min(scores)}")
    elif choice == "4":
        print("BYE") 
        break   
    else:
        print("请输入1-4的数字")
        
