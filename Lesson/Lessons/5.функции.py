

lst = ['Петрова', 'Сидоров']
def print_lastnames(names):
    for name in names:
        if name[0] == 'П' and name[-1] == 'а':
            print(name)
print_lastnames(lst)  # выводит фамилию, которая начинается на п и заканчивается на а



# лучший средний балл
pupils = [{"name":"User1","physics":5,"history":7}, {"name":"User2","physics":3,"history":2}, {"name":"User2","physics":6,"history":4}]
def calc_av_score(users):
    for user in users:
        av = (user["physics"] + user["history"]) / 2
        user["score"] = av

calc_av_score(pupils)

def print_good_students(students, needScore):
    for student in students:
        if student["score"] >= float(needScore):
            print(f'Good student is: {student["name"]}')

print_good_students(pupils, 4)