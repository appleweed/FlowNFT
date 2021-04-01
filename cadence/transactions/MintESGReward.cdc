//import NonFungibleToken from "./NonFungibleToken.cdc"
import NonFungibleToken from 0x631e88ae7f1d7c20
//import ESGReward from 0xf8d6e0586b0a20c7
import ESGReward from 0xba491f1d217bb3e0

// This transction uses the NFTMinter resource to mint a new NFT.
//
// It must be run with the account that has the minter resource
// stored at path ESGReward.MinterStoragePath.

transaction(recipient: Address, data: {String : String}) {
    
    // local variable for storing the minter reference
    let minter: &ESGReward.NFTMinter

    prepare(signer: AuthAccount) {

        // borrow a reference to the NFTMinter resource in storage
        self.minter = signer.borrow<&ESGReward.NFTMinter>(from: ESGReward.MinterStoragePath)
            ?? panic("Could not borrow a reference to the NFT minter")
    }

    execute {
        // get the public account object for the recipient
        let recipient = getAccount(recipient)

        // borrow the recipient's public NFT collection reference
        let receiver = recipient
            .getCapability(ESGReward.CollectionPublicPath)!
            .borrow<&{NonFungibleToken.CollectionPublic}>()
            ?? panic("Could not get receiver reference to the NFT Collection")

        // mint the NFT and deposit it to the recipient's collection
        self.minter.mintNFT(recipient: receiver, metaData: data)
    }
}
