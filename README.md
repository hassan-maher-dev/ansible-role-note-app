📝 Note-Taking App Deployment Role
Role Name
note_app

Description
An Ansible Role that automates the deployment of a Python Flask-based Note-Taking application on RedHat/Amazon Linux systems. It handles the installation of Python, Pip, and Flask, sets up the application as a systemd service, and configures the environment to run on Port 80.

Requirements
Operating System: Amazon Linux 2 or RHEL-based distributions.

Privileges: Root or sudo access is required to install packages and manage services.

Network: Inbound access to Port 80 (HTTP) must be allowed in the security group.

Role Variables
Currently, this role uses hardcoded paths for simplicity in the college project. However, you can modify:

DB_FILE: The location of the SQLite database (default is /opt/note_app/notes.db).

Port: The application is configured to bind to Port 80 within app.py.

Dependencies
None. This role is standalone and does not require other Galaxy roles to function.

Example Playbook
Including an example of how to use your role:

YAML
- hosts: web
  become: yes
  roles:
     - hassan_maher_dev.note_app
License
MIT

Author Information
Hassan Maher

Electronics & Communications Engineering Student.

Digital Egypt Builders Initiative (DEBI) - DevOps Track.
