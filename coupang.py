from selenium import webdriver
from bs4 import BeautifulSoup

# Selenium 웹 드라이버 설정
driver = webdriver.Chrome()  # 자신의 ChromeDriver 경로로 변경해주세요

# 쿠팡 로그인 페이지 URL
url = 'https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1687674261&rver=7.3.6960.0&wp=MBI_SSL&wreply=https%3a%2f%2fwww.microsoft.com%2frpsauth%2fv1%2faccount%2fSignInCallback%3fstate%3deyJSdSI6Imh0dHBzOi8vd3d3Lm1pY3Jvc29mdC5jb20va28ta3I_bGM9MTA0MiIsIkxjIjoiMTA0MiIsIkhvc3QiOiJ3d3cubWljcm9zb2Z0LmNvbSJ9&lc=1042&id=74335&aadredir=0'

# Selenium을 통해 웹 페이지 열기
driver.get(url)

# BeautifulSoup을 사용하여 HTML 파싱
soup = BeautifulSoup(driver.page_source, 'html.parser')

# 쿠팡 로고 가져오기
# logo_img = soup.find('img', class_='member-logo__img-fixer')
# logo_img_url = logo_img['src']
#print('쿠팡 로고 이미지 URL:', logo_img_url)

#헤더 정보 가져오기
#header = soup.find('head')
print(soup)

# 입력 폼 전체 가져오기
#all_input = soup.find('div', class_='win-scroll')
#print('전체 입력 폼 : ', all_input)

# 로그인 버튼 폼 가져오기
#login_button = soup.find('button', class_='login__button')
#print('로그인 버튼 폼:', login_button)

# 웹 드라이버 종료
driver.quit()
