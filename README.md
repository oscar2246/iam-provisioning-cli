# IAM Provisioning CLI

A command-line tool for provisioning and managing user identities, built as part of a home lab IAM/IGA portfolio.

## What it does

- Creates user accounts with collision-safe LANID and email generation
- Enables and disables accounts with status guards (prevents redundant state changes)
- Logs every lifecycle event (create, enable, disable) with timestamps to an audit trail
- Searches live Active Directory users via LDAP

## Stack

- Python 3
- ldap3 (LDAP/Active Directory integration)
- Active Directory (Windows Server 2022, home lab domain)
- JSON persistence layer

## Architecture

| File | Responsibility |
|---|---|
| `main.py` | Menu / entry point |
| `user_ops.py` | User lifecycle operations |
| `storage.py` | JSON persistence and audit logging |
| `AD_operations.py` | Active Directory LDAP operations |

## Lab environment

- Domain controller: Windows Server 2022
- Directory: Active Directory (`idm.internal`)
- Python connects via a least-privilege service account (`svc_iamcli`) scoped to the `TestUsers` OU
