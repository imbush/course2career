import json
import requests
import time

seasonsToSearch = ["FA19", "SP20", "FA20", "SP21", "SU21", "FA21"]
# seasonsToSearch = ["FA21"]

# Get Subject Dictionary
response = requests.get("https://classes.cornell.edu/api/2.0/config/subjects.json?roster=FA21")
if response.status_code >= 400:
    print("ERROR: ", response.status_code)
parsedSubjects = json.loads(response.text)["data"]["subjects"]
subjectsDict = dict()
for subject in parsedSubjects:
    subjectsDict[subject["value"]] = subject
    subjectsDict[subject["value"]]["courses"] = dict()

# For all subjects, adds course dictionary to subject
for subject in subjectsDict:
    response = requests.get("https://classes.cornell.edu/api/2.0/search/classes.json?roster=FA21&subject=" + subject)
    if response.status_code >= 400:
        print("ERROR: ", response.status_code)

    parsedCourses = json.loads(response.text)["data"]["classes"]
    for course in parsedCourses:
        parsedCourse = dict()
        attrToKeep = ["subject", "titleLong", "catalogNbr", "description", "acadCareer"]
        for attr in attrToKeep:
            parsedCourse[attr] = course[attr]
        subjectsDict[subject]["courses"][parsedCourse["catalogNbr"]] = parsedCourse
    print(subject, "processed.")

subjectsDict["description"] = "This JSON contains all courses on course roster from Fall 2021." 

with open("courses.json", 'w') as outJSON:
    outJSON.truncate(0)
    json.dump(subjectsDict, outJSON, indent=4)
