from gmail import *
from random import choice

#select random file
file_names = ['1.html', '2.html', '3.html']
file_name = choice(file_names)


#select random reason
reasons = ['Thứ hai', 'Thứ ba', 'Thứ tư', 'Thứ năm', 'Thứ sáu']
reason = choice(reasons)

#open file
template_file = open(file_name, encoding="utf8")
html_content = template_file.read()
template_file.close()

#fill in placeholder
html_content = html_content.replace('{{reason}}', reason)

#send email
gmail = GMail('vietanh.techkids@gmail.com','1111995ab')
msg = Message('Đơn xin nghỉ học', to = 'c4e13.lab.huynq@gmail.com', html=html_content)
gmail.send(msg)
