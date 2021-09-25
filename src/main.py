import json
import requests
import re
import yake

"""Generate ordered dictionary with all Cornell courses from the given roster."""
def createCourseJSON(roster: str, subjectsDict: dict) -> dict:
    # Get Subject Dictionary
    response = requests.get("https://classes.cornell.edu/api/2.0/config/subjects.json?roster=" + roster)
    if response.status_code >= 400:
        print("ERROR: ", response.status_code)
    parsedSubjects = json.loads(response.text)["data"]["subjects"]
    for subject in parsedSubjects:
        if not subjectsDict.get(subject["value"]):
            subjectsDict[subject["value"]] = subject
            subjectsDict[subject["value"]]["courses"] = dict()

    # For all subjects of this year, adds course dictionary to subject
    for parsedSubject in parsedSubjects:
        subject = parsedSubject["value"]
        response = requests.get("https://classes.cornell.edu/api/2.0/search/classes.json?roster=" + roster + "&subject=" + subject)
        if response.status_code >= 400:
            print("ERROR: ", response.status_code)

        parsedCourses = json.loads(response.text)["data"]["classes"]
        for course in parsedCourses:
            if not subjectsDict.get(subject).get(course["catalogNbr"]):
                parsedCourse = dict()
                attrToKeep = ["subject", "titleLong", "catalogNbr", "description", "acadCareer"]
                for attr in attrToKeep:
                    parsedCourse[attr] = course[attr]
                parsedCourse["rosterURL"] = ("https://classes.cornell.edu/browse/roster/"+ roster + 
                                            "/class/" + parsedCourse["subject"] + "/" + parsedCourse["catalogNbr"])
                subjectsDict[subject]["courses"][parsedCourse["catalogNbr"]] = parsedCourse
        print(roster, subject, "processed.")
    if subjectsDict.get("rosters"):
        subjectsDict["rosters"].append(roster)
    else:
        subjectsDict["rosters"] = [roster]

"""Add titleKeywords, descriptionKeywords, and level attribute to course."""
def addKeywordsLevel(course: dict, subject: str, titleExtractor, descrExtractor) -> None:
    # get TitleKeyWords
    title = course["titleLong"]
    titleKeywords = [keyword[0] for keyword in titleExtractor.extract_keywords(course["titleLong"])]
    descriptionKeywords = [keyword[0] for keyword in descrExtractor.extract_keywords(course["description"])]

    titleKeywords.append(subject)
    course["titleKeywords"] = titleKeywords
    course["descriptionKeywords"] = descriptionKeywords
    course["level"] = getLevel(course)

"""Return value in {0, 1, 2} mapping to {beginner, intermediate, advanced}."""
def getLevel(course: dict) -> int:
    catalogNbr = int(course["catalogNbr"])
    acadCareer = course["acadCareer"]
    title = course["titleLong"].lower()

    if "intro" in title or title.startswith("elementary"):
        return 0
    if "intermediate" in title:
        return 1
    if "advanced" in title:
        return 2

    if acadCareer == "GR" or acadCareer == "LA" or acadCareer == "VT":
        level = 2
    elif acadCareer == "UG":
        level = 0
    else:
        level = 1

    if catalogNbr >= 6000:
        level = round((level + 2) / 2)
    elif catalogNbr >= 5000:
        level = round((level + 1.5) / 2)
    elif catalogNbr >= 4000:
        level = round((level + 1) / 2)
    elif catalogNbr >= 2000:
        level = round((level + 0.5) / 2)
    else:
        level = round(level / 2)

    return level



if __name__ == "__main__":
    subjectsDict = dict()
    rosters = ["SP19", "SU19", "FA19", "WI19", "SP20", "SU20", "FA20", "WI20", "SP21", "SU21", "FA21", "WI21"]
    for roster in rosters:
        createCourseJSON(roster, subjectsDict)

    with open("courses.json", 'w') as outJSON:
        outJSON.truncate(0)
        json.dump(subjectsDict, outJSON, indent=4)

    # Create title keyword extractor
    max_ngram_size = 2
    deduplication_threshold = 0.9
    numOfKeywords = 2
    titleKwExtractor = yake.KeywordExtractor(lan="en", n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)
    
    # Create description keyword extractor
    max_ngram_size = 2
    deduplication_threshold = 0.3
    numOfKeywords = 10
    descrKwExtractor = yake.KeywordExtractor(lan="en", n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)
    
    with open("courses.json", "r") as inJSON:
        subjects = json.load(inJSON)

    # subject = "CS"
    # descrFormal = subjects[subject]["descrformal"]
    # for courseName in subjects[subject]["courses"]:
    #     course = subjects[subject]["courses"][courseName]
    #     print(courseName, course)
    #     addKeywordsLevel(course, descrFormal, titleKwExtractor, descrKwExtractor)
    # print("Keywords complete for", subject)

    for subject in subjects:
        try:
            descrFormal = subjects[subject]["descrformal"]
            for courseName in subjects[subject]["courses"]:
                course = subjects[subject]["courses"][courseName]
                addKeywordsLevel(course, descrFormal, titleKwExtractor, descrKwExtractor)
            print("Keywords complete for", subject)
        except:
            print("Unable to do keyword analysis in", subject)

    with open("coursesWithKW.json", 'w') as outJSON:
        outJSON.truncate(0)
        json.dump(subjects, outJSON, indent=4)