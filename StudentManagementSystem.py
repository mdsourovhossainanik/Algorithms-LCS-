# 🏫 School Management System using Dictionary and match-case

students = {}   # মূল student data store করার dictionary
backup = {}     # backup data রাখার জন্য আলাদা dictionary

# 🎯 Function to add student
def add_student():
    sid = int(input("Enter Student ID: "))
    name = input("Enter Name: ")
    cls = input("Enter Class: ")
    roll = int(input("Enter Roll: "))
    section = input("Enter Section: ")
    
    students[sid] = {
        "name": name,
        "class": cls,
        "roll": roll,
        "section": section
    }
    print("✅ Student Added Successfully!\n")

# 🎯 Function to update student
def update_student():
    sid = int(input("Enter Student ID to Update: "))
    if sid in students:
        print("Current Info:", students[sid])
        name = input("Enter New Name: ")
        cls = input("Enter New Class: ")
        roll = int(input("Enter New Roll: "))
        section = input("Enter New Section: ")
        students[sid].update({
        "name": name,
        "class": cls,
        "roll": roll,
        "section": section
    }) 
        print("🆙 Student Updated Successfully!\n")
    else:
        print("⚠️ Student ID Not Found!\n")

# 🎯 Function to delete student
def delete_student():
    sid = int(input("Enter Student ID to Delete: "))
    if sid in students:
        students.pop(sid) #dictionary থেকে key-value pair মুছে ফেলার method
        print("🗑️ Student Deleted Successfully!\n")
    else:
        print("⚠️ Student ID Not Found!\n")

# 🎯 Function to view all students
def view_students():
    if students: #“যদি students dictionary খালি না হয়”
        print("\n📋 All Student Records:")
        for sid, info in students.items(): #students.items() → dictionary-এর সব key-value pair access করার সহজ উপায়
            print(f"ID: {sid} → {info}")
    else:
        print("\n⚠️ No Student Records Found!\n")

# 🎯 Function to search student
def search_student():
    sid = int(input("Enter Student ID to Search: "))
    if sid in students:
        print("🔎 Student Found:", students.get(sid)) #spacipic key er jonno value get kore
    else:
        print("⚠️ Student Not Found!\n")

# 🎯 Function to clear all data
def clear_all():
    confirm = input("Are you sure you want to clear all records? (yes/no): ").lower()
    if confirm == "yes":
        students.clear()
        print("🚫 All Records Cleared!\n")
    else:
        print("❌ Cancelled.\n")

# 🎯 Function to create backup
def backup_data():
    global backup
    backup = students.copy()
    print("💾 Backup Created Successfully! Total Students:", len(backup))

# 🎯 Function to restore from backup
def restore_data():
    global students
    if backup:
        students = backup.copy()
        print("♻️ Data Restored Successfully from Backup!\n")
    else:
        print("⚠️ No Backup Found! Please create a backup first.\n")

# 🔁 Main menu using match-case (Python 3.10+)
while True:
    print("\n========= 🏫 SCHOOL MANAGEMENT MENU =========")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. View All Students")
    print("5. Search Student")
    print("6. Backup Data")
    print("7. Restore Data")
    print("8. Clear All Records")
    print("0. Exit")
    print("============================================")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            add_student()
        case 2:
            update_student()
        case 3:
            delete_student()
        case 4:
            view_students()
        case 5:
            search_student()
        case 6:
            backup_data()
        case 7:
            restore_data()
        case 8:
            clear_all()
        case 0:
            print("👋 Exiting... Thank you!")
            break
        case _:
            print("❌ Invalid Choice! Please try again.\n")
