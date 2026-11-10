from pyscript import display, document
grade7 = {'Brad Pitt', 'Will Smith', 'Josua Oritz'}
grade8 = {'Lebron James', 'Freddy Fazbear'}
grade9 = {'Scott Pilgrim', 'Don TOliver'}
grade10 = {'Isaac Newton', 'Bill Ding'}
members = grade7 | grade8 | grade9 | grade10

def add_member(event): # adding member
    first = document.getElementById("first_name").value
    last = document.getElementById("last_name").value
    members.add(first + " " + last)
    document.getElementById("output").innerHTML = f"{members} Total Members: {len(members)}"