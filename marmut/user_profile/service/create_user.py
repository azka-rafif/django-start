import uuid
from django.db import connection,IntegrityError

def create_user(email, password, nama, gender, tempat_lahir, tanggal_lahir, kota_asal) -> str:
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO marmut.akun (email, password, nama, gender, tempat_lahir, tanggal_lahir, is_verified, kota_asal) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                [email, password, nama, gender, tempat_lahir, tanggal_lahir, False, kota_asal]
            )
        return 
    except IntegrityError:
         return "Email already exists. Please choose a different email."


def create_user_role(roles, user_email) -> str:
    hak_cipta_id = uuid.uuid4()
    id = uuid.uuid4()
    if len(roles) == 0:
        return "no roles selected"
    for role in roles:
        with connection.cursor() as cursor:
            
            if role == "podcaster":
                cursor.execute("INSERT INTO marmut.podcaster (email) "
                        "VALUES (%s)",
                         [ user_email]
                         )
            if role == "artist":
                cursor.execute("INSERT INTO marmut.artist (id, email_akun, id_pemilik_hak_cipta) "
                            "VALUES (%s, %s, %s)",
                             [id, user_email, hak_cipta_id])
            if role == "songwriter":
                cursor.execute("INSERT INTO marmut.songwriter (id, email_akun, id_pemilik_hak_cipta) "
                            "VALUES (%s, %s, %s)",
                             [id, user_email, hak_cipta_id])
    return "OK"