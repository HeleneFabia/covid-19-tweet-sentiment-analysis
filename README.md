# COVID-19 Tweet Sentiment Analysis

In this project I use [tweets about COVID-19](https://www.kaggle.com/datatattle/covid-19-nlp-text-classification) in order to perform Sentiment Analysis on them. The main goal of this project to become more familiar with Natural Language Processing.

<p align="center">
  <img width="250" height="250" src="https://github.com/HeleneFabia/covid-19-tweet-sentiment-analysis/blob/master/images/twitter-3000965_960_720.png">
</p>

***


#### Training

After running several experiments, training a LSTM model (see below) with learning_rate=0.001, dropout=0.3 for 20 epochs yielded the best results on the validation set.

<p align="left">
  <img width="500" height="140" src="https://github.com/HeleneFabia/covid-19-tweet-sentiment-analysis/blob/master/images/lstm_architecture.png">
</p>

The learning curves of the loss (Binary Cross-Entropy Loss) and accuracy can be seen in the following plots:

<p align="left">
  <img width="550" height="400" src="https://github.com/HeleneFabia/covid-19-tweet-sentiment-analysis/blob/master/images/loss_curve.png">
</p>

<p align="left">
  <img width="550" height="400" src="https://github.com/HeleneFabia/covid-19-tweet-sentiment-analysis/blob/master/images/acc_curve.png">
</p>

#### Testing

The model achieved a test accuracy of 0.8866. When having a look at the confusion matrix, it can be seen that there are many False Positives, so negative tweets that were predicted as positive.  

<p align="left">
  <img width="300" height="300" src="https://github.com/HeleneFabia/covid-19-tweet-sentiment-analysis/blob/master/images/confusion_matrix.png">
</p>

***

Please view my notebooks for more details!
- [Sentiment Analysis with LSTM model](https://github.com/HeleneFabia/covid-19-tweet-sentiment-analysis/blob/master/covid_19_tweet_lstm.ipynb)
- [Sentiment Analysis with BERT model](https://github.com/HeleneFabia/covid-19-tweet-sentiment-analysis/blob/master/covid-19-tweet-bert.ipynb)
- [EDA](https://github.com/HeleneFabia/covid-19-tweet-sentiment-analysis/blob/master/covid-19-tweet-eda.ipynb) 

