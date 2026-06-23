from ldap3 import Server, Connection
from ldap3.utils.conv import escape_filter_chars
import secrets_local

def initialize_connection():


    server = Server(f"ldap://{secrets_local.DC_host_ip}")

    conn = Connection(
        server,
        user=secrets_local.SVC_Account_AD,
        password=secrets_local.SVC_PW,
        auto_bind=True,   
    )

    return conn

def search_user_AD(conn, sAMAccountName_search):
     
     safe_name = escape_filter_chars(sAMAccountName_search)
     conn.search(
                secrets_local.SEARCH_BASE, 
                    f'(&(ObjectClass=user)(objectCategory=Person)(sAMAccountName={safe_name}))', 
                    attributes=['sAMAccountName', 'mail', 'userAccountControl'],
    )

     return conn.entries

def check_email_existence(conn, Email):
     
     safe_name_email = escape_filter_chars(Email)

     conn.search(
          secrets_local.SEARCH_BASE,
          f'(&(ObjectClass=user)(ObjectCategory=Person)(mail={safe_name_email}))'
     )
     return bool(conn.entries)

def check_lan_existence(conn, lan):
     
     safe_name_lan = escape_filter_chars(lan)

     conn.search(
          secrets_local.SEARCH_BASE,
          f'(&(ObjectClass=user)(ObjectCategory=Person)(sAMAccountName={safe_name_lan}))'
     )
     return bool(conn.entries)
