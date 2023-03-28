class ContactList(list):
    def search(self, name):
        matching_contacts = []

        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)

        return matching_contacts


class Contact:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return "Contact(" + self.name + ", " + self.email + ")"


class Agenda:
    all_contacts = ContactList()

    def add_contact(self, contact):
        self.all_contacts.append(contact)

    def remove_contact(self, contact_email):
        for c in self.all_contacts:
            if c.email == contact_email:
                self.all_contacts.remove(c)

                return

    def print_agenda(self):
        for contact in self.all_contacts:
            print(contact)


class Friend(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone

    def __repr__(self):
        return "Friend(" + self.name + ", " + self.email + ", " + self.phone + ")"


# acest bloc se executa doar cand se apeleaza acest script
# se recomanda folosirea acestui bloc pentru a nu se executa la import
if __name__ == "__main__":
    agenda = Agenda()

    agenda.add_contact(Contact("Ion Popescu", "ion_popescu@gmail.com"))
    agenda.add_contact(Friend("Gelu Marin", "gelu@gmail.com", "07365555"))

    print("afisare lista initiala: ")
    agenda.print_agenda()

    agenda.remove_contact("ion_popescu@gmail.com")
    print("afisare lista actualizata: ")
    agenda.print_agenda()
