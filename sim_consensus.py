import random

class Transaction:
    def __init__(self,origin,recipient,amount):
        self.origin = origin
        self.recipient = recipient
        self.amount = amount

        self.ack = None

class Node:
    def __init__(self,uid,initialBalances):
        self.currentBalances = list(initialBalances)
        self.uid = uid
        self.spent = 0
        self.received = 0
        self.confirmedOutTransactions = []
        self.confirmedInTransactions = []

    def transactionArrived(self,transaction):
        if self.currentBalances[transaction.origin] >= transaction.amount:
            self.currentBalances[transaction.origin] -= transaction.amount
            self.currentBalances[transaction.recipient] += transaction.amount

            if transaction.ack is None:
                transaction.ack = self.uid
                peers[transaction.origin].spent += transaction.amount
                peers[transaction.recipient].received += transaction.amount
                peers[transaction.origin].confirmedOutTransactions.append(transaction)
                peers[transaction.recipient].confirmedInTransactions.append(transaction)

    def issueTransaction(self):
        if self.currentBalances[self.uid] == 0: return None

        outcome = random.random()

        if outcome >= issuingRate: return None

        origin = self.uid
        recipient = random.choice(range(len(self.currentBalances)))

        if recipient == self.uid:
            recipient = (recipient + 1) % len(self.currentBalances)

        amount = max(1,int(random.uniform(0,maxAmountRatio*self.currentBalances[self.uid])))

        return Transaction(origin,recipient,amount)

class EvilNode(Node):
    def issueTransaction(self):
        recipient = random.choice(range(len(self.currentBalances)))

        if recipient == self.uid:
            recipient = (recipient + 1) % len(self.currentBalances)

        return Transaction(self.uid,recipient,int(InitialBalance.min/3))

# Simulation parameters
class TransmissionTime: min,max = 1,2
class InitialBalance: min,max = 10,20

issuingRate = 0.01 # 1 transaction every 10 time units
maxAmountRatio = 0.5 # max 1/10th of the total wealth can be given away
peerNum = 20 # Total number of participants
evilPeersNum = 1
iterations = 1000

initialBalances = []
peers = []
eventQueue = [list() for _ in range(peerNum)]

for i in range(peerNum):
    amount = random.choice(range(InitialBalance.min,InitialBalance.max+1))
    initialBalances.append(amount)

print("Initial balances total: %d" % (sum(initialBalances)))

for i in range(peerNum-evilPeersNum):
    peers.append(Node(i,initialBalances))

for i in range(evilPeersNum):
    peers.append(EvilNode(peerNum-evilPeersNum+i,initialBalances))

for i in range(iterations):
    for p in peers:
        transaction = p.issueTransaction()
        if transaction:
            for q in peers:
                if q.uid == p.uid:
                    lag = 0
                else:
                    lag = random.choice(range(TransmissionTime.min,TransmissionTime.max+1))-1

                eventQueue[lag].append((q.uid,transaction))

    ts = eventQueue.pop(0)
    eventQueue.append([])

    for dst,transaction in ts:
        peers[dst].transactionArrived(transaction)

print("Final balances totals:")

for p in peers:
    print("Node %d: %d" % (p.uid,sum(p.currentBalances)))
    print("  %s > %d" % ("% 3d" % initialBalances[p.uid],p.received-p.spent))
    print("  %s" % " ".join((map(lambda q: "% 3d" % q.currentBalances[p.uid], peers))))

# for t in peers[49].confirmedInTransactions:
#     print("IN : From:% 3d - To:% 3d - % 3d - Confirmed by % 3d - %s" % (t.origin,t.recipient,t.amount,t.ack,t))
#
# for t in peers[49].confirmedOutTransactions:
#     print("OUT: From:% 3d - To:% 3d - % 3d - Confirmed by % 3d - %s" % (t.origin,t.recipient,t.amount,t.ack,t))
