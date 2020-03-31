from model.contact import Contact


def test_change_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.change_first_contact(Contact(firstname="test1 edit", middlename="test2 edit", lastname="test3 edit",
                                             nickname="test4 edit", path_to_photo="", title="", company="", address="",
                                             home="", mobile="", work="", fax="", email="", email2="", email3="",
                                             homepage="", bday="-", bmonth="-", byear="", aday="-", amonth="-", ayear="",
                                             new_group=None, address2="", phone2="", notes=""))
    app.session.logout()
