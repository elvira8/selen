import allure
from selenium.webdriver.common.by import By


@allure.title("Успешный вход с валидными кредами")
@allure.description("Проверяем, что пользователь tomsmith может войти и видит сообщение об успехе")
def test_successful_login(driver):
    # Открываем страницу логина
    driver.get("https://the-internet.herokuapp.com/login")

    # Находим поля для ввода и кнопку
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    # Вводим правильные данные
    username_field.send_keys("tomsmith")
    password_field.send_keys("SuperSecretPassword!")

    # Кликаем на кнопку входа
    login_button.click()

    # Находим элемент с сообщением об успешном входе
    success_message = driver.find_element(By.CSS_SELECTOR, ".flash.success")

    # Проверяем, что сообщение содержит текст об успешном входе
    assert "You logged into a secure area!" in success_message.text


@allure.title("Неуспешный вход с неверными кредами")
@allure.description("Проверяем, что при неверных кредах видно сообщение об ошибке")
def test_unsuccessful_login(driver):
    # Открываем страницу логина
    driver.get("https://the-internet.herokuapp.com/login")

    # Находим поля для ввода и кнопку
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    # Вводим неправильные данные
    username_field.send_keys("wrong_user")
    password_field.send_keys("wrong_password")

    # Кликаем на кнопку входа
    login_button.click()

    # Находим элемент с сообщением об ошибке
    error_message = driver.find_element(By.CSS_SELECTOR, ".flash.error")

    # Проверяем, что сообщение содержит текст об ошибке
    assert "Your username is invalid!" in error_message.text