//import ESGReward from 0xf8d6e0586b0a20c7
import ESGReward from 0xba491f1d217bb3e0
pub fun main(owner: Address, nftid: UInt64) : {String : String} {
	let nftOwner = getAccount(owner)  
	let capability = nftOwner.getCapability<&ESGReward.Collection>(ESGReward.CollectionPublicPath)

	let receiverRef = capability.borrow()
	  ?? panic("Could not borrow the receiver reference")
	let reward = receiverRef.borrowESGReward(id: nftid) 
	var val = reward?.metadataObj ?? {"error": "NFT DOES NOT EXIST!"}

	return val
}