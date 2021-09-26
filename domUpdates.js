const tag = document.createElement("div");

let testName = "Objected-Oriented";
let testSubject = "CS";
let testNo = "2110";

const createMiniCardTag = (courseName, subject, courseNo) =>  `<div class="course-result">
                                                                <div class="micro-card-fill"></div>
                                                                <div class="basic-info">
                                                                    <div>
                                                                        <span class="card-sub1">` + subject + `</span>
                                                                        <span class="card-sub2">` + courseNo + `</span>
                                                                    </div>
                                                                    <div>
                                                                        <p class="card-name">` + courseName + `</span>
                                                                    </div>
                                                                </div>
                                                                </div>
                                                                `


tag.innerHTML = createMiniCardTag(testName, testSubject, testNo);

const element = document.getElementById("course-results");
element.appendChild(tag);

console.log("Package delivered");
