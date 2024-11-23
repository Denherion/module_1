def send_email(message, recipient, *, sender="univercity.halp@gmail.com"):
    while True:
        if sender == recipient:
            print('Нельзя отправить письмо самому себе!')
            break
        if sender == 'univercity.halp@gmail.com':
            print('Письмо успешно отправлено с адреса ', sender, ' на адрес ', recipient)
            break
        if (((recipient[-4:-1] + recipient[-1] == '.com' and '@' in recipient)
            or (recipient[-3:-1] + recipient[-1] == '.ru' and '@' in recipient)
            or (recipient[-4:-1] + recipient[-1] == '.net' and '@' in recipient))
            and ((sender[-4:-1] + sender[-1] == '.com' and '@' in sender)
            or (sender[-3:-1] + sender[-1] == '.ru' and '@' in sender)
            or (sender[-4:-1] + sender[-1] == '.net' and '@' in sender))):
            print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ', sender, ' на адрес ', recipient)
            break
        else:
            print('Невозможно отправить письмо с адреса ', sender, ' на адрес ', recipient)
            break

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')