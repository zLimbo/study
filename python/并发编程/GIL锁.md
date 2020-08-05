#### GIL锁

> Python支持真正的多线程，但解释器执行时代码时，每一个线程必须先获得(GIL, Global Interpreter Lock)锁，然后每执行100条字节码，解释器就自动释放GIL锁，切换到别的进程，故多线程在Python中只能交替执行，即使在多核系统上也只能用到一个核，GIL是Python解释器（CPython）设计的历史遗留问题，除非重写一个不带GIL的解释器。