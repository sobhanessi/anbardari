
from flask import Flask , request, render_template , url_for , escape , flash , redirect

app = Flask(__name__)

app.secret_key = 'yadam bashe ye chizi be onvane secret_key set konam'


@app.route('/')
def index():
	
	return render_template('loginmain.html')	

#@app.route('/main/')

#def main(username,department):
	
# inja bayad bar asase usernam i ke dare va 
# department i ke dare render template konam ye chizi ro vasash

	#return render_template()

# too tamame safahat yadam bashe ye dokme bezaram
# baraye logout ke session e shoon ro bebandam va az <a> estefade
# konam baraye in kar
	
#@app.route('/logout/')
#def logout():
	
	#session.pop('username',none)
	
	#return redirect(url_for('index'))




@app.route('/loginmain' , methods = ['post','get'])

def loginmain():
	
	
	error = None
	
	
	
	
	
	# in kar ro moghei bayad anjam bedam ke datash ro ba
	# sql check karde basham va baad in karo anjam bedam
	# ke inja mitoonam ye if o else ham benevisam baraye
	# flash kardan tebghe zir:
	
	
	if (request.form['username'] != 'admin' or request.form['password'] != 'admin'):
	#if username in db:
		#if password in db:
			#session['username'] = request.form['username']
			
			#baadesh bar assase chizi ke sql behem barmigardoone ye doone template 
			#barashoon dorost konam ta kare zir ro anjam bedam
		error = 'ridi baba '
	else:		
		
		flash("nnnnnnnnaaaaaaaaaaaaaaaaaaridiiiiiiiiiiiiiiiiiiiiiiiiii")	
		return redirect(url_for('index'))
	return render_template('loginamin.html' ,error = error)		 
		#else:
			#flash(your password is incorrect)
			#return redirect(url_for('index'))
	#else:
		#flash(your username is incorrect)
		#return redirect(url_for('index'))
		

if __name__=='__main__':
	app.run(debug = True)

app.debug = True
app.run(debug = True)
