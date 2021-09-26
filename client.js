import axios from "axios";


console.log('yup')

const getCourse = async (string) => {
	const strUp = string.toUpperCase()
	const numIdx = strUp.search(/\d/)
	const course = strUp.slice(0, numIdx)
	const number = strUp.slice(numIdx)

	const resp = await axios({
		method: 'get',
		baseURL: 'http://localhost:5000/api/courses/',
		url: `${course}/${number}`
	})
	return resp.data
}

/*Steps:

1) get: course2careerapi.herokuapp.com/api/courses/<LETTERS>/<NUMBERS>

2) get: course2careerapi.herokuapp.com/api/jobs/<location>/<[title+description Keywords]>

3) get: /api/jobs/Ithaca/<subject>/<course_id>

*/