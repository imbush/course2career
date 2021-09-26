const card = (x, y, z) => {
	return `
	<div>
		<div class="course-result">
			<div class="micro-card-fill"></div>
			<div class="basic-info">
				<div>
					<span class="card-sub1">${x}</span>
					<span class="card-sub2">${y}</span>
				</div>
				<div>
					<p class="card-name">${z}</p>
				</div>
			</div>
		</div>
	</div>
	`
}

const detailCard = (v, w, x, y, z) =>  `<div class="details-result">
											<div class="big-card-fill"></div>
											<div class="basic-info">
												<div>
													<span class="card-sub1">`+ v + `</span>
													<span class="card-sub2">` + w + `</span>
												</div>
												<div>
													<p class="card-name">` + x + `</span>
												</div>
												<div class="description">
													<p class="course-description">`
														+ y +
													`</p>
													<div class="fill button">Add</div>
													<a href="` + z + `" class="course-url" target="_blank">Read more 🡢</a>
												</div>
											</div>
											</div>
											`

console.log('yup')
console.log("We have loaded! WOOT!");

myStorage = window.localStorage;

const clearStorage = () => {
	myStorage.clear();
	onLoadUp()}

	const onLoadUp = ()=> {	var arrayOfValues = [];
							for(var i in myStorage){
								if(myStorage.hasOwnProperty(i)){
									arrayOfValues.push(myStorage[i].split(",SPLIT,"));
								}
							}

							console.log(arrayOfValues);
							console.log("Okay??")
							const detailContainer = document.getElementById("details");
							const resultsContainer = document.getElementById("added");

							// resultsContainer.innerHTML="";

							for(_class1=0; _class1<arrayOfValues.length; _class1++) {
								_class=arrayOfValues[_class1]
								console.log(_class[0])
								console.log("Pretty pretty")
								const newCard = card(_class[0], _class[1], _class[2]);
								const newCardDetail = detailCard(_class[0], _class[1], _class[2], _class[3], _class[4]);

								detailContainer.innerHTML = newCardDetail;
								resultsContainer.innerHTML += newCard;
							}
						}
	
	onLoadUp();

// const onLoadUpJobs = async()=> {
// 	var arrayOfValues = [];
// 	for(var i in myStorage){
// 		if(myStorage.hasOwnProperty(i)){
// 			arrayOfValues.push(myStorage[i].split(",SPLIT,"));
// 		}
// 	}
// 	console.log("test")
// 	console.log(arrayOfValues)

// 	for(i=0; i<arrayOfValues.length; i++) {
// 		_class=arrayOfValues[i]

// 		// const dropDown = document.getElementById('dropDownId')
// 		// const dropDownValue = dropDown[dropDown.value].value

// 		const jobs = await fetch(`https://course2careerapi.herokuapp.com/api/jobs/Ithaca/${_class[0]}/${_class[1]}`, {
// 				credentials: 'omit'		
// 			}
// 		)
// 		.then(jobs => jobs.json())
// 		console.log(JSON.stringify(jobs, null, 2))
// 		const jobCard = card(jobs["title"], jobs["locations"], jobs["company"]);
// 		const resultsContainer = document.getElementById("job-results");
// 			resultsContainer.innerHTML += jobCard;
// 	}
// }

// onLoadUpJobs();

const getCourse = async () => {

	const string = document.getElementById('courseSearchField').value
	const strUp = string.toUpperCase()
	const numIdx = strUp.search(/\d/)
	const course = strUp.slice(0, numIdx)
	const number = strUp.slice(numIdx)

	try{ 
		const resp = await fetch(`http://course2careerapi.herokuapp.com/api/courses/${course}/${number}`, {
				credentials: 'omit'		
			}
		)
		.then(resp => resp.json())
		console.log(JSON.stringify(resp, null, 2))
		
		if (resp["error"] == "Course not found") {
			alert("Invalid Course! Ex. CS2112")
		}
		else {
			let classData = [resp["subject"], "SPLIT", resp["catalogNbr"], "SPLIT", resp["titleLong"], "SPLIT", resp["description"], "SPLIT", resp["rosterURL"]]
			myStorage.setItem(resp["titleLong"], classData);
			
			console.log("Printing local storage:")
			console.log(myStorage);

			const newCard = card(resp["subject"], resp["catalogNbr"], resp["titleLong"]);

			const newCardDetail = detailCard(resp["subject"], resp["catalogNbr"], resp["titleLong"], resp["description"], resp["rosterURL"])
			const detailContainer = document.getElementById("details");
			detailContainer.innerHTML = newCardDetail;
			
			const resultsContainer = document.getElementById("added");
			resultsContainer.innerHTML += newCard;

			return resp
			
		}
	}
	catch (error) {
		alert("Invalid Course! Ex. CS2112")
	}
}

const getJobs = async () => {
// 	const course = strUp.slice(0, numIdx)
// 	const number = strUp.slice(numIdx)

	var arrayOfValues = [];
	for(var i in myStorage){
		if(myStorage.hasOwnProperty(i)){
			arrayOfValues.push(myStorage[i].split(",SPLIT,"));
		}
	}
	console.log("test")
	console.log(arrayOfValues)

	for(i=0; i<arrayOfValues.length; i++) {
		_class=arrayOfValues[i]

		// const dropDown = document.getElementById('dropDownId')
		// const dropDownValue = dropDown[dropDown.value].value

		const jobs = await fetch(`https://course2careerapi.herokuapp.com/api/jobs/Ithaca/${_class[0]}/${_class[1]}`, {
				credentials: 'omit'		
			}
		)
		.then(jobs => jobs.json())
		console.log("this is string")
		console.log(JSON.stringify(jobs, null, 2))
		const jobCard = card(jobs["title"], jobs["locations"], jobs["company"]);
		const resultsContainer = document.getElementById("job-results");
			resultsContainer.innerHTML += jobCard;
	}
	return jobs
}

// document.getElementById("courseSearchField")
//     .addEventListener("keyup", function(event) {
//     event.preventDefault();
//     if (event.key === 13) {
//         document.getElementById("searchButton").click();
//     }
// });

document.onload = () => {

	const searchButton = document.getElementById('searchButton')
	searchButton.addEventListener('click', () => {

		console.log('I AM WORKING!')
		getCourse(searchFieldValue)
	})
}