# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 13:04:34 2019

@author: TobieMartinAlexander
"""
#The code examples on this tab use the client library that is provided for Python.

#Installation
pip install --upgrade "watson-developer-cloud>=2.8.0"

#SDK managing the IAM token. Replace {apikey}, {version} and {url}.
from watson_developer_cloud import ToneAnalyzerV3

tone_analyzer = ToneAnalyzerV3(
    version='2017-11-07',
    iam_apikey='NnnCc4TAZqB9GhNinm6t1xk3LmqOUhXPBhUn_NQS8q-F',
    url="https://gateway.watsonplatform.net/discovery/api"
)

#Basic authentication. Replace {username}, {password}, `, and{url}`.

from watson_developer_cloud import ToneAnalyzerV3

tone_analyzer = ToneAnalyzerV3(
    version='2017-11-07',
    username='David Gitonga',
    password='GettyGitonga',
    url='https://twitter.com/GettyGitonga'
)

#Default URL

https://gateway.watsonplatform.net/tone-analyzer/api

#Examples for the Washington DC location in the constructor and after instantiation

tone_analyzer = ToneAnalyzerV3(
    version='2017-11-07',
    iam_apikey='NnnCc4TAZqB9GhNinm6t1xk3LmqOUhXPBhUn_NQS8q-F',
    url='https://gateway-wdc.watsonplatform.net/tone-analyzer/api'
)

#or

tone_analyzer.set_url('https://gateway-wdc.watsonplatform.net/tone-analyzer/api')

#Example error handling

from watson_developer_cloud import WatsonApiException
try:
    # Invoke a Tone Analyzer method
except WatsonApiException as ex:
    print "Method failed with status code " + str(ex.code) + ": " + ex.message

# Example header parameter in a request

response = tone_analyzer.methodName(
    parameters,
    headers = {
        'Custom-Header': '{header_value}'
    })
 #Example request to access response headers

tone_analyzer.set_detailed_response(True)
response = tone_analyzer.methodName(parameters)
// Access response from methodName
print(json.dumps(response.get_result(), indent=2))
// Access information in response headers
print(response.get_headers())
// Access HTTP response status
print(response.get_status_code())

#Example request

tone_analyzer.set_default_headers({'x-watson-learning-opt-out': "true"})

tone(self, tone_input, content_type=None, sentences=None, tones=None, content_language=None, accept_language=None, **kwargs)

# Example request

import json
from watson_developer_cloud import ToneAnalyzerV3

tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    iam_apikey='NnnCc4TAZqB9GhNinm6t1xk3LmqOUhXPBhUn_NQS8q-F',
    url='https://cloud.ibm.com/iam#/apikeys'
)

text = 'Team, I know that times are tough! Product '\
    'sales have been disappointing for the past three '\
    'quarters. We have a competitive product, but we '\
    'need to do a better job of selling it!'

tone_analysis = tone_analyzer.tone(
    {'text': text},
    'application/json'
).get_result()
print(json.dumps(tone_analysis, indent=2))

#Example responses

{
  "document_tone": {
    "tones": [
      {
        "score": 0.6165,
        "tone_id": "sadness",
        "tone_name": "Sadness"
      },
      {
        "score": 0.829888,
        "tone_id": "analytical",
        "tone_name": "Analytical"
      }
    ]
  },
  "sentences_tone": [
    {
      "sentence_id": 0,
      "text": "Team, I know that times are tough!",
      "tones": [
        {
          "score": 0.801827,
          "tone_id": "analytical",
          "tone_name": "Analytical"
        }
      ]
    },
    {
      "sentence_id": 1,
      "text": "Product sales have been disappointing for the past three quarters.",
      "tones": [
        {
          "score": 0.771241,
          "tone_id": "sadness",
          "tone_name": "Sadness"
        },
        {
          "score": 0.687768,
          "tone_id": "analytical",
          "tone_name": "Analytical"
        }
      ]
    },
    {
      "sentence_id": 2,
      "text": "We have a competitive product, but we need to do a better job of selling it!",
      "tones": [
        {
          "score": 0.506763,
          "tone_id": "analytical",
          "tone_name": "Analytical"
        }
      ]
    }
  ]
}

Analyze customer engagement tone

tone_chat(self, utterances, content_language=None, accept_language=None, **kwargs)

# Example Request

import json
from watson_developer_cloud import ToneAnalyzerV3

tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    iam_apikey='{apikey}',
    url='{url}'
)

utterances = [
    {
        "text": "Hello, I'm having a problem with your product.",
        "user": "customer"
    },
    {
        "text": "OK, let me know what's going on, please.",
        "user": "agent"
    },
    {
        "text": "Well, nothing is working :(",
        "user": "customer"
    },
    {
        "text": "Sorry to hear that.",
        "user": "agent"
    }
]

utterance_analyses = tone_analyzer.tone_chat(utterances).get_result()
print(json.dumps(utterance_analyses, indent=2))

#Example responses

{
  "utterances_tone": [
    {
      "utterance_id": 0,
      "utterance_text": "Hello, I'm having a problem with your product.",
      "tones": [
        {
          "score": 0.686361,
          "tone_id": "polite",
          "tone_name": "Polite"
        }
      ]
    },
    {
      "utterance_id": 1,
      "utterance_text": "OK, let me know what's going on, please.",
      "tones": [
        {
          "score": 0.92724,
          "tone_id": "polite",
          "tone_name": "Polite"
        }
      ]
    },
    {
      "utterance_id": 2,
      "utterance_text": "Well, nothing is working :(",
      "tones": [
        {
          "score": 0.997795,
          "tone_id": "sad",
          "tone_name": "sad"
        }
      ]
    },
    {
      "utterance_id": 3,
      "utterance_text": "Sorry to hear that.",
      "tones": [
        {
          "score": 0.730982,
          "tone_id": "polite",
          "tone_name": "Polite"
        },
        {
          "score": 0.672499,
          "tone_id": "sympathetic",
          "tone_name": "Sympathetic"
        }
      ]
    }
  ]
}   
    