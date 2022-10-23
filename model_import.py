import pandas as pd
import excep


def save_to_csv():
    file_name_1 = excep.check_not_file("Enter name of the file without extension for saving students' data: ")
    read_file_st = pd.read_excel("hogwarts.xlsx", sheet_name='Students')
    read_file_st.to_csv(f"{file_name_1}.csv", index = None, header=['ID', 'Surname', 'Name', 'Birthday', 'Dormitory', 'Course'], mode='w')

    # file_name_2 = excep.check_not_file("Enter name of the file without extension for saving teachers' data: ")  
    # read_file_t = pd.read_excel("hogwarts.xlsx", sheet_name='Teachers')
    # read_file_t.to_csv(f"{file_name_2}.csv", index = None, header=['ID', 'Surname', 'Name', 'Subjects'], mode='w')

    return 'Data are saved into .csv\n'
