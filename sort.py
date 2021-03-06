from flask import *
import urllib2
import json
import IP2Location

app = Flask(__name__)
@app.route('/')
def search():
	#my_ip=jsonify({'ip': request.environ['REMOTE_ADDR']})
	ip=str(request.environ['REMOTE_ADDR'])
	#return ip
	IP = IP2Location.IP2Location()
	IP.open("/home/prakash/git/ip2location-python-7.0.0/data/IP-COUNTRY.BIN")
	rec=IP.get_all(ip)
	query=rec.country_long
	queryIP = IP2Location.IP2Location()
	#query=query.replace(' ','%20')
	final_url = ('https://ajax.googleapis.com/ajax/services/search/news?v=1.0&q='+query+'&userip=INSERT-USER-IP')
	json_obj=urllib2.urlopen(final_url)
	data=json.load(json_obj)
	return render_template('b.html',data=data)
	
d={}
dlist=[]
ddlist=[]
@app.route('/result',  methods=['POST'])
def home():
	query = request.form['search']
	query=query.replace(' ','%20')
	final_url = ('https://ajax.googleapis.com/ajax/services/search/news?v=1.0&q='+query+'&userip=INSERT-USER-IP')
	#final_url=url+quer
	json_obj=urllib2.urlopen(final_url)
	data=json.load(json_obj)
	for news1 in data['responseData']['results']:
		url='https://api.facebook.com/method/fql.query?query=select%20%20like_count%20from%20link_stat%20where%20url=%22'+news1['unescapedUrl']+'%22%20&format=json'
		
		d['unescapedUrl']=news1['unescapedUrl']
		d['titleNoFormatting']=news1['titleNoFormatting']
		d['publisher']=news1['publisher']
	
	return render_template('a.html',data=data)

if __name__=="__main__":
    app.run(debug=True)
