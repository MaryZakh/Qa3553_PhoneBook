import random
import time

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

    PHONE_ALERT_TEXT = " Phone not valid: Phone number must contain only digits! And length min 10, max 15!"
    EMAIL_ALERT_TEXT = "Email not valid: must be a well-formed email address"


def test_add_contact_empty_name(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)

    contact = Contact(
        name="",
        last_name=fake.last_name(),
        phone=fake.numerify("050#########"),
        email=fake.unique.email(),
        address=fake.city(),
        description=""

    )

    contact_page.open_contact_form()
    contact_page.fill_contact_form(contact)
    contact_page.submit_contact()

    assert contact_page.is_add_button_active()