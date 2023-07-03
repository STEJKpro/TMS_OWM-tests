import logging
import allure
from pages.main_page import MainPage
from pytest import fixture, mark
from data import ui_data
from data.url_data import LOGIN_PAGE_URL
from playwright.sync_api import expect
import os
