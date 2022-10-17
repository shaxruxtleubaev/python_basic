from homework_lesson30 import Study

School = Study('School', '9-11 years', 'Middle')
College = Study('College', '2 years', 'Middle')
University = Study('University', '4 years', 'High')
with open('studyy.txt', mode='a') as file:
    school_info = []
    school_info.append(School.match())
    college_info = []
    college_info.append(College.match())
    university_info = []
    university_info.append(University.match())
    file.write(f'\n{school_info}')
    file.write(f'\n{college_info}')
    file.write(f'\n{university_info}')
    file.close()
















