import ldap
import ldap.modlist as modlist
import crypt
server=SERVER_URI
# Open a connection
l = ldap.initialize(server)
# Bind/authenticate with a user with apropriate rights to add objects
l.simple_bind_s(ADMIN_DN, PASS_WORD)

# The dn of our new entry/object
dn=USER_DN

# A dict to help build the "body" of the object
attrs = {'cn': [b'Test User'],
    'gecos': [b'Test User'],
    'gidNumber': [b'1557'],
    'givenName': [b'Test'],
    'homeDirectory': [b'/Test'],
    'loginShell': [b'/bin/bash'],
    'mail': [b'test@mail.com'],
    'objectClass': [b'person',
                   b'organizationalPerson',
                   b'inetOrgPerson',
                   b'posixAccount',
                   b'top'],
    'sn': [b'User'],
    'uid': [b'tuser'],
    'uidNumber': [b'8000'],
}

passwrd ="{crypt}" + crypt.crypt("123456789", crypt.mksalt(crypt.METHOD_SHA512))
print(passwrd)
# Convert our dict to nice syntax for the add-function using modlist-module
ldif = modlist.addModlist(attrs)
l.add_s(dn,ldif)

l.undind_s()
