import streamlit as st
st.write("Path to 7 GPA starts here 👑")
Courses_sem1 = {
    "CSSE1001": {
        "name": "Introduction to Software Engineering",
        "In_semester_exam": 0.25,
        "Assignment_1": 0.15,
        "Assignment_2": 0.20,
        "Final_exam": 0.40
    },
    "MATH1051": {
        "name": "Calculus & Linear Algebra",
        "In_semester_exam": 0.20,
        "Assignment_1": 0.075,
        "Assignment_2": 0.075,
        "Practical_exercise": 0.15,
        "Final_exam": 0.50
    },
    "STAT1201": {
        "name": "Analysis of Scientific data",
        "Paper_Review": 0.14,
        "Research_Project": 0.20,
        "Online_quizzes": 0.16,
        "Final_exam": 0.50
    },
    "SCIE1000": {
        "name": "Theory and Practice in Science",
        "Philosophy_assignment": 0.15,
        "Python_and_communication_assignment": 0.15,
        "Practical_exercises": 0.10,
        "Final_exam": 0.60
    }
}

# 2. LOGIC: Wahi fixed function jo humne banaya tha
def calculate_needed(points_earned, desired_gpa, remaining_weight):
    gpa_to_percentage = {7: 85, 6: 75, 5: 65, 4: 50}
    target_total = gpa_to_percentage[desired_gpa]
    gap = target_total - points_earned
    if remaining_weight <= 0:
        return 0 if gap <= 0 else float('inf')
    return gap / remaining_weight

# --- STREAMLIT UI ---
st.set_page_config(page_title="UQ GPA Strategist", page_icon="🎓")
st.title("🎓 UQ Semester 1 GPA Strategist")
st.markdown("Calculate exactly what you need on your remaining exams to hit your target GPA.")

# Step 1: Course Selection
course_code = st.selectbox("Select your course:", list(Courses_sem1.keys()))
course_data = Courses_sem1[course_code]
st.subheader(f"Course: {course_data['name']}")

points_earned = 0.0
weight_completed = 0.0

# Step 2: Assessment Inputs
st.info("Check the assignments you have finished and enter your scores.")

for item, weight in course_data.items():
    if item in ["name", "credits"]:
        continue
    
    # Checkbox aur Score input side-by-side
    col1, col2 = st.columns([1, 2])
    with col1:
        is_finished = st.checkbox(f"{item} ({int(weight*100)}%)", key=item)
    
    if is_finished:
        with col2:
            score = st.number_input(f"Your score for {item}:", min_value=0.0, max_value=100.0, value=100.0, key=f"score_{item}")
            points_earned += (score * weight)
            weight_completed += weight

# Step 3: Target GPA
remaining_weight = 1.0 - weight_completed
target_gpa = st.select_slider("Select your target GPA:", options=[4, 5, 6, 7], value=7)

# Step 4: Final Results
if st.button("Calculate My Target Score"):
    needed = calculate_needed(points_earned, target_gpa, remaining_weight)
    
    st.divider()
    st.write(f"### Results for {course_code}")
    st.metric("Points Secured So Far", f"{points_earned:.2f} / {int(weight_completed*100)}")
    
    if needed > 100:
        st.error(f"⚠️ Impossible to get a GPA {target_gpa}. You would need **{needed:.2f}%** on remaining work.")
    elif needed <= 0:
        st.balloons()
        st.success(f"🎉 You have already secured enough marks for a GPA {target_gpa}!")
    else:
        st.warning(f"🎯 To get a GPA {target_gpa}, you need to average **{needed:.2f}%** on the remaining {int(remaining_weight*100)}% of the course.")
