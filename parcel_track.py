import requests
import json
import csv

def load_parcels():
    temp_list = []
    with open('parcels.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            temp_list.append({'number' : row[0].split(",")[0],'info' : row[0].split(",")[1]})
    return temp_list
            

def track(parcel):
    tr_id = parcel['number']
    info = parcel['info']
    print("Parcel informations: {}".format(info))
    print("Tracking code: {} \n".format(tr_id)) 
  
    req = requests.post('https://www.elta-courier.gr/track.php', data = {'number':tr_id}) 
    
    if req.status_code == 200:
        json_response = json.loads(req.content)
        if json_response['status'] == 1 and json_response['result'][tr_id]['status'] == 1 :
            
            for i,packages in enumerate(json_response['result'][tr_id]['result']):                
                print("Message: {} \n Date: {} Time: {} \n Place {}\n".format(i+1,packages['date'],packages['time'],packages['place']))
                
        else:
            print("Not found tracking number")
    else:
        print("Problem with connection")
    print('----------------------------------------------')


if __name__ == '__main__':
    print('----------------------------------------------')
    print('Tracking parcel from ELTA')
    print('----------------------------------------------')
    parcel_list = load_parcels()
    for parcel in parcel_list:
        track(parcel)

