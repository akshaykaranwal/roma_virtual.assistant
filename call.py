# to hang up the call

import plivo

client = plivo.RestClient('<auth_id>','<auth_token>')

response = client.calls.delete(
    call_uuid='3a2e4c90-dcee-4931-8a59-f123ab507e60', )
print(response)

# to record a call

import plivo

client = plivo.RestClient('<auth_id>','<auth_token>')
response = client.calls.record(
    call_uuid='3a2e4c90-dcee-4931-8a59-f123ab507e60', )
print(response)



