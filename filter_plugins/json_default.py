#!/usr/bin/env python3

from ansible.errors import AnsibleFilterError
import json

class FilterModule(object):

        def filters(self):

                return {
                        'json_default': self.json_default,
                }

        def json_default(self, data):

                try:

                        result = json.loads(data)

                        if result is None:
                                raise ValueError

                        print("Valid JSON: {JSON}".format(JSON=data))

                except (ValueError, TypeError) as err:

                        print("Invalid JSON: {JSON}".format(JSON=data))

                        result = "{}"


                except Exception as err:
                        raise AnsibleFilterError('Unexpected exception: {} {}'.format(type(err), err))

                return result

if __name__ == "__main__":

        print("Validating JSON")
        print("")

        print("Test Valid JSON")
        data = '{ "key": "test_valid" }'
        result = FilterModule.json_default("", data)
        print("Result {RESULT}".format(RESULT=result))
        print("")

        print("Test Invalid JSON")
        data = '{ "key": "test_invalid"'
        result = FilterModule.json_default("", data)
        print("Result {RESULT}".format(RESULT=result))
        print("")
