# Blockchain Network Simulator

This short Python3 script simulates a network of nodes that broadcast transactions. This transactions moves tokens from each node's wallet to a recipient's wallet. The time a transaction takes to get to any node on the network is uniformly sampled from an interval of time intervals rangin from *min* to *max*.

Nodes can act honestly or maliciously. An honest node will never issue a transaction whose value is greater than the current balance of the wallet. Conversely, a malicious node will issue as many transactions as it can in order to try to subvert the consensus of the network.

Without a proper consensus protocol run by the nodes the simulation shows that:

1. with no malicious nodes, whenever *max* > *min* the likelihood of differences between each node's ledger (and, ultimately, in the wallet's balances) increases.
2. malicious nodes can spend more than they actually posses if *max* > *min*.

You can adjust the propagation latency over the network changing the following parameter in the script:

```class TransmissionTime: min,max = 1,2```

After the simulation is run, the outcome is diplsayed as list of lines, each of similare to the following:

```Node 13: 293
   12 > 8
   20  20  20  17  20  20  20  20  17  17  20  20  20  20  20  20  20  20  20  20```

In the first line, on the right of the node number, the total balance of all the wallets according to the node is shown (in this case, 293). In the following line the first number represents the initial balance of the node's wallet while the number on the left represents the net amount of tokens exchanges (i.e. inflows - outflows). In the last line the node's balance according each other node in the network is show. In the case presented here, not all the nodes agree with each other (in the simulation *min*=1 and *max*=5).

Finally, you can define a numnber of malicious nodes changing the following paramenter:

```evilPeersNum = 1```


