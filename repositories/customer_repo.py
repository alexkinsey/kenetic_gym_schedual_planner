from db.run_sql import run_sql
from models.customer import Customer

def save(customer):
    sql = """
    INSERT INTO customers (first_name, last_name, membership, join_date, post_code, phone_number, email) 
    VALUES ( %s, %s, %s, %s, %s, %s, %s) RETURNING id
    """
    values = [customer.first_name, customer.last_name, 
    customer.membership, customer.join_date, 
    customer.post_code, customer.phone_number, customer.email]
    results = run_sql( sql, values )
    customer.id = results[0]['id']
    return customer

def select_all():
    customers = []

    sql = "SELECT * FROM customers"
    results = run_sql(sql)

    for row in results:
        customer = Customer(row['first_name'], row['last_name'], row['membership'], 
        row['join_date'], row['post_code'], row['phone_number'], row['email'], row['id'])
        customers.append(customer)
    return customers

def select(id):
    customer = None
    sql = "SELECT * FROM customers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        customer = Customer(result['first_name'], result['last_name'], 
        result['membership'], result['join_date'], result['post_code'], 
        result['phone_number'], result['email'], result['id'])
    return customer

def delete_all():
    sql = "DELETE FROM customers"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM customers WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(customer):
    sql = """
    UPDATE customers SET 
    (first_name, last_name, membership, join_date, post_code, phone_number, email) 
    = (%s, %s, %s, %s, %s, %s, %s) 
    WHERE id = %s
    """
    values = [customer.first_name, customer.last_name, 
    customer.membership, customer.join_date, 
    customer.post_code, customer.phone_number, customer.email, customer.id]
    run_sql(sql, values)
