
def bechdel_test(params):
	param_value = params.get('bechdel_test', None)

	if not param_value:
		return None

	if param_value == "true":
		return True

	return False