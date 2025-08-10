from MySQLdb import MySQLError
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import logging
import sys

app = Flask(__name__)

# mysql connection
app.config["MYSQL_HOST"] = 'localhost'
app.config["MYSQL_USER"] = 'root'
app.config["MYSQL_PASSWORD"] = 'Pandi@2000'
app.config["MYSQL_DB"] = 'frappeinventory'
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

logging.basicConfig(
    filename='log/frappe.log',
    encoding='utf-8',
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

logger = logging.getLogger(__name__)

# menu screen
@app.route('/home')
def home_page():
    logger.debug('This is a debug message')
    return render_template('side_menu.html')

# @app.route('/master_screen')
# def master_screen():
#     logger.info("Master Screen")
#     return render_template('master_screen.html')


# product_add page
@app.route('/master_screen', methods=['GET', 'POST'])
def customer_add():
    message = ''
    con = mysql.connection.cursor()
    logger.info("** inside customer add method")
    if request.method == "POST":
        try:
            customer_first_name = request.form.get('firstname') or None
            customer_last_name = request.form.get('lastname')
            gstin = request.form.get('gstin')
            customer_email = request.form.get('email')
            mobile_no = request.form.get('phone') or None
            posting_date = request.form.get('dob') or None

            # form validation
            import re
            if re.search(r"[0-9!@#$%^&*()\-\+={}\[\]:;\"'<>,.?\/|\\]", customer_first_name):
                flash("Special characters and numbers are not allowed")
                return render_template('master_screen.html')

            sql = "INSERT INTO CustomerDetails \
                        (customer_first_name, customer_last_name, customer_email, mobile_no, posting_date,gstin) \
                        values (%s,%s,%s,%s,%s,%s)"
            con.execute(sql, [customer_first_name,customer_last_name,customer_email,mobile_no,posting_date,gstin])
            mysql.connection.commit()
            print(sql)
            logger.info(sql)
            logger.debug(f"%s Record inserted successfully into product table", con.rowcount)
            print(f"%s Record inserted successfully into product table", con.rowcount)
            if(con.rowcount == 1):
                print("msg",con.rowcount)
                message = f"The customer '{customer_first_name}' is added successfully."
                print(message)
                flash(message, category="message")
            return redirect(url_for('customer_add'))
        except MySQLError as ex:
            if("Duplicate" in ex.args[1]):
                message = f"The customer {customer_first_name} {customer_last_name} is exists already. You cannot add an existing customer again.."
                logger.error(f"customer_add() Database exception Occurred: %s", ex.args[1])
                flash(message, category="error")
            else:
                flash(ex.args[1], category="error")
                logger.error(f"customer_add() Database exception Occurred: %s", ex.args[1])
            return render_template('master_screen.html')
        finally:
            con.close()
    return render_template('master_screen.html')

# productmasters
@app.route('/product_masters', methods=['GET', 'POST'])
def product_master_data():
    message = ''
    con = mysql.connection.cursor()
    logger.info("** inside customer add method")
    if request.method == "POST":
        try:
            product_id = request.form.get('product_id') or None
            product_name = request.form.get('product_name') or None
            qty = request.form.get('qty') or None
            category = request.form.get('category') or None
            rate = request.form.get('rate') or None
            total = request.form.get('total') or None

            sql = "INSERT INTO Items (product_id,product_name,qty,category,rate,total) values (%s,%s,%s,%s,%s,%s)"
            con.execute(sql, [product_id,product_name,qty,category,rate,total])
            mysql.connection.commit()
            print(sql)
            logger.info(sql)
            logger.debug(f"%s Record inserted successfully into product table", con.rowcount)
            print(f"%s Record inserted successfully into product table", con.rowcount)
            if(con.rowcount == 1):
                print("msg",con.rowcount)
                message = f" This '{product_name}'is added successfully."
                print(message)
                flash(message, category="message")
            return redirect(url_for('product_master_data'))
        except MySQLError as ex:
            if("Duplicate" in ex.args[1]):
                message = f"The customer {product_name} is exists already. You cannot add an existing customer again.."
                logger.error(f"product_add() Database exception Occurred: %s", ex.args[1])
                flash(message, category="error")
            else:
                flash(ex.args[1], category="error")
                logger.error(f"product_add() Database exception Occurred: %s", ex.args[1])
            return render_template('product_masters.html')
        finally:
            con.close()
    return render_template('product_masters.html')

@app.route('/bill_creation', methods=['GET', 'POST'])
def get_list_data():
    product_list = []
    try:
        con = mysql.connection.cursor()
        sql = "SELECT * FROM Items"
        con.execute(sql)
        id = con.fetchall()
        for row in id:
            # print("row", row)
            product_list.append(row)
        logger.debug("product_id list: %s", product_list)
        logger.debug(f"product_add_data_view() %s products available",con.rowcount)
    except MySQLError as ex:
        flash(ex.args[1], category="error")   
        logger.error(f"product_add_data_view() Database Exception Occured: %s",ex.args[1])
    finally:
        con.close()
    return render_template("bill_creation.html",product_data = product_list)

if __name__ == "__main__":
    app.secret_key = "pandi"
    app.run(debug=True)