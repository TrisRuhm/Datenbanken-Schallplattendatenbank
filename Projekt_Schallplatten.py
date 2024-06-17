#!C:\Program Files\Python38\python.exe
import json
from tinydb import TinyDB, Query
import streamlit as st

print ("Content-type: text/html")
print ()


db = TinyDB("schallplatten_db.json", encode="UTF_8")
table_object = db.table("vinyl_table")
items = table_object.search(Query().title.exists())
st.write("Die Datenbank hat ", len(items), " Einträge")
st.text_input("Titel Suche", key="item")
if st.session_state.item:
    item_query = st.session_state.item
    for i in table_object:
        vinyl_query = i.get((Query().title == item_query) | (Query().artist == item_query) | (Query().type == item_query))
    st.write("Titel: " + vinyl_query["title"] +" (" +vinyl_query["type"] + ")")
    st.write("Künstler: ", vinyl_query["artist"])
    st.write("Release: ", vinyl_query["release_date"])
    st.write("ISBN: ", vinyl_query["ISBN"])


st.table(table_object)



        #    vinyl_query["artist"]
        #    vinyl_query["release_date"]
        #    vinyl_query["publisher"]
        #    vinyl_query["isbn"]



# table_object.insert({"title": "Watch", "artist": "Manfred Mann's Earth Band", "release_date": "1978", "type": "Album", "publisher": "Petbrook Ltd.", "ISBN":"5-060051-332005"})

#import cgi
#import json
#import requests # https://requests.readthedocs.io/en/latest/user/quickstart/

#print("</p></div>")

#print('<div><p>')
#print('<form><label for="title">Titel:</label> <input type="text" id="title" name="new_title"><br><br>')
#print('<label for="artist">Künstler:</label> <input type="text" id="artist" name="new_artist"><br><br>')
#print('<label for="release_date">Release-Datum:</label> <input type="date" id="new_release_date" name="release_date"><br><br>')
#print('<label for="publisher">Label:</label> <input type="text" id="publisher" name="new_publisher"><br><br>')
#print('<label for="isbn">ISBN:</label> <input type="text" id="isbn" name="new_isbn"><br><br>')
#print('<input type="submit" value="Neuen Eintrag anlegen">')
#print('</form>')
#print('</p></div>')

#form = cgi.FieldStorage()

#if form.getvalue("new_title"):
#    new_title = form.getvalue("new_title")
#    new_artist = form.getvalue("new_artist")
#    new_release_date = form.getvalue("new_release_date")
#    new_publisher = form.getvalue("new_publisher")
#    new_isbn = form.getvalue("new_isbn")

#    table_object.insert({"title": new_title, "artist": new_artist, "release_date": new_release_date, "publisher": new_publisher, "isbn": new_isbn})

form = st.form("new_entry_form")
form.header("Neuer Eintrag")

form.text_input("Titel", key="new_title"),
form.text_input("Künstler", key="new_artist"),
form.text_input("Typ", key="new_type"),
form.date_input("Release-Datum", key="new_date"),
form.text_input("Label", key="new_publisher"),
form.text_input("ISBN", key="new_isbn"),
form.form_submit_button(label="Submit"),

if st.session_state.new_title:
    new_title = st.session_state.new_title
    new_artist = st.session_state.new_artist
    new_date = st.session_state.new_date
    new_type = st.session_state.new_type
    new_publisher = st.session_state.new_publisher
    new_isbn = st.session_state.new_isbn

    table_object.insert({"title": new_title, "artist": new_artist, "release_date": str(new_date), "type": new_type, "publisher": new_publisher, "isbn": new_isbn})



#        print("<h2>Titel:", title, "</h2>")
#        print("<p>")
#        if "artist" in table_object["vinyl_table"]:
#                    print("<strong>Künstler:</strong>")
#                    for i, artist in enumerate(table_object["vinyl_table"]["artist"]):
#                        print (artist)
#        if "artist" in data["artist"]:
#            print ("<strong>Autor:</strong>")

    #else:
    #    print ("<p>Titel nicht gefunden.</p>")
#print ("</body></html>")


#music = Query()
#print("<p>", table_object['vinyl_db']['title'][0], "</p>")


#new_items = [
#{
#            "title": "Watch",
#            "artist": "Manfred Mann's Earth Band",
#            "release_date": "1978",
#            "type": "Album",
#            "publisher": "Petbrook Ltd.",
#            "ISBN": "5-060051-332005"
#        },
#    {"title": "Rap über Hass", "artist": "K.I.Z", "release_date": "2021", "type": "Album", "publisher": "Vertigo/Capitol", "ISBN":"0602435587448"},
#    {"title": "Heroes", "artist": "David Bowie", "release_date": "1977", "type": "Album", "publisher": "RCA Victor"},
#    {"title": "30", "artist": "Adele", "release_date": "2021", "type": "Album", "publisher": "Columbia"}
#]
# table_object.insert_multiple(new_items)
