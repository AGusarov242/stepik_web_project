def wsgi(environ, start_response):
	status = '200 OK'
	headers = [('Content-Type', 'text/plain')]
	data = environ['QUERY_STRING'].split('&')
	out = '\n'.join(data).encode('utf-8')
	start_responce(status, headers)
	return [out]