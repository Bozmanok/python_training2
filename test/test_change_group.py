from model.group import Group


def test_change_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.change_first_group(Group(name="test1 edit", header="test2 edit", footer="test3 edit"))
    app.session.logout()
