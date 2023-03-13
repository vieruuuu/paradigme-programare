package com.vieru.lab3

class Birth(val year: Int, val month: Int, val day: Int) {
  override fun toString(): String {
    return "($day.$month.$year)"
  }
}

class Contact(val name: String, var phone: String, val birthDate: Birth) {
  fun print() {
    println("Name: $name, Mobile: $phone, Date: $birthDate")
  }
}

fun main(args: Array<String>) {
  val agenda = mutableListOf<Contact>()
  agenda.add(Contact("Mihai", "0744321987", Birth(1900, 11, 25)))
  agenda += Contact("George", "0761332100", Birth(2002, 3, 14))
  agenda += Contact("Liviu", "0231450211", Birth(1999, 7, 30))
  agenda += Contact("Popescu", "0211342787", Birth(1955, 5, 12))

  for (persoana in agenda) {
    persoana.print()
  }

  println("Agenda dupa eliminare contact [George]:")
  agenda.removeAt(1)

  for (persoana in agenda) {
    persoana.print()
  }

  agenda.remove(Contact("Liviu", "0231450211", Birth(1999, 7, 30)))
  println("Agenda dupa eliminare contact [Liviu]:")
  agenda.removeAt(1)

  for (persoana in agenda) {
    persoana.print()
  }

  println("Cautare nume: Popescu")

  for (contact in agenda) {
    if (contact.name == "Popescu") {
      contact.print()
      break
    }
  }

  println("Cautare numar de telefon: 0744321987")

  for (contact in agenda) {
    if (contact.phone == "0744321987") {
      contact.print()
      break
    }
  }

  println("persoana care nu exista: Marius Fratele")

  var aMers = true

  for (contact in agenda) {
    if (contact.name == "Marius Fratele") {
      aMers = false
      break
    }
  }

  if (aMers) {
    println("nu a fost gasit")
  }

  println("Popescu are al nr de tel, 0479994441")

  for (contact in agenda) {
    if (contact.name == "Popescu") {
      contact.phone = "0479994441"
      contact.print()
      break
    }
  }
}
