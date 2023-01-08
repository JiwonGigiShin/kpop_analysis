# 크롬 웹브라우저 실행
path = "chromedriver.exe"

driver = webdriver.Chrome(path)
# 주소는 melon(음원사이트)
driver.get('http://www.melon.com')
time.sleep(2)  # 2초 정지

# 멜론차트 클릭
driver.find_element_by_css_selector(".menu_bg.menu01").click()
time.sleep(2)  # 2초 정지

# 일간차트 클릭
driver.find_element_by_css_selector(".menu_chart.m2").click()


# 크롤링 코드
dict = {}    # 전체 크롤링 데이터를 저장할 딕셔너리 생성

number = 100  # 수집할 글 갯수 정하기

# 반복문 시작
for i in range(0,number):
    # 곡정보 더보기 버튼 클릭
    more_info_list = driver.find_elements_by_css_selector(".btn.button_icons.type03.song_info")
    more_info_list[i].click()
    time.sleep(1)
    # 크롤링
    try :
        music_info = {}  # 개별 블로그 내용을 담을 딕셔너리 생성
        time.sleep(1)
