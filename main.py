import requests as req
import json

# main orchestrator of the function
def main():
    url = "https://ipapi.co/json"
    response = callApiEndpoint(url)
    ip = city = region = country = tz = ""
    if response.status_code == 200:
       try:
        jsonDict = parseJson(response.text)
        ip = extract("ip",jsonDict)
        city, region, country, tz = extractLocation(jsonDict)
       except:
           raise Exception("something")
       finally:
          print("IP : {}, \nCity : {},\nRegion : {},\nCountry : {},\nTimeone : {}".format(ip, city, region, country, tz))
    else:
       print("Response Code is {} for http request to {}".format(response.status_code, url))


# http get method on the url passed as parameter
def callApiEndpoint(url):
    response = req.get(url)
    return response


# converts json string into python dictionary object
def parseJson(text):
    parsed = dict
    try:
       parsed = json.loads(text)
    except:
       raise("Error while parsing text to python dict object")
    finally:
        return parsed


# gets value for the key from dict
def extract(key, dictionary):
   value = ""
   try:
    value = dictionary[key]
   except:
    raise Exception("Error while fetching {} from available keys {}".format(key, dictionary.key()))
   finally:
      return value
   
def extractLocation(jsonDict):
    city, region, country, tz = [ extract("city", jsonDict), extract("region", jsonDict), extract("country", jsonDict), extract("timezone", jsonDict)]
    return [city, region, country, tz]

main()