# Excel-pandas
Read the data from an Excel file using pandas.


## Table of Contents
* [General info](#general-info)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)


## General info
This project allows the data to be read from an Excel file (using pandas). In main part, the data are processed according
to the task to be done. <br>
As we get the final result, we can create the database and fill it with concatenated DataFrames from pandas. <br>
It is also possible to show the results in browser using Flask.


## Technologies Used
Project is created with:
* Python version: 3.6.9
* pandas version: 1.1.5
* openpyxl version: 3.0.9
* Flask version: 2.0.2



## Features
* Extract data from an Excel file
* Populate database (sqlite3) with this data
* Show results in browser, due to Flask


## Setup
Project requirements are in _requirements.txt_. <br>
To get started:
* `pip install -r requirements.txt`


## Usage
* After you clone this repo to your desktop, go to its root directory and run `pip install -r requirements.txt`
to install its dependencies
* To extract data from an Excel file: `main.py`
* To populate the database with data extracted from the Excel file: `database.py`
* To show result in browser: `flask_file.py` and
* You will be able to access it at `127.0.0.1:8000` in your browser


## Project Status
Project is _in progress_.
