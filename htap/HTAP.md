### HTAP （Hybrid Transactional / Analytical Processing）

#### background

- OLTP(Online Transactional Processing) 联机事务处理, 主要是对数据的增删改

- OLAP(Online Analytical Processing) 联机分析处理, 主要是对数据的查询

> 因为OLTP所产生的业务数据分散在不同的业务系统中，而OLAP往往需要将不同的业务数据集中到一起进行统一综合的分析，这时候就需要根据业务分析需求做对应的数据清洗后存储在数据仓库中，然后由数据仓库来统一提供OLAP分析。所以我们常说OLTP是数据库的应用，OLAP是数据仓库的应用。所以OLAP和OLTP之间的关系可以认为OLAP是依赖于OLTP的，因为OLAP分析的数据都是由OLTP所产生的，也可以看作OLAP是OLTP的一种延展，一个让OLTP产生的数据发现价值的过程。
>
> ![img](https://pic2.zhimg.com/80/v2-e7a716b0a66831d791e4aa976a1ff891_1440w.jpg?source=1940ef5c)

#### implementation

- PingCAP 的 TiDB
- 阿里云的 HybridDB for MySQL
- 百度的 BaikalDB

#### type

- 单一系统承载 OLTP 和 OLAP（Single System for OLTP and OLAP）
- 分离的 TP 与 AP 系统（Separate OLTP and OLAP System）



### F1 Lightning

> 分离系统的好处是可以单独针对 TP 和 AP 进行设计，互相之间侵入较小，但在既有的架构下，往往需要通过离线 ETL 来转运数据（原因分析可以参考我们这篇对存储部分的分析）。而 F1 Lightning 设计也落在分离系统的范畴，使用了 CDC 进行实时数据勾兑而非离线 ETL，那毫无疑问，F1 的列存部分设计也需要和我们一样针对列存变更进行设计。
>
> 顺口提一下，论文中分析相关工作时也提到了 TiDB 和 TiFlash，不过这部分描述却是错误的，TiDB 和 Lightning 一样可以提供 Strong Snapshot Consistency，甚至由于它的独特设计，还能提供更强的一致性和新鲜度。

#### 优点

> Lightning 相对于既有 HTAP 系统，**提供了如下几个（TiDB HTAP 也一样拥有的甚至更好）优势**：
>
> 1. 拥有只读的列存副本，提供了更好的执行效率以
> 2. 相对于 ETL 流程，提供了更简单的配置和去重
> 3. 无需修改 SQL 直接查询 HTAP
> 4. 一致性和新鲜度
> 5. 安全方面 TP 与 AP 两部分统一
> 6. 设计关注点分离，TP 和 AP 可以分别针对性优化自己的领域而不过多牵扯
> 7. 扩展性，提供了对接除了 F1 DB 和 Spanner 以外不同的 TP 数据库的可能性

#### 系统架构

> 由于项目立项的前提是对 TP 系统无侵入性，因此作为 HTAP 来说，F1 Lightning 的架构设计相对保守。现有 HTAP 的研究领域，大多数项目都是以所谓 Greenfield 方案（不受前序方案约束）为假设，但 F1 Lightning 需要在对现有业务不做任何迁移且设计方案最大程度不对 TP 系统做修改（组织架构层面，F1 Lightning 团队也不管 TP 系统的代码），所以他们做出了一个 「A loosely coupled HTAP solution」，这是一个犹如驴标蛇皮袋一般巨朴实的方案：通过 CDC 做 HTAP。所以实际上，F1 Lightning 是一个 CDC + 可变更列存的方案。
>
> ![img](http://img1.sycdn.imooc.com/5f881abf0001e2d814400490.jpg)
>
> 
>
> Google 的现有 TP 系统大多选用 MVCC 模型（Multi-Version Concurrency Control 多版本并发控制）, 对于读取语义，Lightning 也选择了 MVCC 和相应的快照隔离：由 TP 发出的 CDC 如果带着时间戳向 Lightning 进行复制，MVCC 会是一个最自然而且最方便的设计。
>
> 而由于分布式 CDC 架构的天然约束和特性，Lightning 选择提供 Safe Timestamps 来保持一致性。这是一个类似水位线的设计，因为经过一次分布式分发，因此不同存储服务器接收到数据将会带来不等同的延迟，因此无法简单保证一致性。所以类似这样水位线的设计可以以数据新鲜度为代价换取查询的快照一致性。

#### 存储





#### Reading

##### abstract

HATP系统的需求日益增长，目前已有很多解决办法，一种方法是从头开始设计相关的HTAP系统，但是“我们”面临的挑战是：已存在大量的OLTP系统，联合查询引擎并不嵌入在这些系统中，需要有一个透明的中间层为新旧应用快速查询提供整合。

##### introduction

很多文献提出了HTAP系统的架构与设计，我们考虑一种不同的方式：一种松散耦合的HTAP体系结构，可以支持各种约束下的HTAP工作负载。

原因是谷歌复杂的数据生态系统，谷歌中使用多个事务性数据存储来服务大型旧版和新工作负载的数据。

