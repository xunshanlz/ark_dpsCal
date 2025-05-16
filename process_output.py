import re

def process_output(value_list):
    processed_list = []
    for value in value_list:
        # 如果是数值类型，默认四舍五入到整数
        if isinstance(value, (int, float)):
            processed_list.append(round(value))
        
        # 如果是字符串，找到所有数字并四舍五入到整数
        elif isinstance(value, str):
            numbers = re.findall(r"[-+]?\d*\.\d+|\d+", value)
            for num in numbers:
                rounded_num = round(float(num),1) 
                value = value.replace(num, str(rounded_num), 1)
            processed_list.append(value)
        
        # 如果是字典，特殊处理
        elif isinstance(value, dict):
            processed_dict = {}
            for key, val in value.items():
                if isinstance(val, (int, float)):
                    # 检测key中是否包含"间隔"或"覆盖率"
                    if '间隔' in key or '覆盖率' or '周期回费效率(费用/s)' in key:  # 特殊键，保留2位小数
                        processed_dict[key] = round(val, 2)
                    else:  # 其他键，四舍五入到整数
                        processed_dict[key] = round(val)
                else:
                    processed_dict[key] = val
            processed_list.append(processed_dict)
        
        # 其他类型直接保留
        else:
            processed_list.append(value)
    
    return processed_list