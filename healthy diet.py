def diet():

  age = int(input("What's the patient age? n/"))
  
  weight = int (input("What's is the patient weight (kilograms)? n/"))
  
  height = int(input("What is the patient height? n/"))

  print("What is the patient physical activity? (sedentary/moderate/active) n/")
  physical_activity = input()

  if age <= 18:
    print("We recomend a high carbohydrate diet")

  elif 18 < age < 35:
    print("We recomend a high protein and lower carbohydrate diet")

  elif age > 35:
    print("We recomend a low sugar diet")


  if 18 < age < 30 and physical_activity == "sedentary" or physical_activity == "moderate" :  
    print("We recomend areobic exercises")

diet()

  
