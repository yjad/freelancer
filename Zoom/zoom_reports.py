import os
from openpyxl import Workbook
from datetime import timedelta, datetime
from graph import plot_stacked_bar

from config import config
from DB import open_db, close_db, exec_query, get_last_meeting_date, get_col_names
from zoom import load_zoom_meetings


def query_to_excel(cmd, file_name, header=None):
    conn, cursor = open_db()
    rows = exec_query(cursor, cmd)
    close_db(cursor)

    if not header:
        header = get_col_names(conn, cmd)

    wb = Workbook()
    ws = wb.active
    ws.append(header)

    for row in rows:
        ws.append(row)
    wb.save(file_name)


def attendance_sheet(meeting_date):
    update_meetings()   # update meetings first
    if meeting_date:
        cmd = f""" SELECT SUBSTR(join_time,1, 10) as "meeting date", type, topic,  
                        a.user_email, name, sum(a.duration/60) as "duration in min" , 
                		Users.firstname, lastname, profile_field_manager_mon, profile_field_manager_wed, 
                        profile_field_group_id, profile_field_code
                        FROM attendees a 
						LEFT Join Users ON a.user_email = Users.email
						LEFT Join meetings m ON a.meeting_uuid = m.uuid
                        WHERE "meeting date" = "{meeting_date}"
                        GROUP BY a.user_email, name, "meeting date"
                        ORDER BY 1, 2, 3"""
    else:
        cmd = f"""SELECT SUBSTR(join_time,1, 10) as "meeting date", type, topic,  
                        a.user_email, name, sum(a.duration/60) as "duration in min" , 
                		Users.firstname, lastname, profile_field_manager_mon, profile_field_manager_wed, 
                        profile_field_group_id, profile_field_code
                        FROM attendees a 
						LEFT Join Users ON a.user_email = Users.email
						LEFT Join meetings m ON a.meeting_uuid = m.uuid
                        GROUP BY a.user_email,name, "meeting date"
                        ORDER BY 1, 2, 3"""

    header = ["meeting date", "meeting type", "meeting topic", "user_email", "Zoom name", "duration (min)", "firstname", "lastname",
              "profile_field_manager_mon",
              "profile_field_manager_wed", "profile_field_group_id", "profile_field_code"]

    if meeting_date:
        file_name = f".\\data\\attendees_{meeting_date}.xlsx"
    else:
        file_name = r".\data\attendees_all.xlsx"

    query_to_excel(cmd, file_name, header)


def list_unmatched_attendees():
    update_meetings()   # update meetings first
    cmd = f"""select substr(join_time,1, 10) as "meeting date", a.user_email, name, user_id, sum(a.duration/60) as "duration in min" 
        from attendees a 
        where a.user_email not in (SELECT email from Users)
        group by a.user_email,name, "meeting date"
        order by 1, 2, 3"""
    header = ["meeting date", "Zoom user_email", "Zoom name", "Zoom user_id", "duration"]
    file_name = r".\data\no_matching_attendees.xlsx"
    query_to_excel(cmd, file_name, header)


def stats_attendees():
    update_meetings()   # update meetings first
    cmd = f"""SELECT meeting_date, meeting_type, topic, COUNT(name), COUNT(firstname), COUNT(name) - COUNT(firstname) 
                FROM (
                    SELECT DATE(join_time) as meeting_date, type as meeting_type, topic,  name, firstname
                    FROM attendees a 
                    LEFT Join Users ON a.user_email = Users.email
                    LEFT Join meetings m ON a.meeting_uuid = m.uuid
                    GROUP BY meeting_date, name 
                    )
                GROUP BY meeting_date
                ORDER BY 1, 2, 3"""
    header = ["meeting date", "meeting_type", "topic", "# of attendees", "Acadmy", "External"]
    file_name = r".\data\stats_attendees.xlsx"
    query_to_excel(cmd, file_name, header)


def update_meetings():
    # get date of last saved meeting
    last_meeting = get_last_meeting_date()
    #date_time_obj = datetime.strptime(last_meeting, '%Y-%m-%d') +  timedelta(days=1)
    load_zoom_meetings(last_meeting)


def stats_attendees_graph():
    sql = f"""SELECT meeting_date, meeting_type, topic, COUNT(name), COUNT(firstname), COUNT(name) - COUNT(firstname) 
                    FROM (
                        SELECT DATE(join_time) as meeting_date, type as meeting_type, topic,  name, firstname
                        FROM attendees a 
                        LEFT Join students ON a.user_email = students.email
                        LEFT Join meetings m ON a.meeting_uuid = m.uuid
                        GROUP BY meeting_date, name 
                        )
                    GROUP BY meeting_date
                    ORDER BY 1, 2, 3"""
    comm, curspr = open_db()
    rows = exec_query(curspr,sql)
    close_db(curspr)
    bars1=[]
    bars2 = []
    names = []
    for row in rows:
        names.append(row[0])
        bars1.append(row[4])
        bars2.append(row[5])
    plot_stacked_bar(bars1, bars2, names, r".\data\attendess by date.png")
    
def attendees_per_month(file_name):
    #update_meetings()
    sql = f"""SELECT substr(meeting_date,1,7) as meeting_month, COUNT(name), COUNT(firstname), COUNT(name) - COUNT(firstname) 
                    FROM (
                        SELECT DATE(join_time) as meeting_date,  name, firstname
                        FROM attendees a 
                        LEFT Join students ON a.user_email = students.email
                        LEFT Join meetings m ON a.meeting_uuid = m.uuid
                        GROUP BY meeting_date, name 
                        )
                    GROUP BY meeting_month
                    ORDER BY 1"""
    comm, curspr = open_db()
    rows = exec_query(curspr, sql)
    close_db(curspr)
    bars1=[]
    bars2 = []
    names = []

    # plot last n lines
    for row in rows:
        names.append(row[0])    # meeting date
        bars1.append(row[1])    # count (first name) --> Academy students
        bars2.append(row[3])    # External Students
    plot_stacked_bar(bars1, bars2, names, file_name)


def attendees_per_day_of_week(file_name):
    #update_meetings()
    sql = f"""SELECT strftime('%w',meeting_date) as day_of_week, COUNT(name), COUNT(firstname), COUNT(name) - COUNT(firstname) 
                    FROM (
                        SELECT DATE(join_time) as meeting_date,  name, firstname
                        FROM attendees a 
                        LEFT Join students ON a.user_email = students.email
                        LEFT Join meetings m ON a.meeting_uuid = m.uuid
                        GROUP BY meeting_date, name 
                        )
                    GROUP BY day_of_week
                    ORDER BY 1"""
    comm, curspr = open_db()
    rows = exec_query(curspr, sql)
    close_db(curspr)
    bars1=[]
    bars2 = []
    names = ['Sunday', 'Monday', 'Tuesday', 'Wednesday ', 'Thursday', 'Friday', 'Saturday']

    # plot last n lines
    for row in rows:
        #names.append(row[0])    # meeting day
        bars1.append(row[1])    # count (first name) --> Academy students
        bars2.append(row[3])    # External Students
    plot_stacked_bar(bars1, bars2, names, file_name)


def attendees_last_2_month(file_name):
    #update_meetings()
    sql = f"""SELECT meeting_date, COUNT(name), COUNT(firstname), COUNT(name) - COUNT(firstname) 
                    FROM (
                        SELECT DATE(join_time) as meeting_date, type as meeting_type, topic,  name, firstname
                        FROM attendees a 
                        LEFT Join students ON a.user_email = students.email
                        LEFT Join meetings m ON a.meeting_uuid = m.uuid
                        WHERE DATE(join_time) > DATE('now', '-2 Month')
                        GROUP BY meeting_date, name 
                        )
                    GROUP BY meeting_date
                    ORDER BY 1"""
    comm, curspr = open_db()
    rows = exec_query(curspr, sql)
    close_db(curspr)
    bars1=[]
    bars2 = []
    names = []

    # plot last n lines
    for row in rows:
        names.append(row[0])    # meeting date
        bars1.append(row[1])    # count (first name) --> Academy students
        bars2.append(row[3])    # External Students
    plot_stacked_bar(bars1, bars2, names, file_name)


def zoom_stats_as_image():
    
    OUT_DIR = r"C:\Yahia\Home\Yahia-Dev\Python\freelancer\Zoom\data"
    #update_meetings()
    #attendees_last_2_month(os.path.join(OUT_DIR, "attendees_last_2_month.png"))
    attendees_per_month(os.path.join(OUT_DIR, "attendees_per_month.png"))
    #attendees_per_day_of_week(os.path.join(OUT_DIR,"attendees_per_day_of_week.png"))