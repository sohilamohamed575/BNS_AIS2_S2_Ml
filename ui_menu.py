import os
# ==========================================================================
# 1) شاشات عامة / Helpers
# ==========================================================================
 
def clear_screen():
    """Clear the terminal screen (works on Windows and Unix)."""
    os.system("cls" if os.name == "nt" else "clear")
 
 
def print_header(title):
    """Print a consistent section header/banner."""
    width = 50
    print("\n" + "=" * width)
    print(title.center(width))
    print("=" * width)
 
 
def print_divider():
    print("-" * 50)
 
 
def print_message(message, kind="info"):
    """
    Print a formatted status message.
    kind: 'success' | 'error' | 'info'
    """
    icons = {"success": "[OK]", "error": "[ERROR]", "info": "[INFO]"}
    tag = icons.get(kind, "[INFO]")
    print(f"{tag} {message}")
 
 
# ==========================================================================
# 2) شاشة الترحيب
# ==========================================================================
 
def print_welcome_screen():
    clear_screen()
    print("=" * 50)
    print("     WELCOME TO THE HOSPITAL MANAGEMENT SYSTEM".center(50))
    print("=" * 50)
 
 
def print_hospital_banner(hospital_name, hospital_location):
    print(f"\nHospital: {hospital_name}   |   Location: {hospital_location}")
 
 
# ==========================================================================
# 3) القائمة الرئيسية (Main Menu)
# ==========================================================================
 
MAIN_MENU_OPTIONS = {
    "1": "Add Department",
    "2": "Register Patient",
    "3": "Register Staff",
    "4": "Search Patient by Name",
    "5": "View Full Hospital Report",
    "6": "Save Data to File",
    "0": "Exit",
}
 
 
def show_main_menu():
    """Display the main menu and return the raw choice string entered by the user."""
    print_header("MAIN MENU")
    for key, label in MAIN_MENU_OPTIONS.items():
        print(f"  {key}. {label}")
    print_divider()
    choice = input("Enter your choice: ").strip()
    return choice
 
 
# ==========================================================================
# 4) شاشات فرعية لكل عملية (كل شاشة بتاخد الداتا الخام من اليوزر وترجعها)
#    ملحوظة: الشاشات دي بترجع القيم "زي ما هي" -
#    التحقق من صحتها هو مسؤولية Input Validation
# ==========================================================================
 
def show_add_department_screen():
    print_header("ADD DEPARTMENT")
    dept_name = input("Enter new department name: ")
    return dept_name
 
 
def show_register_patient_screen():
    print_header("REGISTER PATIENT")
    name = input("Patient name: ")
    age = input("Patient age: ")
    record = input("Medical record (e.g. 'No known allergies'): ")
    return {"name": name, "age": age, "medical_record": record}
 
 
def show_register_staff_screen():
    print_header("REGISTER STAFF")
    name = input("Staff name: ")
    age = input("Staff age: ")
    position = input("Staff position (e.g. 'Cardiologist'): ")
    return {"name": name, "age": age, "position": position}
 
 
def show_search_patient_screen():
    print_header("SEARCH PATIENT")
    name = input("Enter patient name to search: ")
    return name
 
 
def show_department_selection_screen(department_names):
    """
    department_names: list of strings (names only, provided by Integration/Operations)
    Returns the raw choice string (index typed by the user, as text).
    """
    print_header("SELECT DEPARTMENT")
    if not department_names:
        print_message("No departments exist yet. Please add one first.", "error")
        return None
 
    for i, name in enumerate(department_names, start=1):
        print(f"  {i}. {name}")
    print_divider()
    choice = input("Choose a department by number: ").strip()
    return choice
 
 
# ==========================================================================
# 5) شاشة عرض التقرير  (بتاخد الداتا جاهزة و"بس بتعرضها" بشكل منظم)
# ==========================================================================
 
def show_hospital_report_screen(report_data):
    """
    report_data: dict expected shape (built by the Operations part):
    {
        "hospital_name": str,
        "location": str,
        "total_departments": int,
        "total_patients": int,
        "total_staff": int,
        "departments": [
            {
                "name": str,
                "patients": [ "display string", ... ],
                "staff": [ "display string", ... ],
            },
            ...
        ]
    }
    """
    print_header(f"HOSPITAL REPORT: {report_data['hospital_name']}")
    print(f"Location: {report_data['location']}")
    print(f"Total Departments: {report_data['total_departments']}")
    print(f"Total Patients:    {report_data['total_patients']}")
    print(f"Total Staff:       {report_data['total_staff']}")
 
    if not report_data["departments"]:
        print("\nNo departments registered yet.")
        return
 
    for dept in report_data["departments"]:
        print(f"\n--- Department: {dept['name']} ---")
 
        print(f"  Patients ({len(dept['patients'])}):")
        if dept["patients"]:
            for line in dept["patients"]:
                print(f"    - {line}")
        else:
            print("    (no patients)")
 
        print(f"  Staff ({len(dept['staff'])}):")
        if dept["staff"]:
            for line in dept["staff"]:
                print(f"    - {line}")
        else:
            print("    (no staff)")
 
    print("=" * 50)
 
 
def show_search_results_screen(search_name, results):
    """
    results: list of display strings (e.g. "[Dept: Cardiology] ID: 1 | Name: Alice...")
             already prepared by the Operations part.
    """
    if not results:
        print_message(f"No patient found matching '{search_name}'.", "error")
        return
 
    print_header(f"SEARCH RESULTS FOR '{search_name}'")
    for line in results:
        print(f"  {line}")
 
 
# ==========================================================================
# 6) شاشة الخروج
# ==========================================================================
 
def show_exit_screen():
    print_header("GOODBYE")
    print("Thank you for using the Hospital Management System!")
 
 
# ==========================================================================
# اختبار سريع لعرض الشاشات وهي شغالة (Demo Mode)
# شغّل الملف ده لوحده عشان تتفرج على الشاشات بدون أي كلاسات/داتا حقيقية
# ==========================================================================
if __name__ == "__main__":
    print_welcome_screen()
    print_hospital_banner("City Hospital", "123 Main St")

    # جرب القائمة الرئيسية بنفسك
    choice = show_main_menu()
    print_message(f"You chose option: {choice}", "info")

    # لو اخترتي 2 (تسجيل مريض) جرب الشاشة دي كمان
    if choice == "2":
        patient_data = show_register_patient_screen()
        print_message(f"You entered: {patient_data}", "success")

    show_exit_screen()
