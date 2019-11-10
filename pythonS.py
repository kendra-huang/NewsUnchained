#!/usr/bin/python
import argparse
import json
import sys

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

import googleapiclient.discovery


textFiles = [r"test2.txt"]
lister = []



DIALOGFLOW_PROJECT_ID = 'hackutd-258605'
DIALOGFLOW_LANGUAGE_CODE = 'en-US'
GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""{
  "type": "service_account",
  "project_id": "hackutd-258605",
  "private_key_id": "e0e3849fcaa749d6cf44e1765bbe4bde57296559",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCpaEhsK8aIpA8G\n8nGTTVoW9ZBWQtDXgEX9AkinqB9GVWiihk0PXpJ1Qee/sHPlAbRxT9RZccrtyyaD\ngFqIaKz9bP9sAeH1gEvLEjjtbH4VeGEq0Lsr6Fw1MicHbn3jPusUJUlLJiy0UYVV\nB1EobFPZTIiU9sv4pXiZXDfmeX7X5qS29YNEzqSQZfvlyhDBxbdexterJLRs1Rih\nbuCcTiOXT0eSexL37SqkPjgKgeQP8qNK996i+n5EKJzilElYKgAQeHhfgOpY+Cb2\nOadB12WH6kSXzvpJTzv71rRAcklv2jXJwYw33xIbkmNRekcWA4lKEkJt7e06LoWO\nN+2HRbLpAgMBAAECggEAUhoaT2J/26U3KzTA2pT4fnwQsd27/VVLli1PLQIL9jha\nd7oDCtnYvT9to7dO08QZwXjg/2Bo6woz5jOErOueO0xiFeRrsGG3WfnA4UBdcuZe\noTN8IvGADr/5rl5cYJATujW/6c3ciJ+hsO3U5XRqxruSzi8195Gqexj4dpiXYua3\nkRIlvxGJuaB8Qdf+9D+rlxhRw3aTB5wIW81x6r3rtlMHE2nqS/vdlXmXsDJWzgx7\nN+m97bF1YSmCSnagZoaBcnucx1E1x49OFkyDZPx77zAL3LPpEOC30LHKYvqGdwAN\n6rtTP3+Pc3PEbXa8NAtBWJQCc768T96E4ks7Pj5oyQKBgQDs3nzZya0dNgk0EfoZ\nUasLBLCdEoTSGme1jMfq51+ZXWX1xv10IsNKxM0AcfV7ihhtt5aW1FWtekQCuhmZ\neWS2aVU0lAAC8LIgLrMAS46bKUigDYLyYqwsQylIdUwWhSLIivUwlZHv4oonju8B\nDimPsjLcRjybKLKDLLGsp4dy0wKBgQC3FvRPprFT7+/sg3wi/ewGCWxygHEmBifQ\nV7ZnqCJH+LNSnQqTOidEPZbMpGFYD7MHGU/8MX71GgzPQdxVlurAJGm7FzwgrNKc\nZCyb5EeGlpFOCOurAwJ8T0nrnjtaSRQDEsfs1digqLeSCjAFgzirCthMSNuaQ7Dw\n4mLLGzZV0wKBgQCdeHgGDZaB8feCX2UmSe3tIEwN0E7uotFJl/McTn92pOnw0D6V\nY7rzTQyAfEJXxAHjhwac9UKUVtE6AuCb8GEtB6+2iaHMUpoI3SLxUknXC0YV6YWh\ngEm4D1o1qo1P92idbAv/JaBkmvV/wP1RdUnaFvzLBgKqoA61OBRSlPluMwKBgEkQ\nLvSuN6ugX2VJ3zrzi8Go9w8GdKDQ6gh5SEA7V1rTQ3RfWP4BwfO4hDosCvCiazYV\nAtdIRTq4Z4454RyCujFtFohjsEn1zaI9U5PuWCC8a0Xxx2IaNF65IW2WWmcgLI1B\nbGj1uZn7Wi48RIeeovmWvVRL6t63zp+CKByXQmqjAoGBAOYbqhGrrBGzXL8TAPMu\nN2Jm1X6M8+2zn3cjNRHWUnTeRNbWrdPuZO/IrU6+DQE4Wc7YETwL9KM2bqF/FywR\nGcoCZ7yDVbwcN+yKW+UWBqGdVSFarUau/ZlLJNU0tQnN0/DoVYsMdqcS/Q3sGDdh\nlmawd1WSxHdABw6Z6/UXP4f6\n-----END PRIVATE KEY-----\n",
  "client_email": "self-190@hackutd-258605.iam.gserviceaccount.com",
  "client_id": "110064377340067738175",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/self-190%40hackutd-258605.iam.gserviceaccount.com"
}"""

def analyzer(content1):
    credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS
    client = language.LanguageServiceClient()

    document = types.Document(
        content=content1,
        type=enums.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(document=document)
    magnitude = annotations.document_sentiment.magnitude
    for index, sentence in enumerate(annotations.sentences):
        sentence_sentiment = sentence.sentiment.score
        #print('Sentence {} has a sentiment score of {}'.format(
            #index, sentence_sentiment))
        if sentence_sentiment > .8 or sentence_sentiment < 0:
            #print("This sentence text may be objective:" + str(sentence.text))
            lister.append(str(sentence.text))
            print("sentiment add")



        body = {
            'document': {
                'type': 'PLAIN_TEXT',
                'content': str(sentence.text),
            },
            'encoding_type': 'UTF8'
        }

        service = googleapiclient.discovery.build('language', 'v1')

        request = service.documents().analyzeSyntax(body=body)
        response = request.execute()
        response = str(response)
        #print(response)
        adjRatio = response.count("ADJ") / response.count("text")
        print(adjRatio)
        if adjRatio > 0.1 and str(sentence.text) not in lister:
            lister.append(str(sentence.text))
            print("ratio add")


    return lister

def main():
    for i in textFiles:
        with open (i, "r") as myfile:
            text = myfile.read().replace('\n', '')
            lister = analyzer(text)
            f = open("results.txt", "w+")
            f.write(str(lister))




main()
