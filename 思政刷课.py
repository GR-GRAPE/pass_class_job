from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
import time

driver = webdriver.Chrome()

driver.get('https://i.chaoxing.com')

search_box_1 = driver.find_element(By.CLASS_NAME, "ipt-tel")
# count = input("请输入你的账号：")
search_box_1.send_keys('')

search_box_2 = driver.find_element(By.CLASS_NAME, "ipt-pwd")
# passport = input('请输入你的密码：')
search_box_2.send_keys('')

button1 = driver.find_element(By.CLASS_NAME, "btns-box")
button1.click()
# 进行登录

time.sleep(1)
# 需要等待其加载，否则无法定位

list1 = driver.find_element(By.CSS_SELECTOR, '#first13753')
list1.click()
time.sleep(2)

iframe1 = driver.find_element(By.CSS_SELECTOR, '#frame_content')
driver.switch_to.frame(iframe1)
# 切换至课程所在iframe下

button2s = driver.find_elements(By.CSS_SELECTOR, '.color1')
button2 = button2s[1]
button2.click()
time.sleep(1)

# 切到第二个窗口
driver.switch_to.window(driver.window_handles[1])


for i in range(0, 200):

    # 找到该类系的所有科目
    driver.refresh()
    time.sleep(2)

    # 切换到章节
    driver.switch_to.default_content()
    zj = driver.find_element(By.CSS_SELECTOR, ".zj")
    zj.click()

    # 重新切换iframe
    iframe2 = driver.find_element(By.CSS_SELECTOR, '#frame_content-zj')
    driver.switch_to.frame(iframe2)
    elements = driver.find_elements(By.CSS_SELECTOR, '.catalog_level >* .catalog_points_yi')

    # 切换至合适的iframe
    driver.switch_to.default_content()
    iframe2 = driver.find_element(By.CSS_SELECTOR, '#frame_content-zj')
    driver.switch_to.frame(iframe2)

    # 打开具体视频播放页
    elements[i].click()

    # 切换到父类iframe
    time.sleep(3)
    driver.switch_to.default_content()
    driver.switch_to.window(driver.window_handles[1])

    try:
        iframe3 = driver.find_element(By.CSS_SELECTOR, '#iframe')
        driver.switch_to.frame(iframe3)

        # 切换到父类下的iframe
        iframe4 = driver.find_element(By.CSS_SELECTOR, '.ans-attach-online.ans-insertvideo-online')
        driver.switch_to.frame(iframe4)

        # 找到播放按钮
        time.sleep(3)
        button3 = driver.find_element(By.CSS_SELECTOR, '.vjs-icon-placeholder')

        # 使用selenium中的点击操作，因为 button.click 不起作用
        actions = ActionChains(driver)
        actions.move_to_element(button3)
        actions.click().perform()

        # 等待3s
        time.sleep(3)

        # 获取视频时长
        duration_element = driver.find_element(By.CLASS_NAME, 'vjs-duration-display')
        duration_time = duration_element.text
        time_total = datetime.strptime(duration_time, "%M:%S")
        # 计算总秒数
        total_seconds = time_total.minute * 60 + time_total.second * 1

        # 等待视频播放完毕
        time.sleep(total_seconds)

        # 关闭视频播放页，回到课程目录处
        driver.back()
        time.sleep(3)
        driver.back()

    except:
        driver.back()
        time.sleep(3)
        driver.back()
        pass

