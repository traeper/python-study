import PySimpleGUI as sg

window = sg.Window('FC Management System')

result_list = sg.Listbox(values=[], size=(60, 6))

layout = [
        [sg.Text('Please Enter FC Search Conditions')],
        [sg.Text('Base File', size=(20, 1)), sg.Input(key='_file_path_', do_not_clear=True), sg.FileBrowse()],
        [sg.Text('FC', size=(20, 1)), sg.InputText('Default FC', key='_fc_', do_not_clear=True)],
        [sg.Text('DATE_START', size=(20, 1)), sg.InputText('Default DATE_START', key='_date_start_', do_not_clear=True)],
        [sg.Text('DATE_END', size=(20, 1)), sg.InputText('Default DATE_END', key='_date_end_', do_not_clear=True)],
        [sg.Text('APPOINTMENT_STATUS1', size=(20, 1)), sg.InputText('Default APPOINTMENT_STATUS1', key='_appointment_status1_', do_not_clear=True )],
        [sg.Text('APPOINTMENT_STATUS2', size=(20, 1)), sg.InputText('Default APPOINTMENT_STATUS2', key='_appointment_status2_', do_not_clear=True)],
        [sg.Text('RESULT', size=(20, 1))],
        [result_list],
        [sg.Button('Run', button_color=('white', 'green')), sg.Exit()]
    ]

while True:
    event, values = window.Layout(layout).Read()
    if event is None or event == 'Exit':
        break

    print(event, values)

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
    # 1. List
    result_list.Update(values=(result1, ))

    # 2. Popup
    # sg.Popup(event, values, values['_fc_'], values['_fc_'], values['_fc_'])

    # print(event, values)




# 1 input box
# 2 search button
# 3 output result box
# 4  check box for each output row
# 5 input box at the end of each output row
# 6 enter(confirm) button