# Test script. Runs unit tests in order.
#
# Required: 
# - Flow CLI
# - Deployed ESGReward.cdc contract.
# - ADMIN account
# - RECEPIENT account
#
# Usage: Run from top parent directory of Flow project.
#
# Tests:
# 1. Create empty NFT Collection in RECEPIENT account.
# 2. Run again to check that new NFT Collection exists in RECEPIENT account.
# 3. Create another empty NFT Collection in ADMIN's account.
# 4. Mint new NFT and move into RECEPIENT account's Collection.
# 5. Mint a second new NFT and move into ADMIN's account Collection.
# 6. Retrieve metadata of new NFT from recepient account's Collection.
# 7. Move NFT from ADMIN's Collection to RECEPIENT's Collection.
# 8. Retrieve all NFT IDs from RECEPIENT's Collection.
import os

# Defines. Change these per environment.
MAIN_CONTRACT = u'./cadence/contracts/ESGReward.cdc'
NEW_COLLECTION_SCRIPT = u'./cadence/transactions/CreateESGRewardCollection.cdc'
MINT_SCRIPT = u'./cadence/transactions/MintESGReward.cdc'
CHECK_TOKEN_SCRIPT = u'./cadence/scripts/CheckTokenMetadata.cdc'
DEPOSIT_TOKEN_SCRIPT = u'./cadence/transactions/GiveESGRewardTo.cdc'
GET_ALL_IDS = u'./cadence/scripts/GetAllCollectionIDs.cdc'
#ADMIN = u'emulator-account'
#ADMIN_ADDRESS = u'0xf8d6e0586b0a20c7'
ADMIN = u'omar-account'
ADMIN_ADDRESS = u'0xba491f1d217bb3e0'
RECEPIENT_SIGNER = u'my-test-account'
RECEPIENT_ADDRESS = u'0x39bf847ca5ad3c1c'
#HOST = u'localhost:3569'
HOST = u'access.testnet.nodes.onflow.org:9000'

# Pause to start tests...
raw_input("Press Enter to start tests...")


#####################################################
# 1. Create empty NFT Collection in RECEPIENT account.
# Note: RECEPIENT_SIGNER gets new empty Collection.
cmd = u'flow transactions send --code {} --signer {} --host {} --results'.format(NEW_COLLECTION_SCRIPT, RECEPIENT_SIGNER, HOST)

# Submit transaction to Flow
print(u'\n1. Creating new Collection for RECEPIENT account. Will panic() if already exists...\n')
#print(cmd)
#print(u'\n\n')
val = os.system(cmd)
print(u'Return: {}'.format(val))

raw_input("Press Enter to continue...")

#####################################################
# 2. Run again to check that new NFT Collection exists in RECEPIENT account.
# Note: This will cause a panic() at the existence of the Collection.

# Submit transaction to Flow
print(u'\n2. Checking that new Collection exists in RECEPIENT account. Should panic()...\n')
#print(cmd)
#print(u'\n\n')
val = os.system(cmd)
print(u'Return: {}'.format(val))

raw_input("Press Enter to continue...")

#####################################################
# 3. Create another empty NFT Collection in ADMIN's account.
cmd = u'flow transactions send --code {} --signer {} --host {} --results'.format(NEW_COLLECTION_SCRIPT, ADMIN, HOST)

# Submit transaction to Flow
print(u'\n3. Creating new Collection for ADMIN account...\n')
#print(cmd)
#print(u'\n\n')
val = os.system(cmd)
print(u'Return: {}'.format(val))

raw_input("Press Enter to continue...")

#####################################################
# 4. Mint new NFT and move into RECEPIENT account's Collection.
# Note: Requires ADMIN to sign.

# NFT Metadata
# Note: This is formed as a string because Python otherwise thows "unhashable type" with embedded "key" and "value" properties.
metadata = u'\
	{ \
		"key": { \
			"type": "String", \
			"value": "name"	\
		}, \
		"value": { \
			"type": "String", \
			"value": "Drop Beats Launchpad Demo" \
		} \
	}, \
	{ \
		"key": { \
			"type": "String", \
			"value": "rating" \
		}, \
		"value": { \
			"type": "String", \
			"value": "5" \
		} \
	}, \
	{ \
		"key": { \
			"type": "String", \
			"value": "uri" \
		}, \
		"value": { \
			"type": "String", \
			"value": "ipfs://QmZGJhDdTdRD8dEE2c4AeJZukXZgBph9GrpF9vf5ZZpNtt" \
		} \
	}'

args = u'[{{"type":"Address", "value": "{}"}}, {{"type":"Dictionary", "value": [{}]}}]'.format(RECEPIENT_ADDRESS, metadata)
cmd = u'flow transactions send --code {} --signer {} --host {} --args \'{}\' --results'.format(MINT_SCRIPT, ADMIN, HOST, args)

# Submit transaction to Flow
print(u'\n4. Minting new NFT and placing in RECEPIENT\'s Collection...\n')
#print(cmd)
#print(u'\n\n')
val = os.system(cmd)
print(u'Return: {}'.format(val))

raw_input("Press Enter to continue...")

#####################################################
# 5. Mint a second new NFT and move into ADMIN's account Collection.
# Note: Requires ADMIN to sign.

# NFT Metadata
# Note: This is formed as a string because Python otherwise thows "unhashable type" with embedded "key" and "value" properties.
metadata = u'\
	{ \
		"key": { \
			"type": "String", \
			"value": "name"	\
		}, \
		"value": { \
			"type": "String", \
			"value": "Another movie" \
		} \
	}, \
	{ \
		"key": { \
			"type": "String", \
			"value": "rating" \
		}, \
		"value": { \
			"type": "String", \
			"value": "1" \
		} \
	}, \
	{ \
		"key": { \
			"type": "String", \
			"value": "uri" \
		}, \
		"value": { \
			"type": "String", \
			"value": "ipfs://QmVPQmd6uf8o3HFptjwgMeEJS5YwsBX2AWp8RvdyXsQ1gy" \
		} \
	}'

args = u'[{{"type":"Address", "value": "{}"}}, {{"type":"Dictionary", "value": [{}]}}]'.format(ADMIN_ADDRESS, metadata)
cmd = u'flow transactions send --code {} --signer {} --host {} --args \'{}\' --results'.format(MINT_SCRIPT, ADMIN, HOST, args)

# Submit transaction to Flow
print(u'\n5. Minting another NFT and placing in ADMIN\'s Collection...\n')
#print(cmd)
#print(u'\n\n')
val = os.system(cmd)
print(u'Return: {}'.format(val))

raw_input("Press Enter to continue...")

############################################################
# 6. Retrieve metadata of new NFT from recepient account's Collection.
# Note: Change nftid to match the ID of the NFT to retrieve.
nftid = 1 
args = u'[{{"type":"Address", "value": "{}"}}, {{"type":"UInt64", "value": "{}"}}]'.format(RECEPIENT_ADDRESS, nftid)
cmd = u'flow scripts execute --code={} --host {} --args \'{}\''.format(CHECK_TOKEN_SCRIPT, HOST, args)

# Submit transaction to Flow
print(u'\n6. Checking newly created NFT in RECEPIENT\' Collection...\n')
#print(cmd)
#print(u'\n\n')
val = os.system(cmd)
print(u'Return: {}'.format(val))

############################################################
# 7. Move NFT from ADMIN's Collection to RECEPIENT's Collection.
# Note: Change nftid to match the ID of the NFT to retrieve.
nftid = 2
args = u'[{{"type":"Address", "value": "{}"}}, {{"type":"UInt64", "value": "{}"}}]'.format(RECEPIENT_ADDRESS, nftid)
cmd = u'flow transactions send --code {} --signer {} --host {} --args \'{}\' --results'.format(DEPOSIT_TOKEN_SCRIPT, ADMIN, HOST, args)

# Submit transaction to Flow
print(u'\n7. Moving admin\'s NFT to RECEPIENT\'s Collection...\n')
#print(cmd)
#print(u'\n\n')
val = os.system(cmd)
print(u'Return: {}'.format(val))

############################################################
# 8. Retrieve all NFT IDs from RECEPIENT's Collection.

args = u'[{{"type":"Address", "value": "{}"}}]'.format(RECEPIENT_ADDRESS)
cmd = u'flow scripts execute --code={} --host {} --args \'{}\''.format(GET_ALL_IDS, HOST, args)

# Submit transaction to Flow
print(u'\n8. Retrieving all NFT Collection IDs from RECEPIENT...\n')
#print(cmd)
#print(u'\n\n')
val = os.system(cmd)
print(u'Return: {}'.format(val))
