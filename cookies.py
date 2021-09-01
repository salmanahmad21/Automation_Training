import requests
from selenium import webdriver
from selenium.common import exceptions
import time
driver = webdriver.Chrome(
    executable_path="/Users/salmanahmad/Downloads/chromedriver")


head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'origin': 'https://authn.stage.edx.org',
    'referer': 'https://authn.stage.edx.org/',
    'content-type': 'application/x-www-form-urlencoded'
}


csrf_url = "https://courses.stage.edx.org/csrf/api/v1/token"
login_url = "https://courses.stage.edx.org/api/user/v2/account/login_session/"

try:
    client = requests.session()

    # Retrieving the CSRF token first
    client.get(csrf_url)  # sets cookie
    if 'csrftoken' in client.cookies:
        csrftoken = client.cookies['csrftoken']
    else:
        csrftoken = client.cookies['csrf']

    login_payload = dict(email_or_username='salmanahmad21',
                         password='Salman123456', csrfmiddlewaretoken=csrftoken)

    req = client.post(login_url, data=login_payload, headers=head)

    session_cookies = client.cookies
    cookies_dictionary = session_cookies.get_dict()

    driver.get('https://courses.stage.edx.org/')
    time.sleep(2)
    for cookie in session_cookies.items():
        key, value = cookie
        cook = {'name': key,
                'value': value,
                'domain': '.stage.edx.org',
                'path': '/',
                'httpOnly': False,
                'sameSite': 'None',
                'secure': True
                }
        print(cook)
        driver.add_cookie(cook)

    # Adds the cookie into current browser context
    driver.get('https://courses.stage.edx.org/dashboard')
except exceptions.InvalidCookieDomainException as e:
    print(e)
