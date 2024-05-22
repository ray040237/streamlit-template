import re

def SOP_R2C(name, blade, auto):
    Switch = re.search(r'[0-9]+T[0-9]', name)
    if Switch:
        Switch = Switch.group()
    else:
        return []
    GroundConnection = f'{Switch}开关' if blade == 1 else f'{Switch}2刀闸'
    Blade_blank = [''] * 2
    Auto_blank = [''] * 6
    Blade_demo = [
        f'拉开{Switch}2刀闸。',
        f'检查{Switch}2刀闸在拉开位置。',
    ]
    Auto_demo = [
        '汇报调度（申请进行遥控）。',
        '再经调度令。',
        f'切换{Switch}开关“远方/就地”转换开关至“就地”位置。',
        f'退出{Switch}开关保护合闸压板。',
        f'退出{Switch}开关重合闸压板。',
        f'断开{Switch}开关操作电源空气开关。',
    ]
    if blade == 2:
        Blade_blank = Blade_demo
    if auto:
        Auto_blank = Auto_demo
    SOP_R2C_demo = [
        f'核对{name}名称、编号及位置正确。',
        Auto_blank[0],
        Auto_blank[1],
        Auto_blank[2],
        f'断开{Switch}开关。',
        f'检查{Switch}开关在分闸位置。',
        Auto_blank[3],
        Auto_blank[4],
        Blade_blank[0],
        Blade_blank[1],
        f'拉开{Switch}1刀闸。',
        f'检查{Switch}1刀闸在拉开位置。',
        Auto_blank[5],
        f'验明{GroundConnection}线路侧三相确无电压。',
        f'在{GroundConnection}线路侧装设10kV____________接地线1组。',
        f'在{Switch}开关操作把手上悬挂“禁止合闸，线路有人工作”标志牌。',
    ]
    return [item for item in SOP_R2C_demo if item != '']


def SOP_C2R(name, blade, auto):
    SOP_name = name
    Switch = re.search(r'[0-9]+T[0-9]', SOP_name)
    if Switch:
        Switch = Switch.group()
    else:
        return []
    GroundConnection = f'{Switch}开关' if blade == 1 else f'{Switch}2刀闸'
    Blade_blank = [''] * 2
    Auto_blank = [''] * 7
    Blade_demo = [
        f'合上{Switch}2刀闸。',
        f'检查{Switch}2刀闸在合上位置。',
    ]
    Auto_demo = [
        f'合上{Switch}开关操作电源空气开关。',
        f'投入{Switch}开关保护合闸压板。',
        f'投入{Switch}开关重合闸压板。',
        f'切换{Switch}开关“远方/就地”转换开关至“远方”位置。',
        '汇报调度（申请遥控操作）。',
        '再经调度令。',
        f'切换{Switch}开关“远方/就地”转换开关至“就地”位置。',
        f'切换{Switch}开关“远方/就地”转换开关至“远方”位置。',
    ]

    if blade == 2:
        Blade_blank = Blade_demo
    if auto:
        Auto_blank = Auto_demo

    SOP_C2R_demo = [
        f'核对{SOP_name}名称、编号及位置正确。',
        f'取下{Switch}开关操作把手“禁止合闸，线路有人工作”标志牌。',
        f'拆除{GroundConnection}线路侧10kV____________接地线1组。',
        Auto_blank[0],
        f'检查{Switch}开关在分闸位置。',
        f'合上{Switch}1刀闸。',
        f'检查{Switch}1刀闸在合上位置。',
        Blade_blank[0],
        Blade_blank[1],
        Auto_blank[0],
        Auto_blank[1],
        Auto_blank[2],
        Auto_blank[3],
        Auto_blank[4],
        Auto_blank[5],
        f'合上{Switch}开关。',
        f'检查{Switch}开关在合闸位置。',
        Auto_blank[6],
    ]
    return list(filter(lambda item: item != '', SOP_C2R_demo))

def PF_R2C(name, blade,S_num, B_num, L_type):
    PF_name = name
    match = re.search(r"#([0-9]+)\s*杆*塔*", PF_name)
    if match:
        RodNum = match.group(1)
    else:
        RodNum = ' '
    new_steps = []
    GC_name = ''
    H_GC_name = ''

    # Add steps from R2C_Outage_steps
    for i in range(S_num, 0, -1):
        new_steps.append('断开401' + str(i) + '开关。')
        new_steps.append('检查401' + str(i) + '开关在分闸位置。')

    if L_type == '柱上刀闸':
        for i in range(B_num, 0, -1):
            new_steps.append('拉开400' + str(i) + 'G刀闸。')
            new_steps.append('检查400' + str(i) + 'G刀闸在拉开位置。')
        GC_name = '4001G刀闸'
    else:
        for i in range(B_num, 0, -1):
            new_steps.append('拉开401' + str(i) + 'G刀闸。')
            new_steps.append('检查401' + str(i) + 'G刀闸在拉开位置。')
        GC_name = '4011G刀闸'

    new_steps.append('拉开' + RodNum + 'T01RD跌落式熔断器。')
    new_steps.append('检查' + RodNum + 'T01RD跌落式熔断器在拉开位置。')

    if blade > 0:
        new_steps.append('拉开' + RodNum + 'T01刀闸。')
        new_steps.append('检查' + RodNum + 'T01刀闸在拉开位置。')
        H_GC_name = RodNum + 'T01刀闸'
    else:
        H_GC_name = RodNum + 'T01RD跌落式熔断器'

    if (L_type == '配电柜') & (B_num == 0):
        GC_name = '4011开关'

    new_steps.append('验明' + GC_name + '变压器侧相线及零线确无电压。')
    new_steps.append('在' + GC_name + '变压器侧装设0.4kV____________接地线1组。')
    new_steps.append('验明' + H_GC_name + '变压器侧三相确无电压。')
    new_steps.append('在' + H_GC_name + '变压器侧装设10kV____________接地线1组。')
    new_steps.append('在' + GC_name + '操作处上悬挂“禁止合闸，线路有人工作”标志牌。')
    new_steps.append('在' + H_GC_name + '操作处上悬挂“禁止合闸，线路有人工作”标志牌。')

    # Add steps from combined_function
    PF_R2C_demo = [
        '核对' + PF_name + '名称、编号及位置正确。',
    ]
    PF_R2C_demo.extend(new_steps)
    # print(PF_R2C_demo)
    return PF_R2C_demo

def PF_C2R(name, blade, S_num, B_num, L_type):
    PF_name = name
    match = re.search(r"#([0-9]+)\s*杆*塔*", PF_name)
    if match:
        RodNum = match.group(1)
    else:
        RodNum = ' '
    new_steps = []
    GC_name = ''
    H_GC_name = ''
    if L_type == '配电柜':
        if B_num == 0:
            GC_name = '4011开关'
        else:
            GC_name = '4011G刀闸'
    else:
        GC_name = '4001G刀闸'
    if blade > 0:
        H_GC_name = RodNum + 'T01刀闸'
    else:
        H_GC_name = RodNum + 'T01RD跌落式熔断器'
    new_steps.append('取下' + GC_name + '操作处上“禁止合闸，线路有人工作”标志牌。')
    new_steps.append('取下' + H_GC_name + '操作处上悬挂“禁止合闸，线路有人工作”标志牌。')
    new_steps.append('拉开' + RodNum + 'T01RD跌落式熔断器。')
    new_steps.append('检查' + RodNum + 'T01RD跌落式熔断器在拉开位置。')
    new_steps.append('拆除' + H_GC_name + '变压器侧10kV____________接地线1组。')
    new_steps.append('拆除' + GC_name + '变压器侧0.4kV____________接地线1组。')
    if blade > 0:
        new_steps.append('检查' + RodNum + 'T01RD跌落式熔断器在拉开位置。')
        new_steps.append('合上' + RodNum + 'T01刀闸。')
        new_steps.append('检查' + RodNum + 'T01刀闸在合上位置。')
    for i in range(S_num, 0, -1):
        new_steps.append('检查401' + str(i) + '开关在分闸位置。')
    if L_type == '柱上刀闸':
        for i in range(B_num, 0, -1):
            new_steps.append('检查400' + str(i) + 'G刀闸在拉开位置。')
    else:
        for i in range(B_num, 0, -1):
            new_steps.append('检查401' + str(i) + 'G刀闸在拉开位置。')
    new_steps.append('合上' + RodNum + 'T01RD跌落式熔断器。')
    new_steps.append('检查' + RodNum + 'T01RD跌落式熔断器在合上位置。')
    if L_type == '柱上刀闸':
        for i in range(1, B_num + 1):
            new_steps.append('合上400' + str(i) + 'G刀闸。')
            new_steps.append('检查400' + str(i) + 'G刀闸在合上位置。')
    else:
        for i in range(1, B_num + 1):
            new_steps.append('合上401' + str(i) + 'G刀闸。')
            new_steps.append('检查401' + str(i) + 'G刀闸在合上位置。')
    for i in range(1, S_num + 1):
        new_steps.append('合上401' + str(i) + '开关。')
        new_steps.append('检查401' + str(i) + '开关在合闸位置。')
    PF_C2R_demo = [
        '核对' + PF_name + '名称、编号及位置正确。',
    ]
    PF_C2R_demo.extend(new_steps)
    return PF_C2R_demo



def output(name, model, before, after, blade, auto, l_model, l_blade, l_switch):
    models = {
        '柱上开关-运行-检修': SOP_R2C(name, blade, auto),
        '柱上开关-检修-运行': SOP_C2R(name, blade, auto),
        '台区-运行-检修': PF_R2C(name,blade,l_switch, l_blade, l_model),
        '台区-检修-运行': PF_C2R(name,blade,l_switch, l_blade, l_model),
    }

    steps = models[model + '-' + before + '-' + after]
    print(model + '-' + before + '-' + after)
    return steps
