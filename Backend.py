import sqlite3 as sql

class TransactionObject():
    database    = "livraria.db"
    conn        = None
    cur         = None
    connected   = False

    def connect(self):
        TransactionObject.conn      = sql.connect(TransactionObject.database)
        TransactionObject.cur       = TransactionObject.conn.cursor()
        TransactionObject.connected = True

    def disconnect(self):
        TransactionObject.conn.close()
        TransactionObject.connected = False

    def execute(self, sql, parms = None):
        if TransactionObject.connected:
            if parms == None:
                TransactionObject.cur.execute(sql)
            else:
                TransactionObject.cur.execute(sql, parms)
            return True
        else:
            return False

    def fetchall(self):
        return TransactionObject.cur.fetchall()

    def persist(self):
        if TransactionObject.connected:
            TransactionObject.conn.commit()
            return True
        else:
            return False



def initDB():
    trans = TransactionObject()
    trans.connect()
    trans.execute("CREATE TABLE IF NOT EXISTS livros (li_codigo INTEGER PRIMARY KEY , li_nome TEXT , li_autor TEXT , li_editora TEXT ,li_volume TEXT, li_ano_lanc TEXT , li_local TEXT , li_fornecedor TEXT, li_data_entrada TEXT, li_estoque_min INTEGER, li_estoque_max INTEGER , li_estoque_atual INTEGER, li_preco_compra REAL, li_preco_venda REAL)")
    trans.persist()
    trans.disconnect()

def insert(li_nome, li_autor, li_editora, li_volume, li_ano_lanc, li_local, li_fornecedor, li_data_entrada, li_estoque_min, li_estoque_max, li_estoque_atual, li_preco_compra, li_preco_venda):
    trans = TransactionObject()
    trans.connect()
    trans.execute("INSERT INTO livros VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?,?,?)", (li_nome, li_autor, li_editora, li_volume, li_ano_lanc, li_local, li_fornecedor, li_data_entrada, li_estoque_min, li_estoque_max, li_estoque_atual, li_preco_compra, li_preco_venda))
    trans.persist()
    trans.disconnect()

def view():
    trans = TransactionObject()
    trans.connect()
    trans.execute("SELECT * FROM livros")
    rows = trans.fetchall()
    trans.disconnect()
    return rows

def delete(li_codigo):
    trans = TransactionObject()
    trans.connect()
    trans.execute("DELETE FROM livros WHERE li_codigo = ?", (li_codigo,))
    trans.persist()
    trans.disconnect()

initDB()


