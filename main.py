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
        "Practical_exercise" : 0.10,
        "Final_exam" : 0.60
        
    }
}

#logic to calculate percentage required to get a 7 gpa
def calculate_required_percentage(current_percentage, desired_gpa, remaining_weight):
    gpa_to_percentage = {7: 85, 6: 75, 5: 65, 4: 50}
    target_total = gpa_to_percentage[desired_gpa]
    
    # NEW LOGIC: Just find the gap and divide by what's left
    # Formula: (Target Total - Points already in the bag) / Weight of remaining exams
    gap = target_total - points_earned
    
    if remaining_weight <= 0:
        return 0 if gap <= 0 else float('inf')
        
    return gap / remaining_weight
#Select_course

print("Available Courses:", list(Courses_sem1.keys()))
course_code = input("Enter course code: ").upper()
#course_data = Courses_sem1.get(course_code)

if course_code in Courses_sem1:
    course = Courses_sem1[course_code]
    points_earned = 0  #optional
    weight_completed = 0

# 2. Loop through assessments in the dictionary
for assessment, weight in course.items():
    # Skip metadata keys
    if assessment in ["name", "credits"]:                        #might throw an error if these keys are not present.
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
    
    print("-" * 40)
    print(f"📊 SUMMARY FOR {course_code}")
    print(f"Points earned so far: {points_earned:.2f} / {int(weight_completed*100)}")
    print(f"Remaining course weight: {int(remaining_weight*100)}%")
    if needed > 100:
        print(f" ⚠️ Warning: You need {needed:.2f}% to get a {goal}. That's impossible, aiming for a lower GPA might be realistic.")
    elif needed <= 0:
        print(f" ✅ Congrats! You've already secured a GPA {goal}!")
    else:
        print(f" 🎯 To get a GPA {goal}, you need to score {needed:.2f}% on the remaining assessments.")

    print("-"*40)
    print("Thank you for using UQ_GPA_TRACKER")
    print("Made with 💖 by Tanmayi Mendhe")


# ye remaining_weight tumhe calculate karna hoga based on tumhare course ke assessments ke %age weightage ke hisab se.
# ye 1-Remaining_weight tumhare current_percentage ko multiply karega to find out ki tumne ab tak kitna score kiya h. This is basically tumne kitna percent kaam finish kiya hai and will calculate your score when multiplied by current_percentage.

'''A Practical Example (CSSE1001)
Let's say you've finished all assignments but the Final Exam (40%).remaining_weight = 0.4
weight_done = 0.6
current_avg = 90% 
(You're doing great!)target = 85(For a GPA of 7)
The Formula Calculation:Percentage already earned: 90 * 0.6 = 54
Percentage still needed: 85 - 54 = 31
Required exam score: frac{31}/{0.4} = 77.5%
Result: You only need 77.5% in the final exam to secure a GPA 7!'''