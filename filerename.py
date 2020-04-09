import os

os.chdir('e:/Movies/bloodride')

print(os.getcwd())

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    f_title, f_num = f_name.split('.')[1:3]
    f_title = f_title.strip()
    f_num = f_num.strip()

    new_name = '{}-{}{}'.format(f_title, f_num, f_ext)

    os.rename(f, new_name)
