# 区分以下类型哪些是容器序列哪些是扁平序列，哪些是可变序列哪些是不可变序列：

# list
# tuple
# str
# dict
# collections.deque

#容器序列可以存放不同类型的数据。即可以存放任意类型对象的引用。
#容器序列：list,tuple,ollections.deque

#扁平序列只能容纳一种类型。也就是说其存放的是值而不是引用。换句话说扁平序列其实是一段连续的内存空间，由此可见扁平序列其实更加紧凑。但是它里面只能存放诸如字符、字节和数值这种基础类型。
#扁平序列：str

#可变序列：list,collections.deque
#不可变序列：tuple,str