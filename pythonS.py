#!/usr/bin/python
import argparse
import json
import sys

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

import googleapiclient.discovery

import re


textFiles = [r"test2.txt"]
lister = []



DIALOGFLOW_PROJECT_ID = 'hackutd-258605'
DIALOGFLOW_LANGUAGE_CODE = 'en-US'
GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""{
  "type": "service_account",
  "project_id": "hackutd-258605",
  "private_key_id": "436023a481a0a4ed6237a3487c9bda11fb6249f5",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCT/RHUJuTRJxwV\nrjC5n5L/J7yF4higGEeOxkkOpgVUMZPIH2W8QREzWfcq1EYe31kZ2QkU0pf0okG3\nkSw7qmOH/MPqB8L+wZTE6yoSq0xwM3iVdqCt9eTpyj/jn/JERMk+wky7dQQK9SGk\ncmM4OORLotLIvDfi3U9Y01d7n6w7k+Q19Yu47wtnONxKGtIfbPFmEedbk8GO1rg4\n4ZCStf0sWyV75Q/avOma5E1HB4DZaAtrirmT2oDTUmkCaESZL6JpRpFGf8Sh9Wzc\nG8OsevztMxi81SiAaBvzOEH28TIcEKdweEOvEKNvfuyMz5SSutb9WJmmPbHLKQtq\nhh1WnNtBAgMBAAECggEAATc243IqexoIciEDwlISkCkpCbxiYGcaH6ZuNazUVRxL\nBFMSxU8X7VAIDQ9inhP5Sdai0cMSDGy3ESd5PlCiC4waLviMN/WZVzqC67wBxbWE\n7yr8iev3St7mbP3mvcA6PUG1jf3d281RghCOW8TX38tSQX1sMufc117Kriaqm04B\neU4EFEGheq76VyLEeDAb77QSpxvQKYCw0YWGY4dbNmh9qJuICV6IC7yM7q53LqIp\nFooluOzgI9yWRFYcCNfhtakgne4lBdVdtTbjI7VNMH7v5VN7tVYiV0RSfuARU0kf\nOgvTXJni5Pb0LAXBYEe/JNBP8CS5x02wyznjSwUtmQKBgQDOCIcnhaZYCbPaI4d/\n4FWuCLl/BoyOpLsIvCyChtjugqme24pCTSHKLmaAprQll77LaeC6Uipvy1EHjx+x\nUmuqD5WgrlitFmuzplr9A/IDBbOK0TcANBg67Q7X7m+SRDX46WG4Zbf2CsyBAU2m\nuAg1/GglmLhX3//j7ESkJFmA9QKBgQC34NzcT+OnN5QF8sG6kDk0A/Xi6YPgU4kr\nit9rB/FfrOTFLEFTgTHGEwycSHvO4r6TEAYG3KiBqZZkg6LvvQymmwJLeBLrvrVb\nGXpsDz35IP2uGS6N27DEehv1jLtqKggusYK0Gr08BddNbLJ6x3nrqX9iMdHZyS0i\nTVmezjaRnQKBgCjxyOoxxTz5sKRJK0RecKiFU1fLFWPDmOfDfZTy92luzgaj2nYS\nngRv9C7c8jAGWARUpjRg384XuaKm7sVue7bwIewsubKsIfsxtCNUBWRUXbnYmfWQ\nZMBRHAINgF6w74jn2GOs00IyIzH/8E6RhBA2ePv/vaK5AUFqUrnL/32BAoGBAK8A\n/nNYPY0aonD+2E7dkPPmiRFLuk24c6bTZ0wQpTOv85ONSSdWoK6p1qive9Yti7+f\n0nyZam7tnstPVbXiMbYndYmqYCeqvCRWHWPXJd6D/azDHsG4w4ZbyVxscrraAiue\nmo0bndsQnBd+Smf8jhcynKAyVk124NPy1kcEcH8pAoGBAJiTev0qT0TWM6kZ7mqY\n///oEYIqCzD9upKexeOCXC9dvd5qzXbL9JbHmShjjgyZeHfHXMQl2+sH7h4cHuzX\nw9XyU47kePB52sMSOta4Ng3EAtTlMOJtsoWHLcZs1wYNnciE7TN0wN96hsjqBbl+\n7WtjqK2PFZjG2XdI99kGk8l3\n-----END PRIVATE KEY-----\n",
  "client_email": "me-933@hackutd-258605.iam.gserviceaccount.com",
  "client_id": "101723019788941695925",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/me-933%40hackutd-258605.iam.gserviceaccount.com"
}
"""

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

            cleanr = re.compile('<.*?>')
            text = re.sub(cleanr, '', text)

            lister = analyzer(text)
            f = open("results.txt", "w+")
            f.write(str(lister))
            return lister 




main()
