from flask import Flask, send_from_directory, request
import sqlite3
import json
import requests
#from bs4 import BeautifulSoup


app = Flask(__name__)
connection = 0
c = 0

# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('client/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)

# Path to connect to our database
@app.route("/login", methods=['POST'])
def login():
    # login to a database
    connection = sqlite3.connect('StockTreeDB.db')
    c = connection.cursor()
    # load data from request
    data =  json.loads(request.get_data())
    # fetch password from database
    r = c.execute(f"SELECT * FROM ACCOUNTS WHERE Username='{data['username']}'")
    print("r", r)
    fetched_data = r.fetchone()
    fetched_password = fetched_data[1]
    user_type = fetched_data[2]
    return {
        "valid_password": data['password'] == fetched_password,
        "user_type": user_type
    }

# Path to connect to our database
@app.route("/deleteStock", methods=['POST'])
def deleteStock():
    # Connect to database
    connection = sqlite3.connect('StockTreeDB.db')
    c = connection.cursor()
    # load data from request
    data =  json.loads(request.get_data())
    # check if stock exists
    r = c.execute(f"SELECT Name FROM STOCK WHERE Name='{data['stockName']}'")
    fetched_stock = r.fetchone()
    if fetched_stock is None:
        print("None")
        return {
            "is_deleted": false
        }
    else:
        try:
            c.execute(f"DELETE from STOCK WHERE Name='{data['stockName']}'")
            print("deleted", data['stockName'])
            connection.commit()
            connection.close()
            return {
                "is_deleted": "true"
            }
        except:
            print("An error occured when trying to delete")
            connection.close()
            return {
            "is_deleted": "false"
            }
        
# Path to connect to our database
@app.route("/addStockToWatchlist", methods=['POST'])
def addStockToWatchlist():
    # Connect to the database
    connection = sqlite3.connect('StockTreeDB.db')
    c = connection.cursor()
    
    # Load data from the request
    data = json.loads(request.get_data())
    
    # Check if the stock already exists in the watchlist
    r = c.execute("SELECT Name FROM WATCHLIST WHERE Name = ?", (data['Name'],))
    fetched_stock = r.fetchone()
    
    if fetched_stock:
        connection.close()
        return {
            "is_added": "false",
            "message": "Stock is already in the watchlist."
        }
    else:
        try:
            # Insert the new stock into the watchlist table with Name and Price attributes
            c.execute("INSERT INTO WATCHLIST (Name, Price) VALUES (?, ?)", (data['Name'], data['Price']))
            connection.commit()
            connection.close()
            return {
                "is_added": "true",
                "message": "Stock added to watchlist and saved in the database."
            }
        except:
            connection.close()
            return {
                "is_added": "false",
                "message": "Failed to add the stock to the watchlist and save in the database."
            }

# import sqlite3
# import requests
# from bs4 import BeautifulSoup

# connection = sqlite3.connect('StockTreeDB.db')
# c = connection.cursor()


#if wanted to update a company record, would type something like this:
#update_company_record("'Google', 'Sundar Pichai")

# def update_company_record(company_name, ceo_name):
#     #updates CEO of a specific company
#     connection = sqlite3.connect('StockTreeDB.db')
#     c = connection.cursor()

#     updated_query = f"UPDATE COMPANY CEO = {ceo_name} WHERE CompanyName = {c_name}"

#     c.execute(updated_query, (ceo_name, company_name));
#     connection.commit()
#     print(f"Updated CEO of {company_name} to {ceo_name}")
#     connection.close()
    

# def update_stockholder_name(sh_bank_ac, sh_fname, sh_lname):
#     connection = sqlite3.connect('StockTreeDB.db')
#     c = connection.cursor()

#     updated_query = f"UPDATE FIRST NAME = {sh_fname} AND fUPDATE LAST NAME = {sh_lname} WHERE BankAccount = {sh_bank_ac}"

#     c.execute(updated_query, (sh_fname, sh_lname, sh_bank_ac));
#     connection.commit()
#     print(f"Updated investment amount of {sh_bank_ac} to {sh_fname} {sh_lname}")
#     connection.close()

@app.route("/updateInvestment", methods=['POST'])
def update_investment(sh_bank_ac, sh_amt_invested):
    connection = sqlite3.connect('StockTreeDB.db')
    c = connection.cursor()

    updated_query = f"UPDATE INVESTMENT AMOUNT = {sh_amt_invested} WHERE BankAccount = {sh_bank_ac}"

    c.execute(updated_query, (sh_amt_invested, sh_bank_ac));
    connection.commit()
    print(f"Updated investment amount of {sh_bank_acc} to {sh_amt_invested}")
    connection.close()


# def update_financial_markets():
    

# SIGNUP VIEW FUNCTIONALITY

# add a user to the database
@app.route("/addUser", methods=['POST'])
def add_user():
    # connect to the database
    connection = sqlite3.connect('StockTreeDB.db')
    c = connection.cursor()
    # get data from json request
    data =  json.loads(request.get_data())
    # add user to the database
    c.execute(f"INSERT INTO ACCOUNTS VALUES ('{data['username']}','{data['password']}','{data['account_type']}')")
    connection.commit()
    return {
        "success": "1"
    }

# change password 
@app.route("/changePassword", methods=['POST'])
def change_password():
    # connect to the database
    connection = sqlite3.connect('StockTreeDB.db')
    c = connection.cursor()
    # get data from json request
    data =  json.loads(request.get_data())
    # add user to the database
    c.execute(f"UPDATE ACCOUNTS SET Password='{data['password']}' WHERE Username='{data['username']}'")
    connection.commit()
    return {
        "success": "1"
    }


# COMPANY VIEW FUNCTIONALITY

# get company details
@app.route("/companyDetails", methods=['POST'])
def company_details():
    # connect to the database
    connection = sqlite3.connect('StockTreeDB.db')
    c = connection.cursor()
    # get data from json request
    data = json.loads(request.get_data())
    r = c.execute(f"SELECT * FROM COMPANY WHERE Name='{data['company_name']}'")
    res = r.fetchall()[0]
    # extract all data
    ceo, industry, abbrev, name = res
    return {
        "ceo": ceo,
        "industry": industry,
        "abbreviation": abbrev,
    }


# get stock details
@app.route("/getStock", methods=['POST'])
def get_stock():
    # connect to the database
    connection = sqlite3.connect('StockTreeDB.db')
    c = connection.cursor()
    # get data from json request
    data = json.loads(request.get_data())
    r = c.execute(f"SELECT * FROM STOCK WHERE CName='{data['company_name']}'")
    res = r.fetchall()[0]
    # Extract all data
    abbrev, price, openv, ask, day_range, volume, cname, bid, fmarket = res    
    return {
        "abbreviation": abbrev,
        "price": price,
        "open": openv,
        "ask": ask,
        "day_range": day_range,
        "volume": volume,
        "cname": cname,
        "bid": bid,
        "fmarket": fmarket,
    }

# get country details
@app.route("/getCountryDetails", methods=['POST'])
def get_country_details():
    # connect to the database
    connection = sqlite3.connect('StockTreeDB.db')
    c = connection.cursor()
    # get data from json request
    data = json.loads(request.get_data())
    r = c.execute(f"SELECT * FROM COUNTRY WHERE Name='{data['country_name']}'")
    res = r.fetchall()[0]
    # extract all data
    unemployment, gdp, name, inflation, population = res
    return {
        "unemployment_rate": unemployment,
        "gdp": gdp,
        "name": name,
        "inflation_rate": inflation,
        "population": population,
    }

# get historical stock data
@app.route("/getHistoricalStockData", methods=['POST'])
def get_historical_stock_data():
    # connect to the database
    connection = sqlite3.connect('StockTreeDB.db')
    c = connection.cursor()
    # get data from json request
    data = json.loads(request.get_data())
    r = c.execute(f"SELECT * FROM STOCK WHERE CName='{data['company_name']}'")
    res = r.fetchall()[0]
    # Extract all data
    abbrev, price, openv, ask, day_range, volume, cname, bid, fmarket = res    
    print("abbrev:", abbrev)
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f"https://finance.yahoo.com/quote/{abbrev}/history?p={abbrev}"
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    data_table = soup.findAll("table")[0]
    data_table_rows = data_table.find_all("tr")
    data_table_data = []
    data_table_dates = []
    iter = 0
    for r in data_table_rows:
        if iter > 10:
            break
        col = r.find_all("td")
        col = [t.text.strip() for t in col]
        if len(col) > 2:
            data_table_data.append(col[5])
            data_table_dates.append(col[0])
            iter += 1

    return {
        "historical_data": (",").join([str(elem) for elem in data_table_data]),
        "dates": (";").join([str(e) for e in data_table_dates]), 
    }

@app.route("/getNewCountry", methods=['POST'])
def get_new_country():
    #get country
    json_data = json.loads(request.get_data())
    country = json_data['name']
    #Get data from api
    param = ''
    #note: there is a lot of info
    #available through the world bank
    gdp_ind = "NY.GDP.MKTP.CD"
    unemp_ind = "SL.UEM.TOTL.ZS"
    infl_ind = "FP.CPI.TOTL.ZG"
    url = "http://api.worldbank.org/v2/country/" + country + "/indicator/" + gdp_ind + "?format=json"
    response = requests.get(url, params=param)
    #parse
    data = response.json()[1][0]
    gdp = data["value"]
    url = "http://api.worldbank.org/v2/country/" + country + "/indicator/" + unemp_ind + "?format=json"
    response = requests.get(url, params=param)
    #parse
    data = response.json()[1][0]
    unemp = data["value"]
    url = "http://api.worldbank.org/v2/country/" + country + "/indicator/" + infl_ind + "?format=json"
    response = requests.get(url, params=param)
    #parse
    data = response.json()[1][0]
    infl = data["value"]
    #add data to database
    # connect to the database
    connection = sqlite3.connect('StockTreeDB.db')
    c = connection.cursor()
    r = c.execute(f"INSERT INTO COUNTRY (Name, GDP, Unemployment_rate, Inflation_rate) VALUES ('{country}', '{gdp}', '{unemp}', '{infl}')")
    return {
        "outcome":"success" 
    }





# Path to fetch, i.e. SELECT
@app.route("/fetch")
def fetch():
    # connect to database
    connection = sqlite3.connect('StockTreeDB.db')
    c = connection.cursor()
    # execute a function to select from the database
    r = c.execute("SELECT * FROM STOCK")
    return str(r.fetchall())

# Path to fetch, i.e. SELECT
@app.route("/fetchName")
def fetchName():
    # connect to database
    connection = sqlite3.connect('StockTreeDB.db')
    c = connection.cursor()
    # execute a function to select from the database
    r = c.execute("SELECT Name FROM STOCK")
    return str(r.fetchall())

if __name__ == "__main__":
    app.run(debug=True)