import psycopg2
import os

def get_user_data(name):
    connection = psycopg2.connect(
        host=os.environ.get("DB_HOST"),
        database=os.environ.get("DB_NAME"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD")
    )
    cursor = connection.cursor()
    query = "SELECT * FROM player WHERE name = %s"
    cursor.execute(query, (name,))
    result = cursor.fetchone()

    if result is not None:
        nombre, coins, dinero, playerlevel, email, register, timeplay, gender, dinerobanco, skinid, telefono, vip, hambre, sed, vida, armadura = result
        user_data = {
            "name": nombre,
            "coins": coins,
            "cash": dinero,
            "level": playerlevel,
            "email": email,
            "reg_date": register,
            "time_playing": timeplay,
            "gender": gender,
            "bank_money": dinerobanco,
            "skin": skinid,
            "phone_number": telefono,
            "vip": vip,
            "hungry": hambre,
            "thirst": sed,
            "health": vida,
            "armour": armadura
        }
        return user_data
    else:
        return None

user_data = get_user_data(session['name'])

if user_data is not None:
    nombre = user_data["nombre"]
    coins = user_data["coins"]
    dinero = user_data["dinero"]
    playerlevel = user_data["playerlevel"]
    email = user_data["email"]
    register = user_data["register"]
    timeplay = user_data["timeplay"]
    gender = user_data["gender"]
    dinerobanco = user_data["dinerobanco"]
    skinid = user_data["skinid"]
    telefono = user_data["telefono"]
    vip = user_data["vip"]
    hambre = user_data["hambre"]
    sed = user_data["sed"]
    vida = user_data["vida"]
    armadura = user_data["armadura"]
