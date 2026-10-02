import os
FILE = "power.txt"
content = []
if os.path.exists(FILE):
    with open(FILE,"r",encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            parts = line.strip().split(",")
            if len(parts) != 2:
                print(f"跳过格式不对的一行：{line}")
                continue
            content.append({"月份":int(parts[0]),"用电量":float(parts[1])})
def ask_int(promot,low,high):
    n = int(input(promot))
    while n < low or n > high:
        n = int(input(f"请重新输入在{low}-{high}之间的数字"))
    return n
def ask_float(promot,low):
    x = float(input(promot))
    while x < low:
        x = float(input(f"请输入大于{low}的数字"))
    return x
if len(content) == 0:
    print("暂无历史记录请先录入")
else:
    print(f"已读取{len(content)}条数据")
while True:
    print("1. 录入用电记录")
    print("2. 查看全部记录")
    print("3. 统计分析")
    print("4. 退出")
    choice =input("请选择")
    if choice == "1":
        n = ask_int("您要录入几条数据",1,999)       
        for i in range(n):
            month = ask_int("请输入月份",1,12)
            energy = ask_float("请输入电量",0)
            content.append({"月份":month,"用电量":energy})
        with open(FILE,"w",encoding="utf-8") as f:
            for x in content:
                f.write(f"{x['月份']},{x['用电量']}\n")
    elif choice == "2":
        if len(content) == 0:
            print("还没有数据，请先输入")
        else :
            print(f"{'月份':<8}{'用电量':>6}")
            print("-"*18)
            for record in content:
                print(f"{record['月份']:<8}{record['用电量']:>6}")
    elif choice == "3":
        def classify(power):
            if power < 100:
                level = "低用电量"
            elif 100 <= power <= 300:
                level = "用电量正常"
            elif power > 300:
                level = "高用电量"
            return level
        if len(content) == 0:
            print("暂无数据无法统计")
        else:
            total = 0
            for record in content:
                total = total +record['用电量']
            print(f"总用电量为{total}度")
            average = total / len(content)
            print(f"平均用电量为{average:.1f}度")
            top = content[0]
            for challenger in content:
                if challenger["用电量"] > top["用电量"]:
                    top = challenger
            print(f"用电最多：{top['月份']}月，{top['用电量']}度")
            low = content[0]
            for loser in content:
                if loser["用电量"] < low["用电量"]:
                    low = loser
            print(f"用电最少：{low['月份']}月，{low['用电量']}度")
            for record in content:
                print(f"{record['月份']}月{classify(record['用电量'])}")
            above = []
            for record in content:
                if record["用电量"] > average:
                    above.append(record)
            print(f"高于平均用电量的有{len(above)}个月")
            for record in above:
                print(f"{record['月份']}月，{record['用电量']}度")
    elif choice == "4":
        print("BYE")
        break
    else:
        print("请输入1-4的数字")





