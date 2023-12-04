from flask import Flask, send_from_directory, request
import sqlite3
import json
import requests
from bs4 import BeautifulSoup


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
    r = c.execute(f"SELECT Name FROM STOCK WHERE CName='{data['stockName']}'")
    fetched_stock = r.fetchone()
    if fetched_stock is None:
        print("None")
        return {
            "is_deleted": "false"
        }
    else:
        try:
            c.execute(f"DELETE from STOCK WHERE CName='{data['stockName']}'")
            print("deleted", data['stockName'])
            connection.commit()
            connection.close()
            return {
                "is_deleted": "true"
            }
        except Exception as e:
            print("An error occured when trying to delete")
            print(e)
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
    stock_dict = {}
    stock_dict['name'] = data['name']
    stock_dict['symbol'] = data['symbol']
    stock_dict['s_open'] = ""
    stock_dict['bid'] = ""
    stock_dict['ask'] = ""
    stock_dict['day_range'] = ""
    stock_dict['volume'] = ""
    stock_dict['price'] = ""
    stock_dict['bid'] = ""
    stock_dict['fmarket'] = ""
    try:
        # Check if the stock already exists in the watchlist
        print(data['name'])
        r = c.execute("SELECT CName FROM Stock WHERE CName = ?", (stock_dict['name'],))
        fetched_stock = r.fetchone()
    except:
        print("could not query stock database")
        print(e)
        connection.close()
        return {
            "is_added": "false",
            "message": "Failed to add the stock to the watchlist and save in the database."
        }
    if fetched_stock:
        connection.close()
        return {
            "is_added": "false",
            "message": "Stock is already in the watchlist."
        }
    else:
        try:
            headers = {'User-Agent': 'Mozilla/5.0'}
            url = f"https://finance.yahoo.com/quote/{stock_dict['symbol']}"
            print(f"url {url}")
            page = requests.get(url, headers=headers)
            soup = BeautifulSoup(page.content, "html.parser")

            data_table = soup.findAll("table")[0]
            data_table_rows = data_table.find_all("tr")
            data_table_data = []
            for r in data_table_rows:
                col = r.find_all("td")
                col = [t.text.strip() for t in col]
                if col[0] == 'Open':
                    stock_dict['s_open'] = col[1]
                if col[0] == 'Bid':
                    stock_dict['bid'] = col[1]
                if col[0] == 'Ask':
                    stock_dict['ask'] = col[1]
                if col[0] == "Day's Range":
                    stock_dict['day_range'] = col[1]
                if col[0] == 'Volume':
                    stock_dict['volume'] = col[1]
                for key in stock_dict.keys():
                    if stock_dict[key] == "":
                        stock_dict[key] = "Unknown"
                        if key == 'price' or key == 's_open' or key == 'volume':
                            stock_dict[key] = 0
            # Insert the new stock into the watchlist table with Name and Price attributes
            c.execute("INSERT INTO STOCK (CName, Name, Price, Open, Ask, Day_range, Volume, Bid, FMarket) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (stock_dict['name'], stock_dict['symbol'], stock_dict['price'], stock_dict['s_open'], stock_dict['ask'], stock_dict['day_range'], stock_dict['volume'], stock_dict['bid'], stock_dict['fmarket']))
            connection.commit()
            connection.close()
            return {
                "is_added": "true",
                "message": "Stock added to watchlist and saved in the database."
            }
        except Exception as e:
            print("could not add stock to database")
            print(e)
            connection.close()
            return {
                "is_added": "false",
                "message": "Failed to add the stock to the watchlist and save in the database."
            }   

@app.route("/updateInvestment", methods=['POST'])
def update_investment():
    connection = sqlite3.connect('StockTreeDB.db')
    c = connection.cursor()
    data = json.loads(request.get_data())
    try:
        r = c.execute(f"SELECT ID FROM ACCOUNTS WHERE Username='{data['username']}'")
        res = r.fetchall()[0][0]
        print(f"ret id {res}")
        print(f"UPDATE OWNS SET Amt_Share={data['amt']} WHERE ID={res} AND SName='{data['name']}'")

        r = c.execute(f"UPDATE OWNS SET Amt_Share={data['amt']} WHERE ID={res} AND SName='{data['name']}'")
    
        connection.commit()
        connection.close()
        return {
            "success": "1"
        }
    except Exception as e:
        connection.close()
        print("no user id")
        print(e)
        return {
            "success": "0"
        }




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
    try:
        c.execute(f"INSERT INTO ACCOUNTS VALUES ('{data['username']}','{data['password']}','{data['account_type']}')")
        connection.commit()
        return {
            "success": "1"
        }
    except Exception as e:
        print("failed add user")
        print(e)
        return {
            "failed add user"
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
    try:
        c.execute(f"UPDATE ACCOUNTS SET Password='{data['password']}' WHERE Username='{data['username']}'")
        connection.commit()
        return {
            "success": "1"
        }
    except Exception as e:
        print("failed change password")
        print(e)
        return {
            "failed change password"
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
    try:
        r = c.execute(f"SELECT * FROM COMPANY WHERE Name='{data['company_name']}'")
        res = r.fetchall()[0]
        # extract all data
        ceo, industry, abbrev, name = res
        r = c.execute(f"SELECT Country_name FROM OPERATES_IN WHERE CName='{data['company_name']}'")
        country = r.fetchall()[0]
        return {
            "ceo": ceo,
            "industry": industry,
            "abbreviation": abbrev,
            "country": country
        }
    except Exception as e:
        print("failed company details")
        print(e)
        return {
            "message" : "failed"
        }


# get stock details
@app.route("/getStock", methods=['POST'])
def get_stock():
    # connect to the database
    connection = sqlite3.connect('StockTreeDB.db')
    c = connection.cursor()
    # get data from json request
    data = json.loads(request.get_data())
    try:
        r = c.execute(f"SELECT * FROM STOCK WHERE CName='{data['company_name']}'")
        print(f"r {r}")
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
    except Exception as e:
        print("get stock")
        print(e)
        return {
            "message" : "failed"
        }
       

# get country details
@app.route("/getCountryDetails", methods=['POST'])
def get_country_details():
    # connect to the database
    connection = sqlite3.connect('StockTreeDB.db')
    c = connection.cursor()
    # get data from json request
    data = json.loads(request.get_data())
    try:
        r = c.execute(f"SELECT * FROM COUNTRY WHERE Name='{data['country_name']}'")
        res = r.fetchall()[0]
        # extract all data
        unemployment, gdp, name, inflation, population = res
        r = c.execute(f"SELECT GDP / Population FROM COUNTRY WHERE Name='{data['country_name']}'")
        gdp_per_capita = r.fetchall()[0]
        return {
            "message": "success",
            "unemployment_rate": unemployment,
            "gdp": gdp,
            "name": name,
            "inflation_rate": inflation,
            "population": population,
            "gdp_per_capita": gdp_per_capita,
        }
    except Exception as e: 
        print("could not get country details")
        print(e)
        return {
            "message": "failed"
        }

# get historical stock data
@app.route("/getHistoricalStockData", methods=['POST'])
def get_historical_stock_data():
    # connect to the database
    connection = sqlite3.connect('StockTreeDB.db')
    c = connection.cursor()
    # get data from json request
    data = json.loads(request.get_data())
    try:
        r = c.execute(f"SELECT * FROM STOCK WHERE CName='{data['company_name']}'")
        res = r.fetchall()[0]
        # Extract all data
        abbrev, price, openv, ask, day_range, volume, cname, bid, fmarket = res    
        print("abbrev:", abbrev)
        headers = {'User-Agent': 'Mozilla/5.0'}
        url = f"https://finance.yahoo.com/quote/{abbrev}/history?p={abbrev}"
        print(f"url {url}")
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

        print(f"data {data_table_dates}")

        return {
            "historical_data": (",").join([str(elem) for elem in data_table_data]),
            "dates": (";").join([str(e) for e in data_table_dates]), 
        }
    except Exception as e:
        print("get historical stock data failed")
        print(e)
        return {
            "message": "failed"
        }

@app.route("/getNewCountry", methods=['POST'])
def get_new_country():
    try:
        #get country
        json_data = json.loads(request.get_data())
        country = json_data['name']
        #Get data from api
        param = ''
        #note: there is a lot of info
        #available through the world bank
        url = "https://api.worldbank.org/v2/sources/2/concepts/country/search/" + country + "?format=json"
        response = requests.get(url, params=param)
        data = response.json()
        country_code = data['source'][0]['concept'][0]['variable'][0]['id']
        gdp_ind = "NY.GDP.MKTP.CD"
        unemp_ind = "SL.UEM.TOTL.ZS"
        infl_ind = "FP.CPI.TOTL.ZG"
        url = "http://api.worldbank.org/v2/country/" + country_code + "/indicator/" + gdp_ind + "?mrv=1&format=json"
        response = requests.get(url, params=param)
        #parse
        data = response.json()[1][0]
        gdp = data["value"]
        url = "http://api.worldbank.org/v2/country/" + country_code + "/indicator/" + unemp_ind + "?format=json"
        response = requests.get(url, params=param)
        #parse
        data = response.json()[1][0]
        unemp = data["value"]
        url = "http://api.worldbank.org/v2/country/" + country_code + "/indicator/" + infl_ind + "?format=json"
        response = requests.get(url, params=param)
        #parse
        data = response.json()[1][0]
        infl = data["value"]
        add_country_to_database(country, gdp, unemp, infl)
        return {
            "name":country, "gdp":gdp, "unempl_rate":unemp, "infl_rate":infl 
        }
    except Exception as e:
        print("get new country failed")
        print(e)
        return {
            "message":"failed"
        }

def add_country_to_database(country, gdp, unemp, infl):
    #add data to database
    # connect to the database
    
    connection = sqlite3.connect('StockTreeDB.db')
    c = connection.cursor()
    try:
        r = c.execute(f"SELECT Name FROM COUNTRY WHERE Name='{country}'")
        fetched_stock = r.fetchone()
        if fetched_stock is None:
            r = c.execute(f"INSERT INTO COUNTRY (Name, GDP, Unemployment_rate, Inflation_rate) VALUES ('{country}', '{gdp}', '{unemp}', '{infl}')")
            connection.commit()
            connection.close()
            return {"message":"success"}
    except Exception as e:
        print("add country to database failed")
        print(e)
        return {
            "message":"failed"
        }

@app.route("/emplStatsReports", methods=["POST"])
def empl_stats_reports():
    # connect to the database
    connection = sqlite3.connect('StockTreeDB.db')
    c = connection.cursor()
    data = json.loads(request.get_data())
    try:
        r = c.execute(f"SELECT COUNT(*) FROM EMPLOYEE WHERE CName='{data['company_name']}'")
        num_empl = r.fetchall()[0][0]
        print(f"num_empl {num_empl}")
        r = c.execute(f"SELECT Fname, LName, MAX(Salary) FROM EMPLOYEE WHERE CName='{data['company_name']}'")
        highest_empl_fname, highest_empl_lname, _ = r.fetchall()[0]
        highest_name = highest_empl_fname + " " + highest_empl_lname
        r = c.execute(f"SELECT Fname, LName, MIN(Salary) FROM EMPLOYEE WHERE CName='{data['company_name']}'")
        lowest_empl_fname, lowest_empl_lname, _ = r.fetchall()[0]
        lowest_name = lowest_empl_fname + " " + lowest_empl_lname
        r = c.execute(f"SELECT AVG(Salary) FROM EMPLOYEE WHERE CName='Samsung'")
        avg_salary = r.fetchall()[0]
        print(f"avg_salary {avg_salary}")
        return {
            "data": "true",
            "num_empl": num_empl,
            "highest_empl": highest_name,
            "lowest_empl": lowest_name,
            "avg_salary": avg_salary
        }
    except Exception as e:
        print("failed to get stats")
        print(e)
        return {
            "data": "false"
        }

@app.route("/countryStatsReports", methods=["POST"])
def country_stats_reports():
    # connect to the database
    connection = sqlite3.connect('StockTreeDB.db')
    c = connection.cursor()
    data = json.loads(request.get_data())
    try:
        # fetch country-specific details from the database
        r = c.execute(f"SELECT COUNT(*) FROM COUNTRY WHERE Name='{data['country_name']}'")
        country_exists = r.fetchall()[0][0]

        if country_exists:
            # find the avg inflation rate, avg unemployment rate, and min population for each country
            r = c.execute(f"SELECT AVG(Inflation_rate), AVG(Unemployment_rate), MIN(Population) FROM COUNTRY WHERE Name='{data['country_name']}'")
            country_data = r.fetchall()[0]
            avg_inflation_rate, avg_unemployment_rate, min_population = country_data
            # return country data paramaters
            return {
                "country_name": data['country_name'],
                "average_inflation_rate": avg_inflation_rate,
                "average_unemployment_rate": avg_unemployment_rate,
                "minimum_population": min_population,
            }
        else:
            return {
                "message": "Country not found in database."
            }
    except Exception as e:
        print("Failed to get country stats")
        print(e)
        return {
            "message":"failed to get country stats"
        }




# FUNCTIONS FOR ADMIN USERS
@app.route("/userStatsReports", methods=["POST"])
def user_stats_reports():
    # connect to the database
    connection = sqlite3.connect('StockTreeDB.db')
    c = connection.cursor()
    try:
        r = c.execute(f"SELECT COUNT(*) FROM ACCOUNTS WHERE Ac_type='Stockholder'")
        num_stockholders = r.fetchall()[0]
        r = c.execute(f"SELECT COUNT(*) FROM ACCOUNTS WHERE Ac_type='Company'")
        num_companies = r.fetchall()[0]
        r = c.execute(f"SELECT COUNT(*) FROM ACCOUNTS WHERE Ac_type='Admin'")
        num_admins = r.fetchall()[0]
        return {
            "num_companies": num_companies,
            "num_stockholders": num_stockholders,
            "num_admins": num_admins
        }
    except Exception as e:
        print("failed to get stats")
        print(e)
        return {
            "message":"failed to get stats"
        }


# Path to fetch, i.e. SELECT
@app.route("/fetch", methods=["POST"])
def fetch():
    # connect to database
    connection = sqlite3.connect('StockTreeDB.db')
    c = connection.cursor()
    # execute a function to select from the database
    try:
        r = c.execute("SELECT * FROM STOCK")
        return str(r.fetchall())
    except Exception as e:
        print("fetch failed")
        print(e)
        return {
            "message":"fetch failed"
        }

# Path to fetch, i.e. SELECT
@app.route("/fetchName", methods=["POST"])
def fetchName():
    # connect to database
    connection = sqlite3.connect('StockTreeDB.db')
    c = connection.cursor()
    # execute a function to select from the database
    data = json.loads(request.get_data())
    try:
        r = c.execute(f"SELECT ID FROM ACCOUNTS WHERE Username='{data['username']}'")
        ret = r.fetchall()[0][0]
        print(f"SELECT SName, Amt_Share FROM OWNS WHERE ID={ret}")
        r = c.execute(f"SELECT SName, Amt_Share FROM OWNS WHERE ID={ret}")
        stocks = r.fetchall()
        print(stocks)
        stock_list = []
        for stock in stocks:
            stock_list.append([stock[0], f'{stock[1]}'])
        print(stock_list)
        stock_json = json.dumps(stock_list)
        return str(stock_json)
    except Exception as e:
        print("fetch name failed")
        print(e)
        return {
            "message":"fetch name"
        }

if __name__ == "__main__":
    app.run(debug=True)