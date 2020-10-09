CITA 将区块链节点的必要功能解耦为六个微服务：RPC，Auth，Consensus，Chain，Executor，Network。各组件之间通过消息总线交换信息相互协作。

 CITA 默认 3s 出一个块。

各模块功能：

- Executor 仅负责计算和执行交易

- Chain 负责存储交易