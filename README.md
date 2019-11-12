# News Unchained

News Unchained is a Google Chrome extension that uses Natural Language Processing (NLP) to determine levels of sentiment in a body of text. By understanding the levels of sentiment applied in a given text and using knowledge from research, portions of text can be omitted from a web domain activating the elimination of bias. With more objectivity, the reader can formulate opinions for themselves without being chained to subjectivity.

**HackUTD VI 2019**

*Developed by: Nick Baker, Ethan Benavides, Bryant Hou, Kendra Huang*

## Installation
---
Use the package [pip] to install: Google Cloud Language,
                                  Google Cloud Language Enums,
                                  Google Cloud Language Types,
                                  Google API Client Types.
                                  
Use Google Chrome extension to install News Unchained

## Justification of Prediction Model
Our subjectivity detection algorithm uses two main assertions of natural language: 

  1. A more polarized sentiment value increases the probability that the selected sentence is subjective (Palshikar, 2016). 

  2. The number of adjectives in the sentence has a positive correlation with the subjectivity of said sentence (Wiebe et al., 1999), (Hatzivassiloglou and Wiebe, 2000).

The first is an established theory that most current subjectivity classification software is based on (Liu, 2010). To increase accuracy and provide another quantifiable measure, we have also included the ratio of adjectives to the total number of words in a sentence as a determinant. Utilizing the Google Cloud - Natural Language API, we are able to leverage these theories in analyzing text for subjectivity/objectivity. Google’s API allows us to analyze the sentiment and verb frequency sentence by sentence, creating a statistical representation of the sentence that allows us to predict subjectivity. If given more time, we would base the sentiment and verb to word count ratio scores on control texts, increasing the accuracy of our model.

The Python script has the ability to analyze multiple text files in sequence, allowing for the automated analysis of many/large texts. File name and location must be updated in the source code. 

Future work will include testing to increase prediction accuracy, creating independent models to reduce bias and increase efficiency, and research into new predictive factors, such as tense or presence of strongly subjective words. 


## Usage
---
Format Type: Strike Through
             Highlight
             
## Contributing
---
Pull requests are welcome. For major changes, please address the primary developers first one what you would like to change.

## License
---
[MIT]

## Acknowledgments
---
Special thanks to developers Nicholas Baker, Ethan Benavides, Bryant Hou, and Kendra Huang.

## References
---
Hong Yu and Vasileios Hatzivassiloglou (2003):
  For answering opinion questions, separating facts from opinions, and identfying the polarity of opinion sentences.
  Proc. Conf. on Empirical mothods in natural language processing (EMNLP), pages 129-136.

Janyce M. Wiebe, Rebecca F. Bruce, and Thomas P. O'Hara. (1999):
  Development and use of a gold standard data set for subjectivity classifications.
  Proc. 37th annual meeting of the Association for Computational Linguistics, pages 246-253.
  
Bing Liu. (2010):
  Sentiment analysis and subjectivity.
  Handbook of natural language processing, vol. 2, pages 627-666.
  
Palshikar, Girish & Apte, Manoj & Pandita, Deepak & Singh, Vikram. (2016):
  Learning to Identify Subjective Sentences
