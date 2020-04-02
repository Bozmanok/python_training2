from model.contact import Contact


def test_change_first_contact_firstname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="New firstname"))
    app.session.logout()


def test_change_first_contact_nickname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(nickname="New nickname"))
