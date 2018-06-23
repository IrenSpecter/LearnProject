
classes_info = [
    {
        'school_class': '4a',
        'scores': [2, 3, 4, 5, 2]
    },
    {
        'school_class':'4b',
        'scores': [1, 4, 5, 2, 3]
    },
    {
        'school_class':'4c',
        'scores': [3, 5, 5, 2, 5]
    }
    ]

for class_index in range(len(classes_info)):
    class_score1 = classes_info[class_index]['scores']
    class_sum1 = 0
    for score in class_score1:
        class_sum1 += score
    class_mean1 = class_sum1 / len(class_score1)
    print(class_mean1)


school_sum = 0
people_in_school = 0
for class_info in classes_info:
    for score in class_info['scores']:
        school_sum += score
    people_in_school += len(class_info['scores'])
school_mean = school_sum / people_in_school
print(school_mean)