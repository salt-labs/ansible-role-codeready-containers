Role Name
=========

Ansible role that installs CodeReady Containers and optionally installs Ansible Tower into the CodeReady Containers OpenShift cluster.

Requirements
------------

This role has the following requirements:
    - Access to the URL to download the CodeReady release
    - Access to the URL to download the Ansible Tower release

Role Variables
--------------

A summary of default variables and descriptions is below. Further comments are available in `defaults/main.yml`.

| Name | Description | Default |
| :--- | :---------- | :------ |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |

Dependencies
------------

No external dependencies.

Example Playbook
----------------

```yaml
- hosts: servers

roles:
  - install-codeready-containers

vars:
crc_packages_state: present
crc_remove_packages: true
crc_enable_service: true
crc_enable_selinux: true
crc_copy_templates: true
crc_firewall_configure: true
crc_firewall_rules:
    - service: ssh
    - port: 3389
crc_users:
    - user: devops
    group: docker
crc_selinux_booleans:
    - name: ftp_home_dir
    state: true
    persistent: true
tags: crc
```

Usage Scenarios
---------------

| Scenario | Example |
| :------- | :------ |
| Install CodeReady Containers | |
| Install CodeReady Containers and enable remote cluster access | |
| Install CodeReady Containers, but do not | |
| Install CodeReady Containers and configure OC CLI only | |
| Remove CodeReady Containers | |
| Remove CodeReady Containers and perform a fresh Install | |

# TODO: COMPLETE DOCUMENTATION EXAMPLES


**Start a deployment**
```
ansible-playbook  -i inventory deploy-crc.yml  -K
```

**Setup crc and start deployment**
```
ansible-playbook  -i inventory deploy-crc.yml --tags setup_crc,start_crc_deployment  -K
```

**Download and install CRC**
```
ansible-playbook  -i inventory deploy-crc.yml --tags download_crc,extract_crc  -K
```

**Configure OpenShift cli**
```
ansible-playbook  -i inventory deploy-crc.yml --tags configure_oc_cli -K
```

**Configure HAPROXY**
```
ansible-playbook  -i inventory deploy-crc.yml --tags configure_ha_proxy  -K
```

**Configure dnsmasq**
```
ansible-playbook  -i inventory deploy-crc.yml --tags configure_dnsmaq  -K
```

**Get crc url and login info**
```
ansible-playbook  -i inventory deploy-crc.yml --tags get_codeready_info
```

**Delete deployment**
```
ansible-playbook  -i inventory deploy-crc.yml --extra-vars "delete_crc_deployment=true" -K
```

Debug info
----------
* During setup the new CodeReady Containers release tasks
  * `tail -f /tmp/crc_setup.log`
  * or `tail -f  tail -f ~/.crc/crc.log`

Flags
-----

License
-------

Apache 2.0

Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.

Developer Information
------------------

Further information about the role operation is available in the [developer guide](docs/develop.md)
