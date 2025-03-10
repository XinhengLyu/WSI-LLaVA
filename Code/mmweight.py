import torch
# 加载权重文件
res = torch.load("/home/liangyuci/PM_LLaVA/llava-v1.5-7b-lora1024-open+chose-all/non_lora_trainables.bin", map_location=torch.device("cpu"))

# 如果 res 是一个字典，直接使用它
if isinstance(res, dict):
    state_dict = res
else:
    state_dict = res.state_dict()  # 适用于模型对象

# 打印前3层的权重
count = 0
for param_tensor in state_dict:
    if count < 6:  # 只打印前3层
        print(f"参数名称: {param_tensor} \t 权重大小: {state_dict[param_tensor].size()}")
        print(state_dict[param_tensor])  # 打印具体的权重
        count += 1
    else:
        break  # 超过3层后停止循环

