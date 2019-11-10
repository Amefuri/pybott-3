richdata = {
  "size": {
    "width": 2500,
    "height": 1686
  },
  "selected": True,
  "name": "Rich Menu 1",
  "chatBarText": "Bulletin",
  "areas": [
    {
      "bounds": {
        "x": 0,
        "y": 0,
        "width": 2500,
        "height": 924
      },
      "action": {
        "type": "message",
        "text": "แปลข้อความ"
      }
    },
    {
      "bounds": {
        "x": 10,
        "y": 937,
        "width": 793,
        "height": 730
      },
      "action": {
        "type": "uri",
        "uri": "https://en.wikipedia.org/wiki/France"
      }
    },
    {
      "bounds": {
        "x": 808,
        "y": 932,
        "width": 856,
        "height": 730
      },
      "action": {
        "type": "message",
        "text": "https://en.wikipedia.org/wiki/France"
      }
    },
    {
      "bounds": {
        "x": 1693,
        "y": 946,
        "width": 784,
        "height": 702
      },
      "action": {
        "type": "message",
        "text": "https://en.wikipedia.org/wiki/France"
      }
    }
  ]
}

channel_access_token = "SYR/G9r+UQ/7iN73OIrvu1875aJZ8SEj225JyEXfPpwA0CFY1q3lD4u5syGqJsXxYSDWF7i6DXBIS7/8U+zZc+mGLlRswitN28R0isFWJ2ZD8m4ychCTjVS2L1eK2IU72Z/a/8Fi4wX4M4hE4/9wMAdB04t89/1O/w1cDnyilFU="

import json

import requests



def RegisRich(Rich_json,channel_access_token):

    url = 'https://api.line.me/v2/bot/richmenu'

    Rich_json = json.dumps(Rich_json)

    Authorization = 'Bearer {}'.format(channel_access_token)


    headers = {'Content-Type': 'application/json; charset=UTF-8',
    'Authorization': Authorization}

    response = requests.post(url,headers = headers , data = Rich_json)

    print(str(response.json()['richMenuId']))

    return str(response.json()['richMenuId'])

def CreateRichMenu(ImageFilePath,Rich_json,channel_access_token):


    richId = RegisRich(Rich_json = Rich_json,channel_access_token = channel_access_token)

    url = ' https://api.line.me/v2/bot/richmenu/{}/content'.format(richId)

    Authorization = 'Bearer {}'.format(channel_access_token)

    headers = {'Content-Type': 'image/jpeg',
    'Authorization': Authorization}

    img = open(ImageFilePath,'rb').read()

    response = requests.post(url,headers = headers , data = img)

    print(response.json())



CreateRichMenu(ImageFilePath='tran.jpg',Rich_json=richdata,channel_access_token=channel_access_token)