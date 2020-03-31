# -*- coding: utf-8 -*-
from model.contact import Contact
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="first name", middlename="middle name", lastname="lasr name",
                                    nickname="nickname", path_to_photo="C:\\Users\\Asus\\Desktop\\test_image.jfif",
                                    title="title", company="company",
                                    address="address", home="home telephone", mobile="mobile telephone",
                                    work="work telephone", fax="fax telephone", email="e-mail", email2="e-mail2",
                                    email3="e-mail3", homepage="homepage", bday="5", bmonth="February",
                                    byear="1990", aday="14", amonth="June", ayear="2000", new_group="[none]",
                                    address2="secondary address", phone2="secondary home", notes="secondary notes"))
    app.logout()


def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="", middlename="", lastname="", nickname="", path_to_photo="",
                                    title="", company="", address="", home="", mobile="", work="", fax="", email="",
                                    email2="", email3="", homepage="", bday="", bmonth="-", byear="", aday="",
                                    amonth="-", ayear="", new_group="", address2="", phone2="", notes=""))
    app.logout()
