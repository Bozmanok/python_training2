from model.contact import Contact


def test_change_first_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test"))
    app.contact.modify_first_contact(Contact(firstname="New firstname"))


def test_change_first_contact_nickname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(nickname="Test"))
    app.contact.modify_first_contact(Contact(nickname="New nickname"))
