# DS-2002-Final-Project
Group Members: Nathan Patton and Maajid

Overview:
The goal of the second data project, building upon the concepts this semester, is to further demonstrate
(1) an understanding of and (2) competence creating and implementing basic data science systems such
as pipelines, scripts, data transformations, databases, and cloud services. Submit your project via Collab
and past a link to your GitHub Repo. You will utilize public datasets, Python, Pandas, and Mongo to
accomplish your project.

You may work in groups – in your submission and in your code comments, please indicate you
group members and their compute ID’s.

Objective

You will use Netflix TV Shows and Movies data to create an ETL process to Extract, Transform and Load
multiple datasets from CVS Files into a MongoDB Database. After that, you’ll use that data source to
create a simple chatbot which allows the user to as a variety of questions to the chatbot. You DO NOT
need to make this bot run in Discord or Twitter, but rather at the local machine.

Your bot will need to answer the questions (taking note to use various forms of ways to ask the question)
in a human type of form.
1. What were the top 5 shows on Netflix 2 years ago? Show me the top 5 shows on Netflix 2 years
ago. Show me the top 5 shows on Netflix two years ago.
2. What was the top movie on Netflix in 2020?
3. How long was the best movie on Netflix last year? What was the release year of that movie?

These are just *sample* questions. You need to allow you bot to ask 10 different categories/types of
questions. They are up to you on which questions, but the bot needs to tell the user what those question
categories that it can answer. Like: Top movies by year, top X movies / shows by year. Genre of
Movie/Show of the top Movie/Show…# of seasons of top shows…etc. Star(s) of the top show/movie.
You’ll need to use the user response to form a query for your Mongo Dataset.

Your data sources will be the following.
https://www.kaggle.com/datasets/thedevastator/the-ultimate-netflix-tv-shows-and-movies-dataset

Part 1 will be to extract these data sources into one Pandas. Note to only extract the data that supports
the types of questions you want. This is the Extract and Transform sections. For example, if you choose
not to allow users to ask about the number of seasons, do not extract that into your new data set.

Part 2 will be to Load that into a MongoDB. You code will create a new MongoDB and load the data into a
Mongo Database

Part 3 will be to run your bot to answer your questions. The bot will tell the user with that types of
questions they can ask when they enter “help”, and when the bot starts. If the user asks a question that
isn’t in the correct form, or isn’t in the pattern, it suggests the kinds of questions it can answer.

You will turn in:
1) One a Python program that extracts and loads the data into a Mongo DB, which you create in the
Python program. I should be able to execute your code and it create the local MongoDB File from
the source CSVs. You can assume I have the CSVs locally on my computer.
2) One Python program that is the chatbot which will interact with the user and the MongoDB
program.

Grading:
1. Programs successfully builds with no errors – 5
2. Functionally meets the Extract and Transform requirements – 10
    a. Extract multiple CSVs into a Pandas Data frame
    b. Only Transform the Data that you need
3. Load data into a Mongo Database created by your Python Program – 10
4. Your bot will be able to answer questions (10 types of questions asked in various forms) – 15
5. Creativity and Innovation – 3 (think of this as extra)
