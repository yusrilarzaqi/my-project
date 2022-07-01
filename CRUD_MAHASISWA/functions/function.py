import mysql.connector

try:
    db = mysql.connector.connect(
        host="localhost", user="root", password="", database="phpdasar"
    )
    mycursor = db.cursor()
except Exception as e:
    print(e)

table = "bimo"


def query(query):
    mycursor.execute(query)
    return mycursor.fetchall()


def tambah(nama, kelas, email):
    mycursor.execute(
        f"INSERT INTO `bimo` (`id`, `nama`, `kelas`, `email`) VALUES (NULL, '{nama}', '{kelas}', '{email}')"
    )
    db.commit()

def ubah(id, nama, kelas, email):
    mycursor.execute(
        f"UPDATE {table} SET `id` = '{id}', `nama` = '{nama}', `kelas` = '{kelas}', `email` = '{email}' WHERE `bimo`.`id` = {id}"
    )
    db.commit()

def hapus(id):
    mycursor.execute(f"DELETE FROM {table} WHERE id={id}")
    db.commit()
