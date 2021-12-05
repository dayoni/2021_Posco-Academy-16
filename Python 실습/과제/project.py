import sys

# show
def show():
    print('   Student'.center(10) + 'Name'.rjust(15) + '    Midterm'.center(10) + 'Final'.center(10) + 'Average'.center(8) + 'Grade'.center(9) + '\n' + '-'*64)

# search
def search():
    student_id = input("Student ID : ")
    if student_id in stu_id:
        i = stu_id.index(student_id)
        show()
        print(stu_id[i].center(11)+stu_name[i].rjust(14)+stu_mid[i].center(13)+stu_fin[i].center(5)+stu_avg[i].center(11)+stu_gra[i].center(9), '\n')
    else:
        print("NO SUCH PERSON."+'\n')
    

# changescore
def changescore():
    student_id = input("Student ID : ")
    if student_id in stu_id:
        i = stu_id.index(student_id)
        stu_id[i] = student_id
        before = stu_id[i].center(11)+stu_name[i].rjust(14)+stu_mid[i].center(13)+stu_fin[i].center(5)+stu_avg[i].center(11)+stu_gra[i].center(9)
        exam = input("Mid/Final? ").lower()
        if exam == "mid":
            new_score = input("Input new score: ")
            if int(new_score) < 0 or int(new_score) > 100:
                return
            else:
                stu_mid[i] = new_score
                stu_avg[i] = (float(stu_mid[i]) + float(stu_fin[i])) / 2.0
                stu_gra[i] = cal_avg(stu_avg[i])
                stu_avg[i] = str(stu_avg[i])

                show()
                print(before)
                print("Score changed.")
                show()
                print(stu_id[i].center(11)+stu_name[i].rjust(14)+stu_mid[i].center(13)+stu_fin[i].center(5)+stu_avg[i].center(11)+stu_gra[i].center(9))
                print()
                return
        elif exam == 'final':
            new_score = input("Input new score: ")
            if int(new_score) < 0 or int(new_score) > 100:
                return
            else:
                stu_fin[i] = new_score
                stu_avg[i] = (float(stu_mid[i]) + float(stu_fin[i])) / 2.0
                stu_gra[i] = cal_avg(stu_avg[i])
                stu_avg[i] = str(stu_avg[i])
                
                show()
                print(before)
                print("Score changed.")
                show()
                print(stu_id[i].center(11)+stu_name[i].rjust(14)+stu_mid[i].center(13)+stu_fin[i].center(5)+stu_avg[i].center(11)+stu_gra[i].center(9))
                print()
                return
        else:
            print()
            return
    else:
        print("NO SUCH PERSON."+'\n')      
        
# add
def _add():
    student_id = input("Student ID: ")
    if student_id in stu_id:
        print("ALREDY EXISTS."+'\n')
    else:
        new_name = input("Name: ")
        new_mid = input("MIdterm Score: ")
        new_final = input("Final Score: ")
        new_avg = (float((new_mid)) + float((new_final))) / 2.0
        grade = cal_avg(new_avg)
        stu_gra.append(grade)
        
        stu_id.append(student_id)
        stu_name.append(new_name)
        stu_mid.append(new_mid)
        stu_fin.append(new_final)
        stu_avg.append(str(new_avg))        
        print("Student added."+'\n')

# remove
def _remove():
    if stu_id == []:
        print("List is empty."+'\n')
    else:
        student_id = input("Student ID: ")
        if student_id in stu_id:
            i = stu_id.index(student_id)
            del stu_id[i], stu_name[i], stu_mid[i], stu_fin[i], stu_avg[i], stu_gra[i]
            print("Student removed."+'\n')
        else:
            print("NO SUCH PERSON."+'\n')

# searchgrade
def searchgrade():
    index = []
    student_grade = input("Grade to search: ")
    if student_grade in ['A','B','C','D','F']:
        for i in range(len(stu_gra)):
            if stu_gra[i] == student_grade:
                index.append(i)
        if index == []:
            print("NO RESULTS."+'\n')
            return
        show()
        for i in index:
            print(stu_id[i].center(11)+stu_name[i].rjust(14)+stu_mid[i].center(13)+stu_fin[i].center(5)+stu_avg[i].center(11)+stu_gra[i].center(9))
        print()
    else:
        print()
        return

# quit
def quit():
    t = input("Save data?[yes/no] ").lower()
    stu_score = ''
    if t == 'yes':
        end_file = input("File name: ")
        end_file += '.txt'
        result = open(end_file, 'w')
        init_view = '   Student           Name   Midterm   Final   Average   Grade \n' + '-'*64+'\n'
        for i in range(len(stu_id)):
            stu_score += stu_id[i].center(11)+stu_name[i].rjust(14)+stu_mid[i].center(13)+stu_fin[i].center(5)+stu_avg[i].center(11)+stu_gra[i].center(9)+'\n'                
        text = init_view + stu_score
        result.write(text)
        result.close()
        return
    else: return        
        
def cal_avg(avg):
    if avg >= 90.0: grade = 'A'
    elif 80.0 <= avg < 90.0: grade = 'B'
    elif 70.0 <= avg < 80.0: grade = 'C'
    elif 60.0 <= avg < 70.0: grade = 'D'
    else: grade = 'F'
    return grade
        
# main
def main():
    global stu_id, stu_name, stu_mid, stu_fin, stu_avg, stu_gra
    if len(sys.argv) == 1:
        filename = 'students.txt'
    else:
        filename = sys.argv[1]
        
    text_in = open('students.txt', 'r')
    _stu = list()

    for i in text_in:
        stu=i[:-1].split('\t')
        _stu.append(stu)
    text_in.close()
    
    for i in range(len(_stu)):
        _sum, avg = 0.0, 0.0
        for j in range(len(_stu)-1):
            if (j == 2) | (j == 3):
                _sum += float(_stu[i][j])
                if j == 3:
                    avg = _sum / 2.0
                    grade = cal_avg(avg)
        _stu[i].insert(len(_stu), str(avg))
        _stu[i].insert(len(_stu), grade)
    _stu.sort(key=lambda x:x[4], reverse=True)

    stu_id, stu_name, stu_mid, stu_fin, stu_avg, stu_gra = [],[],[],[],[],[]

    for i in _stu:
        stu_id.append(i[0])
        stu_name.append(i[1])
        stu_mid.append(i[2])
        stu_fin.append(i[3])
        stu_avg.append(i[4])
        stu_gra.append(i[5])

    show()
    for i in range(len(stu_id)):    
        print(stu_id[i].center(11)+stu_name[i].rjust(14)+stu_mid[i].center(13)+stu_fin[i].center(5)+stu_avg[i].center(11)+stu_gra[i].center(9))
    print()

    while True:
        command = input("# ").lower()
        if command == 'show':                
            show()
            for i in range(len(stu_id)):    
                print(stu_id[i].center(11)+stu_name[i].rjust(14)+stu_mid[i].center(13)+stu_fin[i].center(5)+stu_avg[i].center(11)+stu_gra[i].center(9))
            print()
        elif command == 'search':
            search()

        elif command == 'changescore':
            changescore()

        elif command == 'add':
            _add()

        elif command == 'remove':
            _remove()

        elif command == 'searchgrade':
            searchgrade()

        elif command == 'quit':
            quit()
            break

        else:
            print()
            continue
            
main()
