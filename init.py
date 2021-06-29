# WARNING: RUNING THIS WILL DELETE THE LDAP DATABASE
# Writen by Waylon Jepsen GSA June 29th 2021
# Inint Rreinitializes the LDAP database, Errasing all user, netgroup, and group data
#
import os
import ldap
import ldap.modlist as modlist
from pprint import pprint

server_uri = 'ldaps://massive'
connection = ldap.initialize(server_uri)
connection.simple_bind_s(ADMIN_DN,PASSWORD)

netgroup_search_base = NETGROUP_DN
user_search_base = USER_DN
group_search_base = GROUP_DN
user_criteria = "(objectClass=person)"
netgroup_criteria = "(objectClass=nisNetgroup)"
group_criteria = "(objectClass=posixGroup)"
attrs = ['*']


saftey = input("WARNING: RUNING THIS WILL ERASE THE LDAP DATABASE ARE YOU SURE YOU WANT TO PROCEED? y/n")
if saftey.lower() == 'y':

    try:
        ldap_users = connection.search_s(
                    user_search_base,
                    ldap.SCOPE_SUBTREE,
                    user_criteria,
                    attrs,
        )
        ldap_netgroups = connection.search_s(
                    netgroup_search_base,
                    ldap.SCOPE_SUBTREE,
                    netgroup_criteria,
                    attrs,
        )
        ldap_groups = connection.search_s(
                    group_search_base,
                    ldap.SCOPE_SUBTREE,
                    group_criteria,
                    attrs,

        )
    except ldap.LDAPError as e:
        print(e)

    #---------------------------------------------------Deleting Users------------------------------------------------------
    print("Deleting Users...")
    for user in ldap_users:
        try:
            connection.delete_s(user[0])
        except ldap.LDAPError as e:
            print(e)
    #--------------------------------------------------Deleting Netgroups---------------------------------------------------
    print("Deleting Netgroups...")
    for netgroup in ldap_netgroups:
        try:
            connection.delete_s(netgroup[0])
        except ldap.LDAPError as e:
            print(e)
    #-------------------------------------------------Deleting Unix Groups--------------------------------------------------
    print("Deleting Unix groups...")
    for group in ldap_groups:
        try:
            connection.delete_s(group[0])
        except ldap.LDAPError as e:
            print(e)

else:
    print("ABORTED")
try:
    ldap_users = connection.search_s(
                user_search_base,
                ldap.SCOPE_SUBTREE,
                user_criteria,
                attrs,
    )
    ldap_netgroups = connection.search_s(
                netgroup_search_base,
                ldap.SCOPE_SUBTREE,
                netgroup_criteria,
                attrs,
    )
    ldap_groups = connection.search_s(
        group_search_base,
        ldap.SCOPE_SUBTREE,
        group_criteria,
        attrs,

    )
except ldap.LDAPError as e:
    print(e)
print("There are currently {} user records in Ldap".format(len(ldap_users)))
print("There are currently {} netgroup records in Ldap".format(len(ldap_netgroups)))
print("There are currently {} unix group records in Ldap".format(len(ldap_groups)))

connection.unbind_s()
