const tag = document.createElement("div");
const tag2 = document.createElement("div");
const tag3 = document.createElement("div");

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

const createBigCardTag = (courseName, subject, courseNo, courseDescription, courseRosterLink) =>  `<div class="details-result">
                                                                                                    <div class="big-card-fill"></div>
                                                                                                    <div class="basic-info">
                                                                                                        <div>
                                                                                                            <span class="card-sub1">`+ subject + `</span>
                                                                                                            <span class="card-sub2">` + courseNo + `</span>
                                                                                                        </div>
                                                                                                        <div>
                                                                                                            <p class="card-name">` + courseName + `</span>
                                                                                                        </div>
                                                                                                        <div class="description">
                                                                                                            <p class="course-description">`
                                                                                                                + courseDescription +
                                                                                                            `</p>
                                                                                                            <div class="fill button">Add</div>
                                                                                                            <a href="` + courseRosterLink + `" class="course-url" target="_blank">Read more 🡢</a>
                                                                                                        </div>
                                                                                                    </div>
                                                                                                    </div>
                                                                                                    `

// tag.innerHTML = createMiniCardTag("Poop", "DN", "21");
// tag2.innerHTML = createMiniCardTag("Poop", "DN", "21");
// tag3.innerHTML = createMiniCardTag("Poop", "DN", "21");

// const element = document.getElementById("course-results");
// element.appendChild(tag);
// element.appendChild(tag2);
// element.appendChild(tag3);

// const bigCard = document.getElementById("details");
// const newFatCard = createBigCardTag("Poop", "DN", "21", `Hello hello hello hellohello hello hellohello hello hellohello hello hellohello hello hellohello hello hellohello hello hellohello hello hello`, "https://www.youtube.com/watch?v=vFTnbvXraBo");

// bigCard.innerHTML = newFatCard;

// console.log("Package delivered");
