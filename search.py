import ldap
from pprint import pprint

server_uri = SERVER_URI
search_base = SEARCH_DN
uid = input("Enter UID: ")
search_filter = '(uid='+uid+')'
print(search_filter)
attrs = ['*']


connection = ldap.initialize(server_uri)
connection.simple_bind_s(ADMIN_DN,ADMINPASS_WORD)

try:
   results = connection.search_s(
    search_base,
    ldap.SCOPE_ONELEVEL,
    search_filter,
    attrs,

)
except ldap.LDAPErroras e:
  print(e)

connection.unbind()
pprint(results)
