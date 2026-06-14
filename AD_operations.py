from ldap3 import Server, Connection
from secrets_local import SVC_PW

def initialize_connection():


    server = Server("ldap://10.0.0.143")

    conn = Connection(
        server,
        user="svc_iamcli@idm.internal",
        password=SVC_PW,
        auto_bind=True,   
    )

    print("Bound?", conn.bound)

    return conn

def search_user_AD(conn, sAMAccountName_search):
     
     
     conn.search(
                'OU=TestUsers,OU=IDM_Lab,DC=idm,DC=internal', 
                    f'(&(ObjectClass=user)(objectCategory=Person)(sAMAccountName={sAMAccountName_search}))', 
                    attributes=['sAMAccountName', 'mail'],
    )
     return conn.entries
    