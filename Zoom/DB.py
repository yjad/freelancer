import sqlite3
from config import config
MEETING_TABLE = "meetings"
ATTENDEES_TABLE = "attendees"


def open_db():
    connection = sqlite3.Connection(config.get("DB_FILE_NAME"))
    cursor = connection.cursor()
    return connection, cursor


def create_tables(cursor):
    cmd = f'CREATE TABLE IF NOT EXISTS {MEETING_TABLE}' \
          f'(uuid TEXT NOT NULL PRIMARY KEY,' \
          f'id INTEGER ,' \
          f'host_id	TEXT,' \
          f'type	INTEGER,' \
          f'topic	TEXT,' \
          f'user_name	TEXT,' \
          f'user_email TEXT,' \
          f'start_time TEXT,' \
          f'end_time	TEXT,' \
          f'duration	INTEGER,' \
          f'total_minutes	INTEGER,' \
          f'participants_count INTEGER)'
    cursor.execute(cmd)

    cursor.execute(f'CREATE TABLE IF NOT EXISTS {ATTENDEES_TABLE}'
                   '(meeting_uuid TEXT,'
                   'id TEXT ,'
                   'user_id TEXT,'
                   'name TEXT,'
                   'user_email TEXT,'
                   'join_time TEXT,'
                   'leave_time TEXT,'
                   'duration INTEGER,'
                   'attentiveness_score TEXT)')
    return


def close_db(cursor):
    cursor.close()


def insert_row(conn, cursor, table_name, rec):
    keys = ','.join(rec.keys())
    question_marks = ','.join(list('?' * len(rec)))
    values = tuple(rec.values())
    try:
        cursor.execute('INSERT INTO ' + table_name + ' (' + keys + ') VALUES (' + question_marks + ')', values)
        conn.commit()
        return 0
    except sqlite3.Error as er:
        #print('SQLite error: %s' % (' '.join(er.args)))
        #print("Exception class is: ", er.__class__)
        #print('SQLite traceback: ')
        #exc_type, exc_value, exc_tb = sys.exc_info()
        #print(traceback.format_exception(exc_type, exc_value, exc_tb))
        return -1


def insert_row_meeting(conn, cursor, rec):
    return insert_row(conn, cursor, MEETING_TABLE, rec)


def insert_row_attendees(conn, cursor, rec):
    return insert_row(conn, cursor, ATTENDEES_TABLE, rec)


def exec_query(cursor, cmd):
    cursor.execute(cmd)
    rows = cursor.fetchall()
    return rows


def get_last_meeting_date():
    conn, cursor = open_db()
    cursor.execute('SELECT start_time from meetings order by start_time DESC LIMIT 1')
    rows = cursor.fetchall()
    close_db(cursor)
    return rows[0][0][:10]

def get_col_names(conn, sql):
    get_column_names = conn.execute(sql + " limit 1")
    col_name = [i[0] for i in get_column_names.description]
    return col_name
