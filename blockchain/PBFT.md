### PBFT

#### [实用拜占庭容错算法（PBFT）](https://yangzhe.me/2019/11/25/pbft/)

- $3f + 1$

- 使用状态机记录自己的操作，各结点的状态机保持一致

- 主结点选择：$i = v \space mod \space|R|$

- 接收到主结点请求后进行两步广播：第一步确认主结点可信认可当前请求，第二步确认大多数结点都认可当前请求（大多数结点都通过了第一步，确保一致性）

- 三阶段：pre-prepare, prepare, commit

  - pre-prepare: 主结点广播 $<<PRE-PREPARE, v, n, d>_{\sigma p}, m>$
  - prepare: 从结点验证通过后广播 $<PREPARE, v, n, d, i>_{\sigma i}$
  - commit: 接收到 $2f$ 个prepare消息后广播 $<COMMIT, v, n, i>_{\sigma i}$

  ![img](https://yangzhe.me/pic/pbft/normal-case-op.png)

- 客户端向主结点发起请求，经过三阶段共识，$committed-local(m, v, n, d, i)$ 为 $true$ 的结点直接将结果返回给客户端，客户端收到$f + 1$个相同的返回结果就将其视作最终的结果。

- 检查点机制
  - 保存历史数据和状态，同时也可以丢弃检查点之前的历史数据释放存储资源
  - 稳定检查点（stable checkpoint)：广播$<CHECKPOINT, n, d, i>_{\sigma i}$消息，收集到$2f$个响应（作为证明）就创建了一个稳定检查点
  
- 区间 $[h, H]$ 避免恶意的主结点滥用序号值，$h$ 为最新检查点的序号，$H$ 设置为一个相对较大的值

- View Change 域转换：域是某个主结点的整个过程，每变换一个主结点，域编号就递增加1

  - 保持系统的活性(liveness)：主从结点模式严重依赖主结点的正确性，故设置域转换避免恶意的主结点
  - 发生异常情况就触发 View Change：
    - 从结点发送 $⟨PREPARE⟩$ 消息后，在一定时间内没有收到 $2f$ 条其它结点广播的同样的 $⟨PREPARE⟩$消息。
    - 从结点发送 $⟨COMMIT⟩$ 消息以后，在一定时间内没有收到 $2f$ 条其它结点广播的同样的  $⟨COMMIT⟩$ 消息。
    - 主结点不响应客户端的请求。

  - 流程：

    1. 结点 $i$ 广播 $<VIEW-CHANGE, v+1, n, C, P, i>_{\sigma i}$ 
       - $n$  是最新稳定检查点额请求序号，$C$ 是其证明 $2f+1$ 个 $<CHECKPOINT>$ 

    2. 域编号为 $v + 1$ 的主结点 $p$ 收到 $2f$ 个 $<VIEW-CHANGE>$ 消息，广播 $<NEW-VIEW, v+1, V,O>_{\sigma p}$ 
       - $V$ 是 $2f + 1$ 个 $<VIEW-CHANGE>$ 
       - $O$ ：新的主结点重新构造相关的  $<PRE-PREPARE>$ 消息
    3. 新的主结点发送 $<VIEW-CHANGE>$ 后进入 $v + 1$ 域，其他结点检查消息后进入 $v + 1$ 域

  - 主结点不响应：客户端广播给从节点，从节点转发给主结点等待其响应，若不响应则提议进行域转换

