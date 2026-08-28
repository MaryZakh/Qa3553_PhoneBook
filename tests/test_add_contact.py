import random
import time

import pytest
from faker import Faker

from models.contact import Contact
from pages.add_new_contact_page import ContactPage

fake = Faker()


def test_add_contact_success_all_fields(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    random_suffix = random.randint(1, 10000000)

    contact = Contact(
        name=fake.first_name(),
        last_name=fake.last_name(),
        # phone = f"05012{random_suffix}",
        phone=fake.numerify("050#########"),
        email=fake.unique.email(),
        address=fake.street_address(),
        description=fake.sentence(nb_words=5)

    )

    print(random_suffix)

    contact_page.open_contact_form()
    contact_page.fill_contact_form(contact)
    contact_page.submit_contact()

    assert contact_page.contact_card_visible(contact.phone)


def test_add_contact_success_req_fields(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    random_suffix = random.randint(1, 10000000)

    contact = Contact(
        name=fake.first_name(),
        last_name=fake.last_name(),
        # phone = f"05012{random_suffix}",
        phone=fake.numerify("050#########"),
        email=fake.unique.email(),
        address=fake.city(),
        description=""

    )

    print(random_suffix)

    contact_page.open_contact_form()
    contact_page.fill_contact_form(contact)
    contact_page.submit_contact()

    assert contact_page.contact_card_visible(contact.phone)

PHONE_ALERT_TEXT = "Phone not valid: Phone number must contain only digits! And length min 10, max 15!"
EMAIL_ALERT_TEXT = "Email not valid: must be a well-formed email address"


def test_add_contact_empty_name(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)

    contact = Contact(
        name="",
        last_name=fake.last_name(),
        phone=fake.numerify("050#########"),
        email=fake.unique.email(),
        address=fake.city(),
        description=fake.sentence(nb_words=5)

    )

    contact_page.open_contact_form()
    contact_page.fill_contact_form(contact)
    contact_page.submit_contact()

    assert contact_page.is_add_button_active()

    contact_page.open_contact_list()
    assert contact_page.contact_cards_count(contact.phone) == 0


def test_add_contact_empty_last_name(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)

    contact = Contact(
        name=fake.first_name(),
        last_name="",
        phone=fake.numerify("050#########"),
        email=fake.unique.email(),
        address=fake.city(),
        description=fake.sentence(nb_words=5)

    )

    contact_page.open_contact_form()
    contact_page.fill_contact_form(contact)
    contact_page.submit_contact()

    assert contact_page.is_add_button_active()

    contact_page.open_contact_list()
    assert contact_page.contact_cards_count(contact.phone) == 0



#@pytest.mark.skip(reason = "BUG-123: Contact with empty mail")
@pytest.mark.xfail (reason = "BUG-123: Contact with empty mail")
def test_add_contact_empty_email(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)

    contact = Contact(
        name=fake.first_name(),
        last_name=fake.last_name(),
        phone=fake.numerify("050#########"),
        email="",
        address=fake.city(),
        description=fake.sentence(nb_words=5)

    )

    contact_page.open_contact_form()
    contact_page.fill_contact_form(contact)
    contact_page.submit_contact()

    assert contact_page.is_add_button_active()

    contact_page.open_contact_list()
    assert contact_page.contact_cards_count(contact.phone) == 0


def test_add_contact_empty_address(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)

    contact = Contact(
        name=fake.first_name(),
        last_name=fake.last_name(),
        phone=fake.numerify("050#########"),
        email=fake.unique.email(),
        address="",
        description=fake.sentence(nb_words=5)

    )

    contact_page.open_contact_form()
    contact_page.fill_contact_form(contact)
    contact_page.submit_contact()

    assert contact_page.is_add_button_active()

    contact_page.open_contact_list()
    assert contact_page.contact_cards_count(contact.phone) == 0


def test_add_contact_invalid_phone(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)

    contact = Contact(
        name=fake.first_name(),
        last_name=fake.last_name(),
        phone="kdfkdjfkdjfkdfjkd",
        email=fake.unique.email(),
        address=fake.address(),
        description=fake.sentence(nb_words=5)

    )

    contact_page.open_contact_form()
    contact_page.fill_contact_form(contact)
    contact_page.submit_contact()


    assert contact_page.get_alert_text().strip() == PHONE_ALERT_TEXT
    contact_page.accept_alert()

    assert contact_page.is_add_button_active()

    contact_page.open_contact_list()
    assert contact_page.contact_cards_count(contact.phone) == 0


def test_add_contact_invalid_email(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)

    contact = Contact(
        name=fake.first_name(),
        last_name=fake.last_name(),
        phone=fake.numerify("050#########"),
        email="invalid_email_format",
        address=fake.city(),
        description=fake.sentence(nb_words=5)

    )

    contact_page.open_contact_form()
    contact_page.fill_contact_form(contact)
    contact_page.submit_contact()

    assert contact_page.get_alert_text().strip() == EMAIL_ALERT_TEXT
    contact_page.accept_alert()

    assert contact_page.is_add_button_active()

    contact_page.open_contact_list()
    assert contact_page.contact_cards_count(contact.phone) == 0


@pytest.mark.xfail (reason = "BUG-124: Duplicate phone")
def test_add_contact_duplicate_phone_rejected(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)

    shared_phone = fake.unique.numerify("050##########")

    first_contact = Contact(
        name=fake.first_name(),
        last_name=fake.last_name(),
        phone=shared_phone,
        email=fake.unique.email(),
        address=fake.city(),
        description=fake.sentence(nb_words=5)

    )
    print(shared_phone)
    second_contact = Contact(
        name=fake.first_name(),
        last_name=fake.last_name(),
        phone=shared_phone,
        email=fake.unique.email(),
        address=fake.city(),
        description=fake.sentence(nb_words=5)
    )
    print(shared_phone)
    contact_page.open_contact_form()
    contact_page.fill_contact_form(first_contact)
    contact_page.submit_contact()
    assert contact_page.contact_card_visible(shared_phone)

    contact_page.open_contact_form()
    contact_page.fill_contact_form(second_contact)
    contact_page.submit_contact()



    contact_page.open_contact_list()
    assert contact_page.contact_cards_count(shared_phone) == 1
