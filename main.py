#Import the necessary libraries
import json, unittest, datetime

# Open function to read the three json files

with open("./data-1.json","r") as f:
    jsonData1 = json.load(f)
with open("./data-2.json","r") as f:
    jsonData2 = json.load(f)
with open("./data-result.json","r") as f:
    jsonExpectedResult = json.load(f)

#Convert Json data from format 1 to a unified format

def convertFromFormat1 (jsonObject):

    # Split the Location with "/"
    # IMPLEMENT: Conversion From Type 1

    locationParts=jsonObject['location']. split('/')

#Create new dictionary

    result= {
        'deviceID': jsonObject['deviceID'],#Extract deviceID
        'deviceType': jsonObject['deviceType'],#Extract deviceType
        'timestamp': jsonObject['timestamp'], #Extract timestamp
        'location': {
            'country': locationParts[0],#Extract country 
            'city': locationParts[1], #Extract the city 
            'area': locationParts[2],#Extract the area 
            'factory': locationParts[3],#Extract the factory 
            'section': locationParts[4]#Extract section
        },
        'data': {
            'status': jsonObject['operationStatus'], # copy the opertaionStatus as status
            'temperature': jsonObject['temp'] #copy the temp as temperature
        }
    }

    return result


def convertFromFormat2 (jsonObject):

    # IMPLEMENT: Conversion From Type 1
    # Convert ISO timestamp to milliseconds

    date= datetime.datetime.strptime(jsonObject['timestamp'],#Extract the ISO timestamp
                                     '%Y-%m-%dT%H:%M:%S.%fZ')#ISO timestamp format
    timestamp=round((date-datetime.datetime(1970, 1, 1)).total_seconds()*1000)# convert to milliseconds

    #new dictionary
    result= {
        'deviceID': jsonObject['device']['id'],#Extract 
        'deviceType': jsonObject['device']['type'],#Extract 
        'timestamp': timestamp, 
        'location': {
            'country': jsonObject['country'],#Extract 
            'city': jsonObject['city'], #Extract 
            'area': jsonObject['area'],#Extract 
            'factory': jsonObject['factory'],#Extract 
            'section': jsonObject['section']#Extract 
        },
        'data': jsonObject['data'] 
    }
    return result


def main (jsonObject):

    result = {}

    if (jsonObject.get('device') == None):
        result = convertFromFormat1(jsonObject) 
    else:
        result = convertFromFormat2(jsonObject) 

    return result


class TestSolution(unittest.TestCase):

    def test_sanity(self):


        result = json.loads(json.dumps(jsonExpectedResult))
        self.assertEqual(
            result,
            jsonExpectedResult
        )

    def test_dataType1(self):


        result = main (jsonData1)
        self.assertEqual(
            result,
            jsonExpectedResult,
            'Converting from Type 1 failed'
        )

    def test_dataType2(self):


        result = main (jsonData2)
        self.assertEqual(
            result,
            jsonExpectedResult,
            'Converting from Type 2 failed'
        )

if __name__ == '__main__':

    unittest.main()
