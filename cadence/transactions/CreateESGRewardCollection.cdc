//import ESGReward from 0xf8d6e0586b0a20c7
import ESGReward from 0xba491f1d217bb3e0

// This transction creates an empty Collection for the account.

transaction() {

	let me: AuthAccount

    prepare(acct: AuthAccount) {

    	self.me = acct
        
        let capability = acct.getCapability<&ESGReward.Collection>(ESGReward.CollectionPublicPath)
        if (capability.borrow() != nil) {
        	panic("Account already has Collection.")
        }

    }

    execute {
        self.me.save(<-ESGReward.createEmptyCollection(), to: ESGReward.CollectionStoragePath)
        self.me.link<&ESGReward.Collection>(ESGReward.CollectionPublicPath, target: ESGReward.CollectionStoragePath)
        log("Added ESG Reward Collection.")
    }
}
