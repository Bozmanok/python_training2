from model.contact import Contact


def test_change_first_contact_firstname(app):
    app.contact.modify_first_contact(Contact(firstname="New firstname"))


def test_change_first_contact_nickname(app):
    app.contact.modify_first_contact(Contact(nickname="New nickname"))
