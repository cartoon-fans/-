# 1,确定技术点
# *并发多线程
# *确定数据传输网络　　tcp
# ２
# 结构设计
# 面向对象封装模式
# 使用类封装主体功能(2,3,4,)
# 3功能模块的划分
# 服务端
#     主线程　不断接收请求　
# 用户模型类
#     初始化　属性　请求类型　ip 地址，端口
#     创建　用户对象
# 用户请求逻辑处理类
#     封装方法　每个用户分配　线程　
#     封装方法　解析请求协议　判断请求类型
#     封装方法　根据类型　调用方法执行请求
#
# 4 请求类型和请求协议
# 5　每个功能逻辑