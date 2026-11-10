from pyscript import document

# Everyone who's in the club
members = ['Franchesca Dela Rosa', 'Miguel Jimenez', 'Gurleen Kaur', 'Jesse Villante',
 'Destiny Reyes', 'Vita De Guzman', 'Santiago Valdez', '3rdy Mercado',
 'MJ Madrelejos', 'Julia Hadji Gapor', 'Chalanie Lumbang', 'Raver Estacio']


def check_student(event):
    first = document.getElementById('first_name').value.strip()
    last = document.getElementById('last_name').value.strip()
    name = f"{first} {last}"

    # True = they're on the list, False = they're not
    replies = {
        True: f"Hello, {name} Your in the club!",
        False: f"Unfortunately, {name} is not on the list.",
    }

    document.getElementById('output').innerText = replies[name in members]
