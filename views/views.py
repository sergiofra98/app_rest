import json
from flask import request, jsonify
from .utils import log_error, constants
import traceback


def inserta_persona():
    nueva_persona = request.json        
    
    if not 'nombre' in nueva_persona or\
        not 'puesto' in nueva_persona or\
        not 'correo' in nueva_persona or\
        not 'fecha_nacimiento' in nueva_persona:
        return jsonify('debe ser dict con los campos "nombre", "puesto", "correo" y "fecha_nacimiento"'), 400
    
    try:
        conn, cursor = constants.genera_cursor()
        SQL = """INSERT INTO usuarios (
            nombre,
            puesto, 
            correo,
            fecha_nacimiento
        ) VALUES (%(nombre)s, %(puesto)s, %(correo)s, %(fecha_nacimiento)s);""" # Note: no quotes
        cursor.execute(SQL, nueva_persona) # Note: no % operator
        conn.commit()
        cursor.close()
        conn.close()

        return jsonify('cuenta "{}" creada correctamente'.format(nueva_persona['correo'])), 201
    except Exception as ex:
        traceback.print_exc()
        cursor.close()
        conn.close()
        return jsonify('error interno'), 500

def obten_persona(correo):
    if not correo:
        return jsonify('proporcione un correo correcto'), 400
  
    conn, cursor = constants.genera_cursor()

    try:
        conn, cursor = constants.genera_cursor()
        SQL = """SELECT * FROM usuarios WHERE correo=%s;""" # Note: no quotes
        cursor.execute(SQL, (correo,)) # Note: no % operator
        resp = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()

        if resp is not None:
            return jsonify({
                'nombre': resp[0],
                'puesto': resp[1],
                'correo': resp[2],
                'fecha_nacimiento': resp[3]
           } ), 200
        else:
            return jsonify('no hay resultados'), 404

    except Exception as ex:
        traceback.print_exc()
        cursor.close()
        conn.close()
        return jsonify('error interno'), 500


def actualiza_persona(correo):
    nueva_persona = request.json        
    
    if not 'nombre' in nueva_persona and\
        not 'puesto' in nueva_persona and\
        not 'correo' in nueva_persona and\
        not 'fecha_nacimiento' in nueva_persona:
        return jsonify('debe ser dict con alguno de los campos "nombre", "puesto", "correo" y "fecha_nacimiento"'), 400
    
    if not correo:
        return jsonify('proporcione un correo correcto'), 400
    if correo != nueva_persona['correo']:
        return jsonify('no se puede cambiar el correo'), 400
    
    conn, cursor = constants.genera_cursor()

    try:
        conn, cursor = constants.genera_cursor()
        SQL = """SELECT * FROM usuarios WHERE correo=%s;""" # Note: no quotes
        cursor.execute(SQL, (correo,)) # Note: no % operator
        resp = cursor.fetchone()
        

        
        if resp is not None:
            viejo = {
                'nombre': resp[0],
                'puesto': resp[1],
                'correo': resp[2],
                'fecha_nacimiento': resp[3]
            }

            SQL = """UPDATE usuarios (
                nombre,
                puesto, 
                correo,
                fecha_nacimiento
            ) SET (
                nombre = %(nombre)s,
                puesto = %(puesto)s,
                correo = %(correo)s,
                fecha_nacimiento = %(fecha_nacimiento)s
            ) WHERE correo = %(correo)s;""" # Note: no quotes
            cursor.execute(SQL,  {
                **viejo,
                **nueva_persona
            }) 
            conn.commit()
            cursor.close()
            conn.close()
            return jsonify({
                **viejo,
                **nueva_persona
            }), 200
        else:
            conn.commit()
            cursor.close()
            conn.close()
            return jsonify('no hay resultados'), 404

    except Exception as ex:
        traceback.print_exc()
        cursor.close()
        conn.close()
        return jsonify('error interno'), 500

def borra_persona(correo):
    if not correo:
        return jsonify('proporcione un correo correcto'), 400
  
    conn, cursor = constants.genera_cursor()

    try:
        conn, cursor = constants.genera_cursor()
        SQL = """SELECT * FROM usuarios WHERE correo=%s;""" # Note: no quotes
        cursor.execute(SQL, (correo,)) # Note: no % operator
        resp = cursor.fetchone()
        

        if resp is not None:
            SQL = """DELETE FROM usuarios WHERE correo = %s;""" # Note: no quotes
            cursor.execute(SQL, (correo,)) # Note: no % operator
            conn.commit()
            cursor.close()
            conn.close()
            return jsonify('usuario eliminado'), 200
        else:
            conn.commit()
            cursor.close()
            conn.close()
            return jsonify('no hay resultados'), 404

    except Exception as ex:
        traceback.print_exc()
        cursor.close()
        conn.close()
        return jsonify('error interno'), 500