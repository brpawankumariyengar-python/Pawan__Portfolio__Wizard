import re as Niyamit__Abhivyakti
import time as Samay
import chardet as varnavignyapakah
import os as Prachalan__Pranali
import glob as Sadhakah
import json
import pandas as Pandas__Data__Frame

All__Face__Value = []
All__Current__Share__Price = []
All__Group__Type = []
All__Price__To__Equity__Ratio = []
All__Price__To__Book__Ratio = []
All__EPS = []
All__Number__Of__Shares = []
All__Invested__Amount = []
All__Company__Names = []
All__Week__High = []
All__ROE = []
Total_Invested_Amount =[]


def Pawan__Load__JSON():
	with open("Pawan__Portfolio__Wizard.FOOD", 'r') as Pawan__File__Data: Pawan__Share__Dictionary = json.load(Pawan__File__Data)
	Pawan__Loop__Dictionary(Pawan__Share__Dictionary)


def Pawan__Loop__Dictionary(Pawan__Share__Dictionary):
	global All__Number__Of__Shares
	global All__Invested__Amount
	global All__Company__Names
	for key in Pawan__Share__Dictionary:
		All__Company__Names.append(Pawan__Share__Dictionary[key][0])
		All__Number__Of__Shares.append(Pawan__Share__Dictionary[key][1])
		All__Invested__Amount.append(Pawan__Share__Dictionary[key][2])
	Pawan__Process__Company__Name()


def Pawan__Process__Company__Name():
	global All__Company__Names
	for index, company in enumerate(All__Company__Names):
		Temp__String = company[43::]
		Temp__Position = Temp__String.find("/")
		Temp__String = Temp__String[:Temp__Position:]
		Temp__String = Temp__String.replace("-", " ")
		Temp__String = Temp__String.upper()
		Temp__Position = Temp__String.find("LIMITED")
		if Temp__Position != -1: Temp__String = Temp__String.replace("LIMITED", "LTD")
		All__Company__Names[index] = Temp__String


def Pawan__Get__Text(Pawan__File__Name):
    with open(Pawan__File__Name, 'rb') as File__Data:
        Pawan__Get__Data = File__Data.read()
    Pawan__Process__String(Pawan__Get__Data)
    #Prachalan__Pranali.remove(Pawan__File__Name)


def Pawan__Process__String(Pawan__Get__Data):
	Pawan__Get__Encoding = varnavignyapakah.detect(Pawan__Get__Data)
	Pawan__Get__Encoding = Pawan__Get__Encoding["encoding"]
	Pawan__Decoded__Data = Pawan__Get__Data.decode(Pawan__Get__Encoding)
	Get__Current__Share__Price(Pawan__Decoded__Data)
	Get__Group__Type(Pawan__Decoded__Data)
	Get__Price__To__Equity__And__Price__To__Book__Ratio(Pawan__Decoded__Data)
	Get__EPS(Pawan__Decoded__Data)
	Get__Week__High(Pawan__Decoded__Data)
	Get__ROE(Pawan__Decoded__Data)


def Pawan__Loop__Text__Files():
	Pawan__Folder__Path = Prachalan__Pranali.getcwd()
	Pawan__Folder__Path = Pawan__Folder__Path  + "\\Images\\"
	Pawan__Pattern = Prachalan__Pranali.path.join(Pawan__Folder__Path,"*.txt")
	Pawan__List__Text__Files = Sadhakah.glob(Pawan__Pattern)
	for Pawan__File__Name in Pawan__List__Text__Files:
		Pawan__Get__Text(Pawan__File__Name)


def Get__Current__Share__Price(Pawan__Decoded__Data):
	global All__Current__Share__Price
	Pawan__Current__Share__Price__Position = Pawan__Decoded__Data.find("52 Wk")
	Pawan__Temporary__String = Pawan__Decoded__Data[:Pawan__Current__Share__Price__Position:]
	Pawan__Current__Share__Price__Position = Pawan__Decoded__Data.find("Previous Close")
	Pawan__Temporary__String = Pawan__Temporary__String[Pawan__Current__Share__Price__Position::]
	Pawan__Pattern = r'\b(\d+\.\d+)\b'
	result__position = Niyamit__Abhivyakti.search(Pawan__Pattern, Pawan__Temporary__String)
	Pawan__Filetered__Data = result__position.group()
	Pawan__Filetered__Data = float(Pawan__Filetered__Data)
	All__Current__Share__Price.append(Pawan__Filetered__Data)
	

def Get__Group__Type(Pawan__Decoded__Data):
	global All__Group__Type
	Pawan__Group__Type__Position = Pawan__Decoded__Data.find("/T+") - 1
	Pawan__Group__Type__Value = Pawan__Decoded__Data[Pawan__Group__Type__Position]
	All__Group__Type.append(Pawan__Group__Type__Value)


def Get__Price__To__Equity__And__Price__To__Book__Ratio(Pawan__Decoded__Data):
	global All__Price__To__Equity__Ratio
	global All__Price__To__Book__Ratio
	Pawan__PE__Position = Pawan__Decoded__Data.find("PE/PB")
	Pawan__PE__Position = Pawan__PE__Position + 5
	Pawan__Temporary__String = Pawan__Decoded__Data[Pawan__PE__Position:(Pawan__PE__Position + 15):]
	Pawan__Temporary__String = Pawan__Temporary__String.replace(" ","")
	Pawan__Pattern = r'(\d+\.\d+)\/(\d+\.\d+)'
	Pawan__Matches = Niyamit__Abhivyakti.findall(Pawan__Pattern, Pawan__Temporary__String)
	PE__Value = Pawan__Matches[0][0]
	PB__Value = Pawan__Matches[0][1]
	All__Price__To__Equity__Ratio.append(PE__Value)
	All__Price__To__Book__Ratio.append(PB__Value)


def Get__EPS(Pawan__Decoded__Data):
	global All__EPS
	Pawan__EPS__Position = Pawan__Decoded__Data.find("EPS (TTM)")
	Pawan__EPS__Position = Pawan__EPS__Position + 9
	Pawan__Temporary__String = Pawan__Decoded__Data[Pawan__EPS__Position::]
	Pawan__Pattern = r'(\d+\.\d+)'
	Pawan__Matches = Niyamit__Abhivyakti.search(Pawan__Pattern, Pawan__Temporary__String)
	Pawan__Temporary__String = Pawan__Matches.group()
	All__EPS.append(Pawan__Temporary__String)


def Get__Week__High(Pawan__Decoded__Data):
	global All__Week__High
	Pawan__Week__High__Position = Pawan__Decoded__Data.find("Wk High")
	Pawan__Week__High__Position = Pawan__Week__High__Position + 7
	Pawan__Temporary__String = Pawan__Decoded__Data[Pawan__Week__High__Position:(Pawan__Week__High__Position + 11):]
	Pawan__Temporary__String = Pawan__Temporary__String.replace(",","")
	Pawan__Temporary__String = Pawan__Temporary__String.replace(" ","")
	Pawan__Temporary__String = Pawan__Temporary__String.replace("T","")
	Pawan__Temporary__String = Pawan__Temporary__String.replace("Q","")
	Pawan__Temporary__String = float(Pawan__Temporary__String)
	All__Week__High.append(Pawan__Temporary__String)


def Get__ROE(Pawan__Decoded__Data):
	global All__ROE
	Pawan__ROE__Position = Pawan__Decoded__Data.find("ROE")
	Pawan__ROE__Position = Pawan__ROE__Position + 3
	Pawan__Temporary__String = Pawan__Decoded__Data[Pawan__ROE__Position:(Pawan__ROE__Position + 9):]
	Pawan__Pattern = r'\d+\.\d+'
	result__position = Niyamit__Abhivyakti.search(Pawan__Pattern, Pawan__Temporary__String)
	result__position = result__position.group()
	result__position = float(result__position)
	All__ROE.append(result__position)


def Generate__Excel__Sheet():
	Total__Current__Amount = [price * shares for price, shares in zip(All__Current__Share__Price, All__Number__Of__Shares)]
	Delta__Values = [High - Current for High, Current in zip(All__Week__High, All__Current__Share__Price)]
	Profit__Loss__Statement = [Total__Current__Amount__Value -  Invested__Value for Total__Current__Amount__Value, Invested__Value in zip(Total__Current__Amount, All__Invested__Amount)]
	Profit__Loss__Percentage = [((Profit__And__Loss / Total__Current__Amount__Value ) * 100) for Profit__And__Loss, Total__Current__Amount__Value in zip(Profit__Loss__Statement, Total__Current__Amount)]

	Pawan__Consolidated__Dictionary = {
	'Company__Name': All__Company__Names,
	'Share Price Info': All__Current__Share__Price,
	'Detla Value': Delta__Values,
	'Invested Value': All__Invested__Amount,
	'Number Of Shares': All__Number__Of__Shares,
	'Total Current Amount': Total__Current__Amount,
	'Profit & Loss Statement' : Profit__Loss__Statement,
	'Profit & Loss Percentage' : Profit__Loss__Percentage,
	'ROE Value' : All__ROE,
	'EPS Info' : All__EPS,
	'PE Ratio': All__Price__To__Equity__Ratio,
	'P/B Ratio': All__Price__To__Book__Ratio,
	'Share Group Category' : All__Group__Type
	}

	Pawan__Consolidated__Dataframe = Pandas__Data__Frame.DataFrame(Pawan__Consolidated__Dictionary)
	Pawan__Consolidated__Dataframe.to_excel("Pawan__Portfolio__Wizard.xlsx", sheet_name = 'Portfolio__Sheet', index=False)

if __name__ == "__main__":
	Pawan__Load__JSON()
	Pawan__Loop__Text__Files()
	Generate__Excel__Sheet()
	Samay.sleep(21)


