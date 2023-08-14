#Dictionary Comprehension Exercise1 - Calculating the number of letters in a particular word
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split()}
print(result)

#Dictionary Comprehension Exercise2 - Converting a dictionary temperature in celcius to a dictionary temperature in fahrenheit
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day:(temp_c*9/5) + 32 for (day, temp_c) in weather_c.items()}
print(weather_f)

#How to iterate over a Pandas DataFrame
student_dict = {
    "studeent": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictonaries
for (key, value) in student_dict.items():

    pass

import pandas
student_data_Frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_Frame.iterrows():

    pass


