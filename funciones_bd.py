# ==========================================
# 3. MÓDULO DE PERSISTENCIA CON SQLITE (funciones_bd.py)
# ==========================================
import sqlite3
from datetime import date

NOMBRE_BD = "sabor_urbano.db"

def obtener_fecha_actual():
    """Retorna la fecha de hoy en formato texto 'YYYY-MM-DD'."""
    return date.today().isoformat()

def inicializar_bd():
    """Crea la base de datos y la tabla resumen_diario si no existen."""
    conexion = sqlite3.connect(NOMBRE_BD)
    cursor = conexion.cursor()
    
    # TODO 1: Ejecuta la sentencia SQL para crear la tabla 'resumen_diario'
    # con las columnas: fecha TEXT PRIMARY KEY y monto_total REAL.
    # Pista: usa CREATE TABLE IF NOT EXISTS resumen_diario (...)  
    cursor.execute("""
    
    

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS "resumen_diario" (
    "fecha"	TEXT NOT NULL,
    "monto_total"	REAL NOT NULL,
    PRIMARY KEY("fecha"));
    """)
    
    conexion.commit()
    conexion.close()

def cargar_monto_diario():
    """Consulta el monto guardado para la fecha de hoy. Si no existe, crea el registro en 0.0."""
    hoy = obtener_fecha_actual()
    conexion = sqlite3.connect(NOMBRE_BD)
    cursor = conexion.cursor()
    
    # TODO 2: Consulta el 'monto_total' de la tabla 'resumen_diario' donde fecha sea igual a 'hoy'.
    # Pista: cursor.execute("SELECT monto_total FROM resumen_diario WHERE fecha = ?", (hoy,))
    
    fila = cursor.fetchone()
    
    if fila is not None:
        monto = fila[0]
    else:
        # TODO 3: Si no hay registro para hoy (fila is None), inserta una nueva fila
        # con la fecha de hoy y monto_total en 0.0, luego haz commit.
        # Pista: INSERT INTO resumen_diario (fecha, monto_total) VALUES (?, ?)
        pass
        monto = 0.0
        
    conexion.close()
    return monto

def guardar_monto_diario(nuevo_monto):
    """Actualiza el monto_total en la base de datos para la fecha de hoy."""
    hoy = obtener_fecha_actual()
    conexion = sqlite3.connect(NOMBRE_BD)
    cursor = conexion.cursor()
    
    # TODO 4: Actualiza el campo 'monto_total' con 'nuevo_monto' para la fecha 'hoy'.
    # Pista: UPDATE resumen_diario SET monto_total = ? WHERE fecha = ?
    
    conexion.commit()
    conexion.close()