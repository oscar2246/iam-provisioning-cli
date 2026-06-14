from ldap3 import Server, Connection
import secrets_local

def initialize_connection():


    server = Server(f"ldap://{secrets_local.DC_host_ip}")

    conn = Connection(
        server,
        user=secrets_local.SVC_Account_AD,
        password=secrets_local.SVC_PW,
        auto_bind=True,   
    )

    print("Bound?", conn.bound)

    return conn

def search_user_AD(conn, sAMAccountName_search):
     
     
     conn.search(
                secrets_local.SEARCH_BASE, 
                    f'(&(ObjectClass=user)(objectCategory=Person)(sAMAccountName={sAMAccountName_search}))', 
                    attributes=['sAMAccountName', 'mail'],
    )
     return conn.entries
    