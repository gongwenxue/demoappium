# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["platformName"] = "android"
caps["deviceName"] = "aa"
caps["appPackage"] = "com.xueqiu.android"
caps["appActivity"] = "com.xueqiu.android.common.MainActivity"
#caps["autoGrantPermissions"] = "true"
caps["noReset"]="true"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(10)
el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.ImageView")
el1.click()
el2 = driver.find_element_by_id("com.xueqiu.android:id/tv_login")
el2.click()
el3 = driver.find_element_by_id("com.xueqiu.android:id/tv_login_by_phone_or_others")
el3.click()
el4 = driver.find_element_by_id("com.xueqiu.android:id/register_phone_number")
el4.send_keys("232434")

driver.quit()