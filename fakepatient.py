
# random patient generator

import random, xlwt
from xlwt import Workbook

row = 1

pt_sheet = Workbook()
pt_entry = pt_sheet.add_sheet('day1')
pt_entry.write(row, 0, 'prefix')
pt_entry.write(row, 1, 'name')
pt_entry.write(row, 2, 'surname')
pt_entry.write(row, 3, 'age')
pt_entry.write(row, 4, 'disease')
pt_entry.write(row, 5, 'department')
pt_entry.write(row, 6, 'mobile number')

row = 3


for i in range(100):
    
    # generate random name probably from southern indian states
    # final value variable = 'name' and 'surname'

    gender_option = ['male', 'male', 'female']
    gender = random.choice(gender_option)
    if gender == 'female':
        name_file = open('F:\\project_fake\\female_name.txt')
        name = random.choice(name_file.read().split(','))
    else:
        name_file = open('F:\\project_fake\\male_name.txt')
        name = random.choice(name_file.read().split(','))

    # surname generator for patient
    # final value variable = 'surname'

    surname_file = open('F:\\project_fake\\surname.txt') #surname generator
    surname_list = surname_file.read().split(',')
    surname = random.choice(surname_list)

    # assign a department for that patient from ayuved
    # final value variable = 'department'

    all_department_file = open('F:\\project_fake\\department.txt')
    all_departments = all_department_file.read().split(',')
    department = random.choice(all_departments)    
    
    # assign random age
    # final value variable = 'age'
    if department == 'Balachikitsa(Obstectrics/Pediatrics)':
        age = random.randint(1,16)
    else:
        age = random.randint(1,78)
    print('patient is ' + str(age) + ' years old.')

    # give a proper Ms, Miss, Mrs, Mr
    # final value variable = 'prefix'

    prefix_option = ['Miss', 'Mrs', 'Mrs', 'Ms']
    if gender == 'female' and age > 21 :
        prefix = random.choice(prefix_option)
    elif gender == 'female' and age < 21:
        prefix = 'Ms'
    else:
        prefix = 'Mr'
    print('patient\'s name is ' + prefix + ' ' + name + ' ' + surname + '.')

    # assign some disease into files so we can use them
    # final value variable = 'disease'

    kc_disease_file = open('F:\\project_fake\\kc_disease.txt') #kaya chikitsa
    kc = kc_disease_file.read().split(',')

    bc_disease_file = open('F:\\project_fake\\bc_disease.txt') # bala chikitsa
    bc = bc_disease_file.read().split(',')

    gc_disease_file = open('F:\\project_fake\\gc_disease.txt') #graha chikitsa
    gc = gc_disease_file.read().split(',')

    sc_disease_file = open('F:\\project_fake\\sc_disease.txt') #shakya chikitsa
    sc = sc_disease_file.read().split(',')

    skc_disease_file = open('F:\\project_fake\\skc_disease.txt') #shalakya chikitsa
    skc = skc_disease_file.read().split(',')

    vc_disease_file = open('F:\\project_fake\\vc_disease.txt') #visha chikitsa
    vc = vc_disease_file.read().split(',')

    rc_disease_file = open('F:\\project_fake\\rc_disease.txt') # rasayana chikitsa
    rc = rc_disease_file.read().split(',')

    vkc_disease_file = open('F:\\project_fake\\vkc_disease.txt') # veerajkarn chikitsa
    vkc = rc_disease_file.read().split(',')

    # assigning random disease from a list of disease comes under each department

    if department == 'Kayachikitsa(General Medicine)':
        disease = random.choice(kc)
        #print('patient is having treatment for ' + disease)
    elif department == 'Balachikitsa(Obstectrics/Pediatrics)':
        disease = random.choice(bc)
        #print('patient is having treatment for ' + disease)
    elif department == 'Graha Chikitsa(Psychiatry)':
        disease = random.choice(gc)
        #print('patient is having treatment for ' + disease)
    elif department == 'Salya Chikitsa(Surgery)':
        disease = random.choice(sc)
        #print('patient is having treatment for ' + disease)
    elif department == 'Salakya Chikitsa(ENT & Cephalic Diseases)':
        disease = random.choice(skc)
        #print('patient is having treatment for ' + disease)
    elif department == 'Visha Chikitsa(Toxicology)':
        disease = random.choice(vc)
        #print('patient is having treatment for ' + disease)
    elif department == 'Vajeekarana(Aphrodisiac Treatment)':
        if gender == 'male' and age > 30:
            disease = random.choice(vkc)
        else:
            disease = 'imfertility'
        #print('patient is having treatment for ' + disease)
    else:
        disease = random.choice(rc)
        #print('patient is having treatment for ' + disease)

    print('patient is having treatment for ' + disease + ' under ' + department + ' department.')
        
    # assign a doctor to the patient

    # generate random mobile number
    # final value variable = 'mobile_number'

    number = []
    first = number.append(random.randint(6,9))
    for digit in range(9):
        x = random.randint(0, 9)
        number.append(x)
    mobile_number = str(number[0]) + str(number[1]) + str(number[2]) + str(number[3]) + str(number[4]) + str(number[5]) + str(number[6]) + str(number[7]) + str(number[8]) + str(number[9])

    if age < 18:
        print('patient\'s parent\'s mobile number is ' + mobile_number)
    else:
        print('patient\'s mobile number is ' + mobile_number)
    
    
    pt_entry.write(row, 0, prefix)
    pt_entry.write(row, 1, name)
    pt_entry.write(row, 2, surname)
    pt_entry.write(row, 3, age)
    pt_entry.write(row, 4, disease)
    pt_entry.write(row, 5, department)
    pt_entry.write(row, 6, mobile_number)

    row += 1
    
        
    i += 1
pt_sheet.save('excel_sheet_patients_day6.xls')


    


