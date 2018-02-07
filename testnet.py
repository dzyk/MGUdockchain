# -*- coding: utf-8 -*-
import steembase
import steem

from steembase.account import PasswordKey
from steembase.account import PrivateKey


steembase.chains.known_chains['STEEM'] = {
    'chain_id': '79276aea5d4877d9a25892eaa01b0adf019d3e5cb12a97478df3298ccdd01673',
    'prefix': 'STX', 'steem_symbol': 'STEEM', 'sbd_symbol': 'SBD', 'vests_symbol': 'VESTS'
}
s = steem
client = s.Steem(
    ['https://testnet.steem.vc']
                                            )

owner_key = PasswordKey('mgu', '2018mgu2018', role="owner")
owner_pubkey = format(owner_key.get_public_key(), "STX")
active_key = PasswordKey('mgu', '2018mgu2018', role="active")
active_pubkey = format(active_key.get_public_key(), "STX")
posting_key = PasswordKey('mgu', '2018mgu2018', role="posting")
posting_pubkey = format(posting_key.get_public_key(), "STX")
memo_key = PasswordKey('mgu', '2018mgu2018', role="memo")
memo_pubkey = format(memo_key.get_public_key(), "STX")



account = s.account.Account('mgu', steemd_instance=client)
bal = account['sbd_balance']
account2 = s.account.Account('mgu23', steemd_instance=client)
bal2 = account2['sbd_balance']
print (bal)
print (bal2)
opk = str(owner_key.get_private_key())
apk = str(active_key.get_private_key())
ppk = str(posting_key.get_private_key())
mpk = str(memo_key.get_private_key())
w = s.wallet.Wallet(steemd_instance=client)
print ("mgu->mgu23 1 BSD")
w.setKeys({'memo':mpk, 'owner':opk, 'posting':ppk, 'active':apk})
client.transfer(to='mgu23', amount=1, asset='SBD', account='mgu')
account = steem.account.Account('mgu', steemd_instance=client)
bal = account['sbd_balance']
account2 = steem.account.Account('mgu23', steemd_instance=client)
bal2 = account2['sbd_balance']
print (bal)
print (bal2)

