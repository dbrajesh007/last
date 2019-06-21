from flask import Flask

app = Flask(__name__)


@app.route('/a')
def Hello():
    return "hello_world1111"
    
@app.route('/b')
def Hello():
    import pyodbc


    server = 'sunthedb.database.windows.net'
    database = 'sunthemart'
    username = 'suntheadmin'
    password = '$unthe123$'
    
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ',1433', user=username, password=password, database=database)
    cursor = conn.cursor()
                             
    return "hello_world2222"


if __name__ == '__main__':
    app.run()
