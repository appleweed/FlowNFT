## 👋 Hi!

This repo contains a Flow contract (ESGReward) to mint NFTs on the Flow blockchain, along with supporting transactions and scripts. 

## Contracts

ESGReward.cdc: This the only contract of concern. It inherits from Flow's NonFungibleToken.cdc contract.
NonFungibleToken.cdc: Flow's default NFT contract.

## Transactions

CreateESGRewardCollection.cdc: To create an empty NFT Collection for a specific account.
MintESGReward.cdc: To mint a new NFT and place in a specific account. Requires an admin account that owns the ESGReward contract.
GiveESGRewardTo.cdc: Transfers an NFT from an owner account to a specified recepient account.

## Scripts

CheckTokenMetadata.cdc: Returns the associated metadata for the NFT in an owner's Collection given the account address and NFT's ID.
GetAllCollectionIDs.cdc: Returns all the NFT ID's in an owner's Collection given the account address.

## Tests

Note: Requires Python 3.x

1. Open ./tests.py and update the following defaults:

ADMIN = u'emulator-account' // Account with the ESGReward Contract
ADMIN_ADDRESS = u'0xf8d6e0586b0a20c7' // Corresponding Admin account address
RECEPIENT_SIGNER = u'my-test-account' // Target recepient account name to run tests
RECEPIENT_ADDRESS = u'0x39bf847ca5ad3c1c' // Target recepient account address to run tests
HOST = u'localhost:3569' // Emulator, or use Testnet: access.testnet.nodes.onflow.org:9000

2. Run tests: python ./tests.py

## Contact

Questions? Contact me at omar [atta] eastsidegames.com. Thanks!
