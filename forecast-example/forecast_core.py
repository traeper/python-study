def recommend_units(postpone_unit_count: int):
    """
    :param postpone_unit_count: 연기 희망 갯수
    :return: 할당된 모든 unit
    """
    is_fool = False
    total_assigned_units = []

    # TODO 5 ~ 9의 recommendation flow를 구현.
    for step in range(5,10):
        print(step)

        # 할당을 꽉 채웠으면 step 중단
        if is_fool is True:
            break

        # TODO 특정 단계의 units 데이터를 엑셀로부터 모두 가져온다.(list type)
        units_data_from_excel = get_units_data_from_excel(step)

        # 각 step에 해당하는 벤더들의 unit들에 대해 반복
        for units_of_step in units_data_from_excel:
            total_assigned_units.append(units_of_step)

            # 할당 유닛 갯수
            total_assigned_count = len(total_assigned_units)

            # 할당 유닛 갯수가 연기 희망 갯수보다 많거나 같으면 중단
            if total_assigned_count >= postpone_unit_count:
                is_fool = True
                break

    return total_assigned_units


def get_units_data_from_excel(step: int):

    # TODO unit에 들어가야할 데이터 정리를 해야한다. unit의 priority, vendor, 수량 등 정보가 필요함.
    units_data_from_excel = []

    # TODO step별로 Excel에서 데이터를 어떻게 가져올지 작성.
    if step == 5:
        # step 5
        pass
    elif step == 6:
        # step 6
        pass
    elif step == 7:
        # step 7
        pass
    elif step == 8:
        # step 8
        pass
    elif step == 9:
        # step 9
        pass

    # TODO Excel로부터 데이터를 가져오세요.
    return units_data_from_excel
