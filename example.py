# coding=utf-8


import pyota_api
from pyota_api.driver import Session
import pandas as pd
from Crypto.Cipher import AES
import Crypto


import random
import string
from iota import Address
from pyota_api import Session
from pyota_api.ciphers import Ed25519Cipher
from pyota_api.ciphers import RSACipher
from pyota_api.mam_lite import MAML_Ed25519
import nacl.encoding
import nacl.signing

session = Session(conn='https://durian.iotasalad.org:14265')

mam_stream_1 = session.open_mam_stream()
mam_stream_2 = session.open_mam_stream()


prikey1, pubkey1 = Ed25519Cipher.generate_keys()
prikey2, pubkey2 = Ed25519Cipher.generate_keys()
mam_stream_1.add_trusted_pubkey('test', pubkey1)
mam_stream_2.add_trusted_pubkey('test', pubkey2)





MAML_Ed25519(root_address=addr_test,channel_password='test_pass')
mam_stream_2 = MAML_Ed25519(root_address=addr_test,channel_password='test_pass')


addr_test = 

Address(''.join(random.choices(string.ascii_uppercase + '9', k=81)))





# generate pubkey and make it trusted
prikey, pubkey = Ed25519Cipher.generate_keys()
mam_stream_1.add_trusted_pubkey('test', pubkey)
mam_stream_2.add_trusted_pubkey('test', pubkey)

# write with first MAML stream
mam_stream_1.write('data_to_be_sent', pubkey, prikey)

# read and validate with another
read_res = mam_stream_2.read()

# split the channel
mam_stream_1.split_channel('test_pass_2')

# write new msg to new channel
write_res = mam_stream_1.write('data_to_be_sent_2', pubkey, prikey)

# switch the channel on second stream
mam_stream_2.split_channel('test_pass_2')

# read msg in second stream
read_res = mam_stream_2.read()






host_seed = 'SEED9GOES9HERE'
guest_seed = '9SENDTOSEED'
filename = "VehicleService.csv"

dframe = pd.read_csv(filename, delimiter=';', dtype=str, nrows=8)
#session = Session(seed=host_seed, conn='https://durian.iotasalad.org:14265')

session = Session(conn='https://durian.iotasalad.org:14265')
session.data_to_tangle(data='Hello Tangle!', tag='TEST')


session.data_to_tangle(data=dframe, tag='CSV')




addr = session.convert_into_address(filename, 'JG&^F&*gewh43y56GF&*^%F*(g4t5y')

#
#for index, row in dframe.iterrows():
#    session.data_to_tangle(data=row.to_json(), tag='CSV')

#







#conn_nodes = conn.get_active_full_nodes(host_seed, 4)
#
#
#
#
#
#
#
#iota_node_ip_1 = 'https://iotanode.us:443'
#iota_node_ip_2 = 'https://peanut.iotasalad.org:14265'
#iota_node_ip_3 = 'https://potato.iotasalad.org:14265'
#iota_node_ip_4 = 'https://tuna.iotasalad.org:14265'
#iota_node_ip_5 = 'https://durian.iotasalad.org:14265'
#
#host_seed = 'SEED9GOES9HERE'
#guest_seed = '9SENDTOSEED'
#
#api = Iota(iota_node_ip_3, host_seed)
## api2 = Iota(iota_node_ip, guest_seed)
#
#in_address = Addr.generate_address()
#
#value = 0
#message = "SomeMSG98765"
#
#
#print('Full Node Status: ' + str(api.get_node_info()))
#result = api.send_transfer(
#        transfers=[
#                    ProposedTransaction(
#                        address=in_address,
#                        value=value,
#                        tag="AIRCOINTW",
#                        message =TryteString.from_string(message)
#                    )
#                ]
#)
#
#for bundle in result.values():
#    print('--------------------')
#    print('Bundle hash: ' + str(bundle.hash))
#    print('Bundle confirmation: ' + str(bundle.is_confirmed))
#    for transaction in bundle.transactions:
#        i = transaction.current_index + 1
#        print('--------------------')
#        print(f'    Tx{i} hash: ' + str(transaction.hash))
#        print(f'    Tx{i} address: ' + str(transaction.address))
#        print(f'    Tx{i} value: ' + str(transaction.value))
#        print(f'    Tx{i} message: ' + str(transaction.signature_message_fragment.decode()))
#        print(f'    Tx{i} tag: ' + str(transaction.tag))
#        print(f'    Tx{i} nonce: ' + str(transaction.nonce))
#        print(f'    Tx{i} branch hash: ' + str(transaction.branch_transaction_hash))
#        print(f'    Tx{i} trunk hash: ' + str(transaction.trunk_transaction_hash))
#        print(f'    Tx{i} timestamp: ' + str(transaction.timestamp))