#new_list = [new_item for item in list_of_items if test}
list_items = ["2", "5","5"]
new_list = [item for item in list_items if int(item) > 3]
print(new_list)

#new_dic = {new_key:new_value for (key, value) in dict.items() if test}
import random
names = ["ana", "carla", "camila", "carol"]
students_scores = {student:random.randint(1,100) for student in names}

#Looping for a dictionary (example)
passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}


#Exemplo utilizando split de nomes