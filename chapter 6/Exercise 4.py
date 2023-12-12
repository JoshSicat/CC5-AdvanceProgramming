import json

#function to write student details to json file 
def write_to_json(file_name):
    student_details = {}

    #asking user for student details
    student_name = input("Entry your name: ")
    student_id = input("Entry your id: ")
    student_course = input("Entry your course: ")

    #update of student details dictionary
    student_details["Name"] = student_name
    student_details["ID"] = student_id
    student_details["course"] = student_course

    #write initail student  details to json file
    with open(file_name, 'w') as file:
        json.dump(student_details, file, indent=4)
    print("student details written to json file successfully. ")

#fucntion to read and update json file with course details
def update_json(file_name): 
    with open(file_name, 'r') as file:
        data = json.load(file)
    
    # appending course details for  student 1
    data['courseDetails'] = {
        "Group": "A",
        "Year": 2
    }

    #Update json file with the added course details
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)
    print("coursedetails added to json file successfully. ")

#fucntion to read and update json file with course details
def read_from_json(file_name):
    with open(file_name, 'r') as file:
        student_data = json.load(file)

    #diplaying the student details
    print("\ndetails of the student are")
    print("Name:", student_data["Name"])
    print("ID:", student_data["ID"])
    print("course:", student_data["course"])

    if "CourseDetails" in student_data:
        print("Group:", student_data["coursedetails"]["Group"])
        print("Year:", student_data["coursedetails"]["Year"])

#file name for json, student details, and coursedetail
file_name = 'Studentjson.json'

write_to_json(file_name)

update_json(file_name)

read_from_json(file_name)