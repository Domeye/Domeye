import requestTry from "@/network/requestTry";

export const getTry = (search) => {
	return requestTry({
		method: 'post',
		url: 'try',
		data: {
			input_search: search,
		}
	})
}
