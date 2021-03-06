#### 多任务

> 三种方式：
>
> - 多进程模式
> - 多线程模式
> - 多进程+多线程模式
>
> 线程是最小执行单元，进程至少由一个线程组成，如何调度进程和线程完全由操作系统决定。
>
> 多进程和多线程涉及到同步、数据共享问题。
>
> 多任务通常会设计`Master-Worker`模式，`Master`负责分配任务，`Worker`负责执行任务。

#### 进程和线程的优劣

|      | 多进程                                                       | 多线程                                   |
| ---- | ------------------------------------------------------------ | ---------------------------------------- |
| 优点 | 稳定性高，一个子进程崩溃了不会影响主进程和其他子进程（主进程崩溃其他子进程也会崩溃，但`Master`只负责分配任务，崩溃概率低） | 创建线程开销低                           |
| 缺点 | 创建进程开销代价大，同时在内存和CPU的限制下，操作系统能调度的进程数是有限的 | 稳定性低，任一线程崩溃，整个进程就会崩溃 |

#### 作业切换开销

多任务达到一定限度，就会消耗系统所有资源，导致效率急剧下降

|      | 计算密集性                | IO密集型                                              |
| ---- | ------------------------- | ----------------------------------------------------- |
| 特点 | 进行大量计算，消耗CPU资源 | 涉及到网络、磁盘IO，CPU消耗少，大部分时间在等待IO完成 |
| 方式 | 进程数等于CPU核心数       | 多进程，脚本语言（代码量少）                          |

#### 异步IO

> 现代操作系统支持异步IO，可利用单进程单线程执行多任务，称为“事件驱动模型”（Nginx是支持异步IO的Web服务器)。
>
> 异步IO在Python上成为协程。