Role Name
=========

Ansible role that installs CodeReady Containers.

Requirements
------------

This role has the following requirements:
    - Access to the URL to download the CodeReady release

Role Variables
--------------

Descriptions on the available variables can be found in the `defaults/main` directory.

Dependencies
------------

No external dependencies.

Example Playbook
----------------

```yaml
TODO: PROVIDE EXAMPLE PLAYBOOKS
```

Usage Scenarios
---------------

# TODO: COMPLETE DOCUMENTATION EXAMPLES

| Scenario | Example |
| :------- | :------ |
| Install CodeReady Containers | |
| Install CodeReady Containers and enable remote cluster access | |
| Install CodeReady Containers, but do not | |
| Install CodeReady Containers and configure OC CLI only | |
| Remove CodeReady Containers | |
| Remove CodeReady Containers and perform a fresh Install | |

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

```bash
tail -F ~/.crc/crc.log
```

Flags
-----

License
-------

Apache 2.0

Author Information
------------------

Salt Labs

Developer Information
------------------

Further information about the role operation is available in the [developer guide](docs/develop.md)
