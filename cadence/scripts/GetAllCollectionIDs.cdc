//import ESGReward from 0xf8d6e0586b0a20c7
import ESGReward from 0xba491f1d217bb3e0

pub fun main(owner: Address) : [UInt64] {
	let nftOwner = getAccount(owner)  
	let capability = nftOwner.getCapability<&ESGReward.Collection>(ESGReward.CollectionPublicPath)

	let receiverRef = capability.borrow()
	  ?? panic("Could not borrow the receiver reference")

	return receiverRef.getIDs()
}