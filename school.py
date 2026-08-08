# ==========================================
# 🏫 SCHOOL PORTAL (Console Test Version)
# ==========================================

# Database stored in memory
students = {
    "101": {"name": "Alex", "marks": {"Math": 85, "Science": 90, "English": 88}},
    "102": {"name": "Sam", "marks": {"Math": 78, "Science": 82, "English": 80}},
}

homework = [
    {"subject": "Math", "task": "Exercise 3.2 Q1-5", "due": "Friday"},
    {"subject": "Science", "task": "Read Chapter 4", "due": "Monday"}
]

def student_view():
    print("\n--- 👨‍🎓 STUDENT DASHBOARD ---")
    student_id = input("Enter your Roll Number (e.g., 101): ").strip()
    
    if student_id in students:
        student = students[student_id]
        print(f"\nWelcome, {student['name']}!")
        
        print("\n📊 YOUR MARKS:")
        for subject, score in student["marks"].items():
            print(f"  • {subject}: {score}/100")
            
        print("\n📚 ACTIVE HOMEWORK:")
        for hw in homework:
            print(f"  • [{hw['subject']}] {hw['task']} (Due: {hw['due']})")
    else:
        print("❌ Roll Number not found!")

def teacher_view():
    print("\n--- 👩‍🏫 TEACHER PORTAL ---")
    pwd = input("Enter Teacher Password: ")
    
    if pwd != "teacher123":
        print("❌ Incorrect password!")
        return
    
    print("\n✅ Authenticated as Teacher!")
    print("1. Add / Update Marks")
    print("2. Post Homework")
    choice = input("Select choice (1 or 2): ").strip()
    
    if choice == "1":
        print("\nAvailable Students:", ", ".join(students.keys()))
        roll = input("Enter Student Roll Number: ").strip()
        
        if roll in students:
            subj = input("Enter Subject (Math/Science/English): ").strip()
            try:
                score = int(input("Enter Score (0-100): "))
                students[roll]["marks"][subj] = score
                print(f"✅ Success! Updated {students[roll]['name']}'s {subj} mark to {score}.")
            except ValueError:
                print("❌ Invalid input! Score must be a number.")
        else:
            print("❌ Invalid Roll Number!")
            
    elif choice == "2":
        subj = input("Enter Subject: ").strip()
        task = input("Enter Task Description: ").strip()
        due = input("Enter Due Date: ").strip()
        homework.append({"subject": subj, "task": task, "due": due})
        print("✅ Homework posted successfully!")

# Main Loop
while True:
    print("\n" + "="*35)
    print("      🏫 SCHOOL MANAGEMENT SYSTEM")
    print("="*35)
    print("1. Student View")
    print("2. Teacher View")
    print("3. Exit")
    
    user_choice = input("Select an option (1-3): ").strip()
    
    if user_choice == "1":
        student_view()
    elif user_choice == "2":
        teacher_view()
    elif user_choice == "3":
        print("Exiting program... Goodbye!")
        break
    else:
        print("❌ Invalid choice, please try again.")
