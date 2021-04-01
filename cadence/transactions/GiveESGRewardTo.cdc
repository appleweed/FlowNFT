//import NonFungibleToken from "./NonFungibleToken.cdc"
import NonFungibleToken from 0x631e88ae7f1d7c20
//import ESGReward from 0xf8d6e0586b0a20c7
import ESGReward from 0xba491f1d217bb3e0

// This transction withdraws an NFT from AuthAccount and gives to
// another recepient's account.

transaction(recipient: Address, nftid: UInt64) {
    
    // local variable for storing the minter reference
    let collection: &ESGReward.Collection

    prepare(signer: AuthAccount) {

        // borrow a reference to the AuthAccount's private Collection
        self.collection = signer.borrow<&ESGReward.Collection>(from: ESGReward.CollectionStoragePath)
            ?? panic("Could not borrow a reference to the Collection")
    }

    execute {
        // get the public account object for the recipient
        let recipient = getAccount(recipient)

        // borrow the recipient's public NFT collection reference
        let receiver = recipient
            .getCapability(ESGReward.CollectionPublicPath)!
            .borrow<&{NonFungibleToken.CollectionPublic}>()
            ?? panic("Could not get receiver reference to the NFT Collection")

        // Get NFT
        let token <- self.collection.withdraw(withdrawID: nftid) as! @ESGReward.NFT

        // give to recepient
        receiver.deposit(token:<-token)

    }
}
