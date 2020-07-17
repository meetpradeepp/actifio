ansible_ondemand_backup
======================

This is a ansible role to perform Actifio ondemand backup for any applications and VMs.

Requirements
--------------

Backup target appplications or VMs must have a SLA ID which means protected with template and profile within Actifio.

Empty job slot must be required to avoid ansble job failure. If the backup job queued within Actifio, ansible job will fail.

Need to adjuest pause seconds, retiries, delay seconds for your environment within tasks/main.yml.


Role Variables
--------------

Following variables are accepted/required for this role. 

### Actifio Applinace Related 

| Variable Name    | Description | Required (Y/N) |
|------------------|---|---|
| act_appliance    | Actifio Appliance IP or FQDN. | Y               |
| act_user         | Actifio username. This should be a Actifio user with System Manage priviledges | Y
| act_pass         | Password for the Actifio User | Y
| act_vendorkey    | Vendor key can be obtained by the customer through opening a Support Case with the CSE. | Y
| act_appname 	   | Target Application/VM name | Y
| act_hostname     | Host Name running the application | Y (If the backup target is application.)
| act_esxhost      | ESXi Host Name running the VM | Y (If the backup target is VM.)
| act_imagelabel   | Label for backup image. Default is 'Ansible_Playbook'. | N
| act_backuptype   | If the target application is Oracle or SQL database, choose db/log/dblog. | N
| act_policyname   | Policy name for issuing backup job. If not specified, the first defined policy within template will be used. | N


Example Playbook
----------------

### Backup an Application Example

```
- name: testng backup app
  hosts: "{{ host_group }}"
  become: yes
  become_method: sudo
  roles:
    - { role: ansible_ondemand_backup, act_appliance: my-actifio, act_user: ansible, act_pass: mypassword }
  vars:
    act_vendorkey: "{{ contact CSE to get yours }}"
    act_appname: "TargetApp"
    act_hostname: "TargetHost"

```


License
-------

Copyright 2018 <Hiroshi Takeuchi hiroshi.takeuchi@actifio.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
