console.log('yup')

const getCourse = async (string) => {
	const strUp = string.toUpperCase()
	const numIdx = strUp.search(/\d/)
	const course = strUp.slice(0, numIdx)
	const number = strUp.slice(numIdx)

	const resp = await fetch(`http://course2careerapi.herokuapp.com/api/jobs/Ithaca/${course}/${number}`)
	.then(resp => resp.json())
	return resp
}

document.onload = () => {
	const searchButton = document.getElementById('searchButton')
	searchButton.addEventListener('click', () => {
		console.log('FOCK')
		const searchFieldValue = document.getElementById('courseSearchField').value
		getCourse(searchFieldValue)
	})
}
/*Steps:

1) get: course2careerapi.herokuapp.com/api/courses/<LETTERS>/<NUMBERS>

2) get: course2careerapi.herokuapp.com/api/jobs/<location>/<[title+description Keywords]>

3) get: /api/jobs/Ithaca/<subject>/<course_id>

*/