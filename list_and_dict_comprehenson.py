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

#Looping DataFrames With Pandas
#exemplo: {new_key:new:value for(index, row) in df.iterrows()}



#Criando um dicionário a partir de um dicionário
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day:(temp_c  * 9/5) + 32 for (day, temp_c) in weather_c.items()}
print(weather_f)



