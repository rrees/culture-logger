from markdown_it import MarkdownIt

rating_map = {
	1: u'\u2605',
	2: u'\u2605\u2605',
	3: u'\u2605\u2605\u2605',
	4: u'\u2605\u2605\u2605\u2605',
	5: u'\u2605\u2605\u2605\u2605\u2605',
}

def stars(rating):
	return rating_map.get(rating, '')

md = MarkdownIt()

def markdown(content):
	return md.render(content)

custom_filters = {
	'stars': stars,
	'markdown': markdown,
}