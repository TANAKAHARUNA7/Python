import matplotlib.pyplot as plt

genders = ['Male', 'Female']

total_male_students = 676.398
total_female_students = 636.860
male_percentage = 51.51
female_percentage = 48.49

students = [total_male_students, total_female_students]

percentages = [male_percentage,female_percentage]

plt.figure(figsize=(14,6))

plt.subplot(1,2,1)
plt.bar(genders, students, color=['blue', 'pink'])
plt.xlabel('Gender')
plt.ylabel('Number of Students')
plt.title('Number of High School Students by Gender')
plt.grid(True)


plt.subplot(1,2,2)
plt.bar(genders, percentages, color=['blue', 'pink'])
plt.xlabel('Gender')
plt.ylabel('percentage (%)')
plt.title('percentage of High School Students by Gender')
plt.grid(True)


plt.tight_layout()
plt.show()




