import numpy as np
import pandas as pd
import pandasql as ps
import sqlite3

def read_sql_queda(queda):
	conn = sqlite3.connect('db.sqlite3')
	sql_datas = f"""
				SELECT queda_tesao FROM cable_tabelacondutor
        WHERE secao = '{queda}';
	"""

	read_db = pd.read_sql_query(sql_datas, conn)
	conn.close()

	return read_db

