from flask import Flask
#from flask import request
app=Flask(__name__)


@app.route('/')
def index():
	#name=request.args.get('name',name)
	return "Hello from Bleza"

app.run(debug=True, port=8000, host='0.0.0.0')