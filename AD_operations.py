from ldap3 import Server, Connection
from secrets_local import SVC_PW

def initialize_connection():


    server = Server("ldap://REDACTED_IP")

    conn = Connection(
        server,
        user="REDACTED_ACCOUNT",
        password=SVC_PW,
        auto_bind=True,   
    )

    print("Bound?", conn.bound)

    return conn

def search_user_AD(conn, sAMAccountName_search):
     
     
     conn.search(
                'REDACTED_BASE_DN', 
                    f'(&(ObjectClass=user)(objectCategory=Person)(sAMAccountName={sAMAccountName_search}))', 
                    attributes=['sAMAccountName', 'mail'],
    )
     return conn.entries
    