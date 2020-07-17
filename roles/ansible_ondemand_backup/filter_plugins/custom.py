__author__ = 'Hiroshi Takeuchi'
from ansible import errors

def get_policy_id (values, policyname):
    from ansible import errors
    import json
    
    if len(values['json']['result']) == 1 or policyname == '':
        return values['json']['result'][0]['id']
    else:
        for rslts in values['json']['result']:
            if rslts['name'] == policyname:
                break
        return  rslts['id']

class FilterModule(object):
    def filters(self):
        return {
            'get_policy_id': get_policy_id
        }

