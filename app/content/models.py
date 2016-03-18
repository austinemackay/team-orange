from flask import g

def get_all_content():
	return g.db.execute("SELECT * FROM content").fetchall()

#Get content by reading ID
def get_reading_content(reading_id):
	query = "SELECT * FROM content JOIN reading_content ON content.id = reading_content.content_id WHERE reading_content.reading_id = :id"
	return g.db.execute(query, {"id": reading_id}).fetchall()

#Get readings by content ID
def get_content_reading(content_id):
	query = "SELECT * FROM reading JOIN reading_content ON reading.id = reading_content.reading_id WHERE reading_content.content_id = :id"
	return g.db.execute(query, {"id": content_id}).fetchall()

def find_content(id):
	return g.db.execute('SELECT * FROM reading WHERE id = :id', {"id": id}).fetchone()

def add_content_to_db(name, creation_time,approved, content):
    query = '''
        INSERT INTO content (name, creation_time, approved, content)
        VALUES (:name, :creation_time, :approved, :content)
            '''
    cursor = g.db.execute(query, {"name":name,"creation_time":creation_time, "approved":approved, "content":content})
    g.db.commit()
    return cursor.rowcount

def all_content():
    cursor = g.db.execute('select * from content')
    return cursor.fetchall()