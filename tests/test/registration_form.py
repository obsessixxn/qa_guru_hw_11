from selene import have


class RegistrationFormPage:

    def __init__(self, in_browser):
        self.browser = in_browser

    def open(self, value):
        self.browser.open(value)

    def fill_name(self, name):
        self.browser.element("#firstName").type(name)

    def fill_surname(self, name):
        self.browser.element("#lastName").type(name)

    def fill_email(self, email):
        self.browser.element("#userEmail").type(email)

    def choose_gender(self, value):
        self.browser.element(f'[for="gender-radio-{value}"]').click()

    def fill_number(self, value):
        self.browser.element("#userNumber").type(value)

    def fill_date_of_birth(self, year, month, day):
        self.browser.element('#dateOfBirthInput').click()
        self.browser.element('.react-datepicker__month-select').type(month)
        self.browser.element('.react-datepicker__year-select').type(year)
        self.browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()

    def choose_subject(self, value):
        self.browser.element("#subjectsInput").type(value).press_enter()

    def choose_hobby(self):
        self.browser.element('label[for="hobbies-checkbox-1"]').click()

    def choose_photo(self, value):
        self.browser.element("#uploadPicture").set_value(os.path.abspath(f'./img/{value}'))

    def fill_address(self, value):
        self.browser.element('#currentAddress').type(value)

    def choose_state(self, value):
        self.browser.element('#state').click()
        self.browser.all('div[class*="option"]').element_by(have.text(value)).click()

    def choose_city(self, value):
        self.browser.element('#city').click()
        self.browser.all('div[class*="option"]').element_by(have.text(value)).click()

    def submit_form(self):
        self.browser.element('#submit').click()

    def should_registered_student_with(self, full_name, email, gender, number, date_of_birth,
                                       subject, hobby, photo, address, state, city):
        self.browser.element('.table').all('td').even.should(have.texts([
            full_name,
            email,
            gender,
            number,
            date_of_birth,
            subject,
            hobby,
            photo,
            address,
            state + ' ' + city
        ]
        ))
