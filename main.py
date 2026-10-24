from pyscript import document

def candidate_checker(e):
    club_members = ["inigo combong", "andi chua", "ruffalyn cuartero", "luna noemayr", "angelica kershaw"]

    f_name = document.getElementById('first_name').value
    l_name = document.getElementById('last_name').value

    candidate = f_name.strip() + ' ' + l_name.strip()
    member_checker = candidate.lower() in club_members

    messages = (
        f'Sorry {candidate}, your name is not on the list.',
        f'Congratulations {candidate}! You are now part of the Rainbow Catering Club!'
    )

    document.getElementById('result').innerHTML = messages[member_checker]
