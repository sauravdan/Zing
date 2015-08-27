from flask import *
import urllib2
import json
import IP2Location
import HTMLParser

app = Flask(__name__)
@app.route('/')
def search():
	#my_ip=jsonify({'ip': request.environ['REMOTE_ADDR']})
	ip=str(request.environ['REMOTE_ADDR'])
	#return ip
	IP = IP2Location.IP2Location()
	IP.open("/home/prakash/git/ip2location-python-7.0.0/data/IP-COUNTRY.BIN")
	rec=IP.get_all(ip)
	#query=rec.country_long
	#queryIP = IP2Location.IP2Location()
	#query=query.replace(' ','%20')
	query='Delhi'
	final_url = ('https://ajax.googleapis.com/ajax/services/search/news?v=1.0&q='+query+'&userip=INSERT-USER-IP')
	json_obj=urllib2.urlopen(final_url)
	data=json.load(json_obj)
	for news1 in data['responseData']['results']:
		news1['titleNoFormatting']= HTMLParser.HTMLParser().unescape(news1['titleNoFormatting'])
		for news2 in news1['relatedStories']:
			news2['titleNoFormatting']=HTMLParser.HTMLParser().unescape(news2['titleNoFormatting'])
	return render_template('b.html',data=data)
	
@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.environ['REMOTE_ADDR']}), 200
    
d={}

@app.route('/result',  methods=['POST'])
def home():
	query = request.form['search']
	query=query.replace(' ','%20')
	#url='https://api.angel.co/1/search?query='
	final_url = ('https://ajax.googleapis.com/ajax/services/search/news?v=1.0&q='+query+'&userip=INSERT-USER-IP')
	#final_url=url+quer
	json_obj=urllib2.urlopen(final_url)
	data=json.load(json_obj)
	
	for news1 in data['responseData']['results']:
		news1['titleNoFormatting']= HTMLParser.HTMLParser().unescape(news1['titleNoFormatting'])
	
	return render_template('a.html',data=data)
	

				
        #json_list=[]
        #for i in range(1,5):
            #url1='https://api.angel.co/1/jobs?page='+str(i)
            #json_obj1=urllib2.urlopen(url1)
            #data1=json.load(json_obj1)
            #json_list.append(data1)
        dlist=[]
        for job in data:
            i=0
            for job1 in json_list:
                for job2 in job1['jobs']:
                    if str(job['id']) in job2['angellist_url']:
                        d['id']=job2['id']
                        d['title']=job2['title']
                        d['description']=job2['description']
                        dlist.append(d)
            continue  


	#for job in data:
        #	if job['type']=='Startup':                                   #display an error message if type is not found
	#		url1='https://api.angel.co/1/startups/'
	#		job_id=job['id']
	#		final_url1=url1+str(job_id)+'/jobs'
	#		json_obj1=urllib2.urlopen(final_url1)
	#		data1=json.load(json_obj1)
			
			
			
	
if __name__=="__main__":
    app.run(debug=True)
