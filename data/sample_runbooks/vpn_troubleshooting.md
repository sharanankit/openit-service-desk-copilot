# Runbook: VPN Connection Troubleshooting

**Document ID:** KB-IT-001  
**Category:** Network and Remote Access  
**Audience:** L1 IT Service Desk  
**Version:** 1.0  
**Status:** Approved for this synthetic project

## Symptoms

- The user cannot connect to the corporate VPN.
- The VPN reports authentication failure after a password change.
- The VPN client repeatedly requests credentials.

## Troubleshooting Procedure

1. Confirm that the device has an active internet connection.
2. Ask the user to verify that they are entering their current corporate credentials.
3. If the password was recently changed, close the VPN client and reopen it before attempting to authenticate again.
4. If the client offers a saved-credentials option, follow the organization's approved procedure for refreshing stored credentials. Do not ask the user to disclose their password.
5. Record the exact error message and the time the failure occurred.
6. If the issue persists, escalate to the network support team with the error message, VPN client version, operating system, and troubleshooting steps already attempted.

## Security Notes

- Never request or record a user's password.
- Do not disable multifactor authentication.
- Do not bypass corporate access controls.
- Do not install unapproved VPN software.

## Escalation Criteria

Escalate when authentication continues to fail after approved basic checks, multiple users are affected, or the client reports a server or certificate error requiring network-team investigation.

## Source Limitations

This is synthetic training content, not a real organization's approved procedure. Validate any operational procedure with the relevant IT team before using it in a real environment.