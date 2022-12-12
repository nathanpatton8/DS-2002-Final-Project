#!/usr/bin/env python
# coding: utf-8

# # Project 2

# ## Instructions
# Overview:
# The goal of the second data project, building upon the concepts this semester, is to further demonstrate
# (1) an understanding of and (2) competence creating and implementing basic data science systems such
# as pipelines, scripts, data transformations, databases, and cloud services. Submit your project via Collab
# and past a link to your GitHub Repo. You will utilize public datasets, Python, Pandas, and Mongo to
# accomplish your project.
# 
# You may work in groups – in your submission and in your code comments, please indicate you
# group members and their compute ID’s.
# 
# Objective
# 
# You will use Netflix TV Shows and Movies data to create an ETL process to Extract, Transform and Load
# multiple datasets from CVS Files into a MongoDB Database. After that, you’ll use that data source to
# create a simple chatbot which allows the user to as a variety of questions to the chatbot. You DO NOT
# need to make this bot run in Discord or Twitter, but rather at the local machine.
# 
# Your bot will need to answer the questions (taking note to use various forms of ways to ask the question)
# in a human type of form.
# 1. What were the top 5 shows on Netflix 2 years ago? Show me the top 5 shows on Netflix 2 years
# ago. Show me the top 5 shows on Netflix two years ago.
# 2. What was the top movie on Netflix in 2020?
# 3. How long was the best movie on Netflix last year? What was the release year of that movie?
# 
# These are just *sample* questions. You need to allow you bot to ask 10 different categories/types of
# questions. They are up to you on which questions, but the bot needs to tell the user what those question
# categories that it can answer. Like: Top movies by year, top X movies / shows by year. Genre of
# Movie/Show of the top Movie/Show…# of seasons of top shows…etc. Star(s) of the top show/movie.
# You’ll need to use the user response to form a query for your Mongo Dataset.
# 
# Your data sources will be the following.
# https://www.kaggle.com/datasets/thedevastator/the-ultimate-netflix-tv-shows-and-movies-dataset
# 
# Part 1 will be to extract these data sources into one Pandas. Note to only extract the data that supports
# the types of questions you want. This is the Extract and Transform sections. For example, if you choose
# not to allow users to ask about the number of seasons, do not extract that into your new data set.
# 
# Part 2 will be to Load that into a MongoDB. You code will create a new MongoDB and load the data into a
# Mongo Database
# 
# Part 3 will be to run your bot to answer your questions. The bot will tell the user with that types of
# questions they can ask when they enter “help”, and when the bot starts. If the user asks a question that
# isn’t in the correct form, or isn’t in the pattern, it suggests the kinds of questions it can answer.
# 
# You will turn in:
# 1) One a Python program that extracts and loads the data into a Mongo DB, which you create in the
# Python program. I should be able to execute your code and it create the local MongoDB File from
# the source CSVs. You can assume I have the CSVs locally on my computer.
# 2) One Python program that is the chatbot which will interact with the user and the MongoDB
# program.
# 
# Grading:
# 1. Programs successfully builds with no errors – 5
# 2. Functionally meets the Extract and Transform requirements – 10
#     a. Extract multiple CSVs into a Pandas Data frame
#     b. Only Transform the Data that you need
# 3. Load data into a Mongo Database created by your Python Program – 10
# 4. Your bot will be able to answer questions (10 types of questions asked in various forms) – 15
# 5. Creativity and Innovation – 3 (think of this as extra)

# ### Questions for Bot
# 1)What were the top 3 shows on Netflix 5 years ago?
# What were the top three shows on Netflix five years ago?
# Show me the top three shows on Netflix five years ago
# Show me the top 3 shwos on Netflix 5 years ago
# 
# 2)What was the top movie in 2019?
# Show me the top movie in 2019
# 
# 3)What was the top show in 2021?
# Show me the top show in 2021
# 
# 4)What were the worst movie in 2018?
# Show me the worst movie in 2018
# 
# 5)What was the worst show in 2020?
# Show me the worst show in 2020
# 
# 6)What is the genre of the best show ever?
# Show me the genre of the best show ever
# 
# 7)What is the genre of the best movie ever?
# Show me the genre of the best movie ever
# 
# 8)What was the score of the worst show ever?
# Show me the score of the worst show ever
# 
# 9)What was the score of the worst movie ever?
# Show me the score of the worst movie ever
# 
# 10)What is the duration of Top Gun?
# How long is Top Gun?
# 
# 11)Where was the main production for Breaking Bad?
# 

# ## Code

# In[1]:


# Import Statements
import pandas as pd


# In[10]:


# Loading in the local csv files
BestShowsByYear = pd.read_csv(r'C:\Users\natha\Downloads\Best Show by Year Netflix.csv')
BestShows = pd.read_csv(r'C:\Users\natha\Downloads\Best Shows Netflix.csv')
BestMoviesByYear = pd.read_csv(r'C:\Users\natha\Downloads\Best Movie by Year Netflix.csv')
BestMovies = pd.read_csv(r'C:\Users\natha\Downloads\Best Movies Netflix.csv')
rawTitles = pd.read_csv(r'C:\Users\natha\Downloads\raw_titles.csv')
rawCredits = pd.read_csv(r'C:\Users\natha\Downloads\raw_credits.csv')


# In[11]:


# Displaying BestShowsByYear
BestShowsByYear


# In[12]:


# Displaying BestShows
BestShows


# In[13]:


# Displaying BestMoviesByYear
BestMoviesByYear


# In[14]:


# Displaying BestMovies
BestMovies


# In[15]:


# Displaying rawTitles
rawTitles


# In[16]:


# Displaying rawCredits
rawCredits


# In[46]:


# Creating Data Frame df containing the only the data need to answer the questions that the Bot can be asked
df = {
    'Best_Movie_Titles': BestMovies.loc[:,"TITLE"],
    'Best_Movie_Genres': BestMovies.loc[:,"MAIN_GENRE"],
    'Best_Movie_Scores': BestMovies.loc[:,"SCORE"],
    'Best_Show_Titles': BestShows.loc[:,"TITLE"],
    'Best_Show_Genres': BestShows.loc[:,"MAIN_GENRE"],
    'Best_Movie_Titles_by_Year': BestMoviesByYear.loc[:,"TITLE"],
    'Best_Movie_Release_Year': BestMoviesByYear.loc[:,"RELEASE_YEAR"],
    'Best_Show_Titles_by_Year': BestShowsByYear.loc[:,"TITLE"],
    'Best_Show_Relase_Year': BestShowsByYear.loc[:,"RELEASE_YEAR"]}
df = pd.DataFrame(df, columns = ['Best_Movie_Titles','Best_Movie_Genres','Best_Movie_Scores','Best_Show_Titles',
                                 'Best_Show_Genres','Best_Movie_Titles_by_Year','Best_Movie_Release_Year','Best_Show_Titles_by_Year',
                                 'Best_Show_Relase_Year'])
df


# In[47]:


# Converting df to a CSV and writing it to a local file (Directions: Click "Run" to convert the DataFrame to a CSV and save that as a local file called "out.csv")
df.to_csv('out.csv', index=False) 

