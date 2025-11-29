# check_db.py
import sqlite3
import sys

def check_database():
    try:
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        
        print("=== Tablas en la base de datos ===")
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
        for table in tables:
            table_name = table[0]
            print(f"\nTabla: {table_name}")
            
            try:
                # Obtener información de columnas
                cursor.execute(f"PRAGMA table_info({table_name})")
                columns = [col[1] for col in cursor.fetchall()]
                print(f"Columnas: {columns}")
                
                # Verificar si hay datos
                cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
                count = cursor.fetchone()[0]
                print(f"Registros: {count}")
                
                # Mostrar algunas filas de ejemplo
                if count > 0:
                    print("\nPrimeras filas:")
                    cursor.execute(f"SELECT * FROM {table_name} LIMIT 2")
                    for row in cursor.fetchall():
                        print(row)
                        
            except Exception as e:
                print(f"Error al leer la tabla {table_name}: {str(e)}")
                
    except Exception as e:
        print(f"Error al conectar a la base de datos: {str(e)}")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    check_database()