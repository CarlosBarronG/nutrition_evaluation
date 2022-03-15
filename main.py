import math
def nutrition_evaluation():
    weight = float(input("Introduce weight = "))
    weight_units = input("Introduce units (kg or lbs) = ")
    height = float(input("Introduce height = "))
    height_units = input("Introduce units (cm, m, ft, in) = ")
    age = float(input("Introduce age= "))
    gender = input("Introduce gender (m or f) = ")
    physical_activity = input("Introduce physical activiy (Intense, Moderate, Low) = ")
    hr = float(input("Introduce Basal Heart Rate = "))
    triceps = float(input("Introduce triceps fold in mm ="))
    subescapular = float(input("Introduce Subscapular fold in mm ="))
    biceps = float(input("Introduce Biceps fold in mm ="))
    chest = float(input("Introduce Chest fold in mm ="))
    axial = float(input("Introduce Axial fold in mm ="))
    iliac = float(input("Introduce Iliac fold in mm ="))
    supraspinal = float(input("Introduce Supraspinal fold in mm ="))
    abdominal = float(input("Introduce Abdominal fold in mm ="))
    thigh = float(input("Introduce Thight fold in mm ="))
    calf = float(input("Introduce Calf fold in mm ="))
    print("NOW WE ARE GOING TO REGISTER CIRCUMFERENCES")
    waist = float(input("Introduce Waist circumference in cm ="))
    hip = float(input("Introduce Hip circumference in cm ="))
    wrist = float(input("Introduce Wrist circumference in cm ="))
    relaxed_arm = float(input("Introduce relaxed_arm circumference in cm ="))
    bistyloid = float(input("Introduce bystyloid diameter in cm = "))
    femoral= float(input("Introduce femoral diameter in cm = "))
    if weight_units.upper() == "KG" and height_units.upper() == "CM":
        imc = weight / ((height / 100) ** 2)
    elif weight_units.upper() == "KG" and height_units.upper() == "M":
        imc = weight / (height ** 2)
    elif weight_units.upper() == "LBS" and height_units.upper() == "M":
        imc = (weight / .45) / (height ** 2)
    elif weight_units.upper() == "LBS" and height_units.upper() == "CM":
        imc = (weight / .45) / ((height / 100) ** 2)
    icc = waist/hip
    if gender.upper() == "F" and icc >= 0.8:
        icc_interpretation = "Android"
    elif gender.upper() == "F" and icc < 0.8:
        icc_interpretation = "Gynecoid"
    elif gender.upper() == "M" and icc >= 1:
        icc_interpretation = "Android"
    elif gender.upper() == "F" and icc < 1:
        icc_interpretation = "Gynecoid"
    if height_units.upper() == "M":
        complexion = (height*100)/wrist
    elif height_units.upper() == "CM":
        complexion = height/wrist
    elif height_units.upper() == "IN":
        complexion = (height*2.54)/wrist
    elif height_units.upper() == "FT":
        complexion = (height*30.48)/wrist
    if gender.upper() == "F":
        ambr = ((relaxed_arm-((triceps/10)*3.1416))**2)/(3.1416*4)-6.5
    elif gender.upper() == "M":
        ambr = ((relaxed_arm - ((triceps / 10) * 3.1416)) ** 2) / (3.1416 * 4) - 10
        abr = (ambr**2)/(3.1416*4)
    if gender.upper() == "F" and age <= 19:
        c = 1.1599
        m = 0.0717
    elif gender.upper() == "F" and age <= 29:
        c = 1.1549
        m = 0.0678
    elif gender.upper() == "F" and age <= 39:
        c = 1.1423
        m = 0.0645
    elif gender.upper() == "F" and age <= 49:
        c = 1.1339
        m = 0.0632
    elif gender.upper() == "F" and age >= 50:
        c = 1.1333
        m = 0.0612
    elif gender.upper() == "M" and age <= 19:
        c = 1.1620
        m = 0.0630
    elif gender.upper() == "M" and age <= 29:
        c = 1.1631
        m = 0.0632
    elif gender.upper() == "M" and age <= 39:
        c = 1.1422
        m = 0.0544
    elif gender.upper() == "M" and age <= 49:
        c = 1.1620
        m = 0.0700
    elif gender.upper() == "M" and age >= 50:
        c = 1.1715
        m = 0.0779
    if gender.upper() == "F":
        arm_fat_area = abr+6.5
    else:
        arm_fat_area = abr+10
    fat_percent = arm_fat_area/abr*100
    fat_formula=input("Introduce the formula to be used (Durnin, Brozek, Faulkner, Thorland, Jackson) = ")
    if fat_formula.upper() == "DURNIN":
        density= c-(m*math.log10(triceps+subescapular+biceps+supraspinal))
        total_fat_percent=495/density-450
    elif fat_formula.upper() == "JACKSON" and gender.upper() == "F":
        constant1 = triceps+supraspinal+abdominal+thigh
        density = 1.096095-(0.0006952*constant1)+(0.0000011*constant1**2)-(0.0000714*age)
        total_fat_percent=(457/density)-414.2
    elif fat_formula.upper() == "JACKSON" and gender.upper() == "M":
        constant2 = chest + axial + triceps + subescapular + supraspinal + abdominal + thigh
        density = 1.112 - (0.00043499 * constant2) + (0.00000055 * constant2 ** 2) - (0.000028826 * age)
        total_fat_percent = (457 / density) - 414.2
    elif fat_formula.upper() == "BROZEK":
        density = c - (m * math.log10(triceps + subescapular + biceps + supraspinal))
        total_fat_percent = 457/density-414.2
    elif fat_formula.upper() == "FAULKNER" and gender.upper() == "F":
        constant3 = triceps + subescapular + supraspinal + abdominal
        total_fat_percent = constant3 * 0.213 + 7.9
    elif fat_formula.upper() == "FAULKNER" and gender.upper() == "M":
        constant3 = triceps + subescapular + supraspinal + abdominal
        total_fat_percent = constant3 * 0.153 + 5.789
    elif fat_formula.upper() == "THORLAND" and gender.upper() == "F":
        constant4 = triceps + subescapular + iliac
        density = 1.0987 - 0.00122 * constant4 + constant4**2
        total_fat_percent = 495 / density - 450
    elif fat_formula.upper() == "THORLAND" and gender.upper() == "M":
        constant4 = triceps + subescapular + axial + iliac + abdominal + thigh + calf
        density = 1.1091 - 0.00052 * constant4 + 0.00000032 * constant4**2
        total_fat_percent = 495 / density - 450
    total_fat = total_fat_percent * weight / 100
    muscle_formula= input("Introduce your favorite formula for muscle mass calculation (Heymsfield or Matiegka) =")
    if height_units.upper() == "M":
        height_cm = height * 100
    elif height_units.upper() == "FT":
        height_cm = height * 30.48
    elif height_units.upper() == "IN":
        height_cm = height * 2.54
    else:
        height_cm = height
    if weight_units.upper() == "LBS":
        weight_kg = weight * 0.453592
    else:
        weight_kg = weight
    osea_mass = ((((height_cm/100)**2)*(bistyloid/100)*(femoral/100)*400)**0.712)*3.02
    residual_mass = weight_kg * 0.209
    if muscle_formula.upper() == "HEYMSFIELD":
        muscle_mass_kg = height_cm * (0.0264 + 0.0029*ambr)
    elif muscle_formula.upper() == "MATIEGKA" :
        muscle_mass_kg = weight_kg - (total_fat+osea_mass+residual_mass)
    muscle_percent=muscle_mass_kg*weight_kg/100
    osea_percent=osea_mass*weight_kg/100
    residual_percent=residual_mass*weight_kg/100
    print(f"Your IMC is: {imc}")
    print(f"Your fat % is: {total_fat_percent}")
    print(f"Your total fat is: {total_fat}")
    print(f"Your muscle mass is: {muscle_mass_kg}")
    print(f"Your osea mass is: {osea_mass}")
    print(f"Your residual mass is: {residual_mass}")
    from matplotlib import pyplot as plt
    body_composition=[total_fat_percent,muscle_percent,osea_percent,residual_percent]
    body_composition_tag = ['total_fat_percent', 'muscle_percent', 'osea_percent', 'residual_percent']
    fig= plt.figure(figsize=(10,7))
    plt.pie(body_composition, labels = body_composition_tag)
    plt.show()

nutrition_evaluation()
