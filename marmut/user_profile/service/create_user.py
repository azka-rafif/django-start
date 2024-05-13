import uuid
from django.db import connection, IntegrityError


def create_user(email, password, nama, gender, tempat_lahir, tanggal_lahir, kota_asal) -> str:
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO marmut.akun (email, password, nama, gender, tempat_lahir, tanggal_lahir, is_verified, kota_asal) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                [email, password, nama, gender, tempat_lahir,
                    tanggal_lahir, False, kota_asal]
            )
        return
    except IntegrityError:
        return "Email already exists. Please choose a different email."


def create_user_role(roles, user_email) -> str:
    id = uuid.uuid4()
    if len(roles) == 0:
        return "no roles selected"
    for role in roles:
        with connection.cursor() as cursor:
            if role == "podcaster":
                cursor.execute("INSERT INTO marmut.podcaster (email) "
                               "VALUES (%s)",
                               [user_email]
                               )
            if role == "artist":
                hak_cipta_artist = uuid.uuid4()
                cursor.execute("INSERT INTO marmut.pemilik_hak_cipta (id, rate_royalti) "
                               "VALUES (%s, %s)",
                               [hak_cipta_artist, 2_000_000])
                cursor.execute("INSERT INTO marmut.artist (id, email_akun, id_pemilik_hak_cipta) "
                               "VALUES (%s, %s, %s)",
                               [id, user_email, hak_cipta_artist])
            if role == "songwriter":
                hak_cipta_songwriter = uuid.uuid4()
                cursor.execute("INSERT INTO marmut.pemilik_hak_cipta (id, rate_royalti) "
                               "VALUES (%s, %s)",
                               [hak_cipta_songwriter, 2_000_000])
                cursor.execute("INSERT INTO marmut.songwriter (id, email_akun, id_pemilik_hak_cipta) "
                               "VALUES (%s, %s, %s)",
                               [id, user_email, hak_cipta_songwriter])
    return ""
