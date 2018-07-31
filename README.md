# Blockchain Network Simulator

This short Python3 script simulates a network of nodes that broadcast transactions. A transaction moves tokens from a node's wallet to a recipient's wallet. The time a transaction takes to get to any other node on the network is uniformly sampled from a range of time intervals, from *min* to *max*.

Nodes can act honestly or maliciously. An honest node will never issue a transaction whose value is greater than the current balance of the wallet and will issue at most one transaction per time interval. Conversely, a malicious node will issue as many transactions as it can in order to try to subvert the consensus of the network.

Without a proper consensus protocol run by the nodes the simulation shows that:

1. even with no malicious nodes, whenever *max* > *min* the likelihood of differences between each node's ledger (and, ultimately, in the wallet's balances) increases.
2. malicious nodes can spend more than they actually posses if *max* > *min* exploiting the variance in the time a transactions take to reach a node.

You can adjust the propagation latency over the network changing the following parameters in the script:

```python
class TransmissionTime: min,max = 1,2
```

After the simulation is run, the outcome is diplayed as a list of lines, one per node, each similar to the following:

```python
Node 13: 293
   12 > 8
   20  20  20  17  20  20  20  20  17  17  20  20  20  20  20  20  20  20  20  20
```

In the first line, next to the node number, the total balance of all the wallets according to the node is shown (in this case, 293). In the following line the first number represents the initial balance of the node's wallet while the number on the right represents the net amount of tokens exchanges (i.e. *inflows* - *outflows*). In the last line the node's balance according each other node in the network is shown. In the case presented here, not all the nodes agree on the balance of node 13 (in the simulation *min*=1 and *max*=5).

Finally, you can define a number of malicious nodes changing the following paramenter:

```python
evilPeersNum = 1
```

The malicious nodes are the the last ones.
