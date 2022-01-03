import sqlite3


# creating the dbase
def youtubeData():
    conn = sqlite3.connect("c:/Users/cyberxploit/Pictures/upload.db")
    c = conn.cursor()
    c.execute(
        "CREATE TABLE IF NOT EXISTS video (id INTEGER PRIMARY KEY, Date TEXT, VidID TEXT, VidTitle TEXT, \
            VidType TEXT, Status TEXT )"
    )
    conn.commit()
    conn.close()


def addRec(date, vidID, vidTitle, vidType, status):
    conn = sqlite3.connect("c:/Users/cyberxploit/Pictures/upload.db")
    c = conn.cursor()
    c.execute(
        "INSERT INTO video VALUES (NULL, ?, ?, ?, ?, ?)",
        (date, vidID, vidTitle, vidType, status),
    )
    conn.commit()
    conn.close()


def viewRec():
    conn = sqlite3.connect("c:/Users/cyberxploit/Pictures/upload.db")
    c = conn.cursor()
    c.execute("SELECT * FROM video")
    row = c.fetchall()
    conn.commit()
    conn.close()
    return row


def updateRec(id, date="", vidID="", vidTitle="", vidType="", status=""):
    conn = sqlite3.connect("c:/Users/cyberxploit/Pictures/upload.db")
    c = conn.cursor()
    c.execute(
        "UPDATE video SET Date=?, VidID=?, VidTitle=?, VidType=?, Status=? WHERE id=?",
        (date, vidID, vidTitle, vidType, status, id),
    )
    conn.commit()
    conn.close()


def searchRec(date="", vidID="", vidTitle="", vidType="", status=""):
    conn = sqlite3.connect("c:/Users/cyberxploit/Pictures/upload.db")
    c = conn.cursor()
    c.execute(
        "SELECT * FROM video WHERE Date=? OR VidID=? OR VidTitle=? OR VidType=? OR Status=? ",
        (date, vidID, vidTitle, vidType, status),
    )
    row = c.fetchall()
    conn.commit()
    conn.close()
    return row


def deleteRec(id):
    conn = sqlite3.connect("c:/Users/cyberxploit/Pictures/upload.db")
    c = conn.cursor()
    c.execute("DELETE FROM video WHERE id=?", (id,))
    conn.commit()
    conn.close()


youtubeData()
