import PySimpleGUI as sg
from gui import progress

window = sg.Window('FC Management System')

result_headings = ['ISA', 'FC', 'Vendor', 'Date', 'Status', 'Units', 'Yakin', 'Schedule Date']
# result_table = sg.Table(headings=result_headings, values=[('','','','','')])

# result_table_values can be changed after running progress
result_table_values = [('1', '2', '3', '4', '5'), ('A', 'B', 'C', 'D', 'E'), ('가', '나', '다', '라', '마')]
result_table = sg.Table(
    key='_result_table',
    headings=result_headings,
    values=result_table_values,
    auto_size_columns=False,
    # 더블 클릭 이벤트
    bind_return_key=True)

# selected_table_values can be changed after running progress
selected_table_values = []
selected_table = sg.Table(
    key='_selected_table',
    headings=result_headings,
    values=selected_table_values,
    # 더블 클릭 이벤트
    bind_return_key=True,
    auto_size_columns=False,
    size=(20, 5))

layout = [
    [sg.Text('Please Enter FC Search Conditions')],
    [sg.Text('Base File', size=(20, 1)), sg.Input(key='_file_path_', do_not_clear=True), sg.FileBrowse()],
    [sg.Text('FC', size=(20, 1)), sg.InputText('Default FC', key='_fc_', do_not_clear=True)],
    [sg.Text('DATE_START', size=(20, 1)), sg.InputText('Default DATE_START', key='_date_start_', do_not_clear=True)],
    [sg.Text('DATE_END', size=(20, 1)), sg.InputText('Default DATE_END', key='_date_end_', do_not_clear=True)],
    [sg.Text('APPOINTMENT_STATUS1', size=(20, 1)),
     sg.InputText('Default APPOINTMENT_STATUS1', key='_appointment_status1_', do_not_clear=True)],
    [sg.Text('APPOINTMENT_STATUS2', size=(20, 1)),
     sg.InputText('Default APPOINTMENT_STATUS2', key='_appointment_status2_', do_not_clear=True)],
    [sg.Text('RESULT (Double Click -> move data to SELECTED table)', size=(50, 1))],
    [result_table],
    [sg.Text('SELECTED (Double Click -> move data to RESULT table)', size=(50, 1))],
    [selected_table],
    [sg.Button('Run', key='_run', button_color=('white', 'green')), sg.Button('Confirm', key='_confirm', button_color=('white', 'skyblue')),]
]

# Event Handling
while True:
    event, values = window.Layout(layout).Read()

    # debugging
    print(event, values)

    if event is None or event == 'Exit':
        break

    # 결과 데이터 더블 클릭 이벤트
    if event == '_result_table':
        if len(values['_result_table']) == 0:
            # 빈 곳 클릭한 것이므로 무시
            continue
        index = values['_result_table'][0]

        # add data to selected_table
        selected_table_values.append(result_table.Values[index])
        selected_table.Update(selected_table_values)

        # remove data from result_table
        del result_table_values[index]
        result_table.Update(result_table_values)

        continue

    # 선택 데이터 더블 클릭 이벤트
    if event == '_selected_table':
        if len(values['_selected_table']) == 0:
            # 빈 곳 클릭한 것이므로 무시
            continue

        index = values['_selected_table'][0]

        # add data to result_table
        result_table_values.append(selected_table.Values[index])
        result_table.Update(result_table_values)

        # remove data from selected_table
        del selected_table_values[index]
        selected_table.Update(selected_table_values)

        continue

    if event == '_confirm':
        popup = sg.PopupOKCancel('(FC) will push (I#of check) of level(#) today', )

        if popup == 'OK':
            # export csv file at certain path
            pass
        elif popup == 'Cancel':
            continue

    # <===== RUN Program =====>
    file_path = values['_file_path_']
    fc = values['_fc_']
    date_start = values['_date_start_']
    date_end = values['_date_end_']
    appointment_status1 = values['_appointment_status1_']
    appointment_status2 = values['_appointment_status2_']

    # Run Search Function

    # TODO Result
    result1 = '1'

    # <===== RESULT =====>
    # 1. Table
    result_table.Update(values=(result1,))

    # 2. Popup
    # sg.Popup(event, values, values['_fc_'], values['_fc_'], values['_fc_'])

    # print(event, values)

