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
GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""
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




main()
