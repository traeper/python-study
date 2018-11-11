
from . import forecast_core as core

# 4. 연기 희망 units를 입력
postpone_unit_count = int(input())
print("연기 희망 units = " + str(postpone_unit_count))

# 5 ~ 9. recommendation flow

# 할당된 모든 units, recommend_units 함수를 만들어서 추천하는 기능을 구현하세요.
total_assigned_units = core.recommend_units(postpone_unit_count)

for unit in total_assigned_units:
    print(unit)




