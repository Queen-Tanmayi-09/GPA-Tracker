'''The logic of the project'''
#Semester 1 subjects
#CSSE1001
#MATH1051
#STAT1201
#SCIE1000

Courses_sem1= {
    "CSSE1001": {
        "name": "Introduction to Software Engineering",
        "credits": 2,
        "In_semester_exam" : 0.25,
        "Assignment_1" : 0.15,
        "Assignment_2" : 0.20,
        "Final_exam" : 0.40
    },
    "MATH1051": {
        "name": "Calculus & Linear Algebra",
        "credits": 2,
        "In_semester_exam" : 0.20,
        "Assignment_1" : 0.075,
        "Assignment_2" : 0.075,
        "Practical_exercise" : 0.15,
        "Final_exam" : 0.50
    },
    "STAT1201": {
        "name": "Analysis of Scientific data",
        "credits": 2,
        "Paper_Review" : 0.14,
        "Research_Project" : 0.20,
        "Online_quizzes" : 0.16,
        "Final_exam" : 0.50
    },
    "SCIE1000": {
        "name": "Theory and Practice in Science",
        "credits": 2,
        "Philosophy_assignment" : 0.15,
        "Python_and_communication_assignment" : 0.15,
        "Practical_exercises" : 0.10,
        "Final_exam" : 0.60
        
    }
}

#logic to calculate percentage required to get a 7 gpa
def calculate_required_percentage(current_percentage, desired_gpa, remaining_weight):
    gpa_to_percentage = {7: 85, 6: 75, 5: 65, 4: 50}
    target= gpa_to_percentage[desired_gpa]
    
    if desired_gpa not in gpa_to_percentage:
        raise ValueError("Desired GPA must be between 4 and 7.")
    
    required_total_percentage = gpa_to_percentage[desired_gpa]
    required_percentage = (required_total_percentage - current_percentage * (1 - remaining_weight)) / remaining_weight
    
    return required_percentage
#Select_course

print("Available Courses:", list(Courses_sem1.keys()))
course_code = input("Enter course code: ").upper()
course_data = Courses_sem1.get(course_code)

points_earned = 0
weight_completed = 0

# 2. Loop through assessments in the dictionary
for assessment, weight in course_data.items():
    # Skip metadata keys
    if assessment in ["name", "credits"]:
        continue
    
    status = input(f"Have you finished {assessment} ({int(weight*100)}%)? (y/n): ").lower()
    
    if status == 'y':
        score = float(input(f"Enter your score for {assessment} (0-100): "))
        points_earned += (score * weight)
        weight_completed += weight

# 3. Calculate what's left
remaining_weight = 1.0 - weight_completed

if remaining_weight <= 0:
    print("All assessments finished! Check your final total.")
else:
    goal = int(input("Enter desired GPA (4-7): "))
    needed = calculate_required_percentage(points_earned, goal, remaining_weight)
    
    print("-" * 30)
    print(f"Course: {course_data['name']}")
    print(f"Points earned so far: {points_earned:.2f} / {int(weight_completed*100)}")
    
    if needed > 100:
        print(f"Warning: You need {needed:.2f}% to get a {goal}. That's impossible, aiming for a lower GPA might be realistic.")
    elif needed <= 0:
        print(f"Congrats! You've already secured a GPA {goal}!")
    else:
        print(f"To get a GPA {goal}, you need to score {needed:.2f}% on the remaining assessments.")


current_percentage = float(input("Enter your current percentage: "))
desired_gpa = int(input("Enter your desired GPA (4-7): "))
remaining_weight = float(input("Enter the remaining weight of assessments (as a decimal): "))





# ye remaining_weight tumhe calculate karna hoga based on tumhare course ke assessments ke %age weightage ke hisab se.
# ye 1-Remaining_weight tumhare current_percentage ko multiply karega to find out ki tumne ab tak kitna score kiya h. This is basically tumne kitna percent kaam finish kiya hai and will calculate your score when multiplied by current_percentage.
required_percentage = calculate_required_percentage(current_percentage, desired_gpa, remaining_weight)
print(f"To achieve a GPA of {desired_gpa}, you need to score {required_percentage:.2f}% in the remaining assessments.")

'''A Practical Example (CSSE1001)
Let's say you've finished all assignments but the Final Exam (40%).remaining_weight = 0.4
weight_done = 0.6
current_avg = 90% 
(You're doing great!)target = 85(For a GPA of 7)
The Formula Calculation:Percentage already earned: 90 * 0.6 = 54
Percentage still needed: 85 - 54 = 31
Required exam score: frac{31}/{0.4} = 77.5%
Result: You only need 77.5% in the final exam to secure a GPA 7!'''