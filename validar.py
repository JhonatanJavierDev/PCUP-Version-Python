import hashlib
import mysql.connector

# Conexion a tu base de datos
cnx = mysql.connector.connect(user='user', password='password', host='host', database='database')
cursor = cnx.cursor()

# Fixeo de Vulneraribilidades
name = cnx.escape_string(request.form['name'])
password = cnx.escape_string(request.form['password'])

session['name'] = html.escape(name, quote=True)

if name and password:
    query = "SELECT salt FROM player WHERE name = %s"
    cursor.execute(query, (name, ))
    result = cursor.fetchone()
    if result:
        salt = result[0]
        hash = f"{password}{salt}"
        password = hashlib.sha256(hash.encode()).hexdigest()
        query = "SELECT * FROM player WHERE name = %s AND pass = %s"
        cursor.execute(query, (name, password))
        if cursor.rowcount > 0:
            return redirect(url_for('home'))
        else:
            return render_template('index.html')
    else:
        return render_template('index.html')
else:
    return render_template('index.html')

cursor.close()
cnx.close()
