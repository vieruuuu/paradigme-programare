package Lab2.src;

//import libraria principala polyglot din graalvm
import org.graalvm.polyglot.*;

import java.util.*;

//clasa principala - aplicatie JAVA
class Polyglot {
  // metoda privata pentru conversie low-case -> up-case folosind functia
  // toupper() din R
  private static String RToUpper(String token) {
    // construim un context care ne permite sa folosim elemente din R
    Context polyglot = Context.newBuilder().allowAllAccess(true).build();
    // folosim o variabila generica care va captura rezultatul excutiei funcitiei R,
    // toupper(String)
    // pentru aexecuta instructiunea I din limbajul X, folosim functia graalvm
    // polyglot.eval("X", "I");
    Value result = polyglot.eval("R", "toupper(\"" + token + "\");");
    // utilizam metoda asString() din variabila incarcata cu output-ul executiei
    // pentru a mapa valoarea generica la un String
    String resultString = result.asString();
    // inchidem contextul Polyglot
    polyglot.close();

    return resultString;
  }

  // metoda privata pentru evaluarea unei sume de control simple a literelor unui
  // text ASCII, folosind PYTHON
  private static int SumCRC(String token) {
    // construim un context care ne permite sa folosim elemente din PYTHON
    Context polyglot = Context.newBuilder().allowAllAccess(true).build();
    // folosim o variabila generica care va captura rezultatul excutiei functiei
    // PYTHON, sum()
    // avem voie sa inlocuim anumite elemente din scriptul pe care il construim spre
    // evaluare, aici token provine din JAVA, dar va fi interpretat de PYTHON
    Value result = polyglot.eval("python", "sum(ord(ch) for ch in '" + token + "')");
    // utilizam metoda asInt() din variabila incarcata cu output-ul executiei,
    // pentru a mapa valoarea generica la un Int
    int resultInt = result.asInt();
    // inchidem contextul Polyglot
    polyglot.close();

    return resultInt;
  }

  private static long Sum5Grade(String token) {
    // construim un context care ne permite sa folosim elemente din PYTHON
    Context polyglot = Context.newBuilder().allowAllAccess(true).build();
    // folosim o variabila generica care va captura rezultatul excutiei functiei
    // PYTHON, sum()
    // avem voie sa inlocuim anumite elemente din scriptul pe care il construim spre
    // evaluare, aici token provine din JAVA, dar va fi interpretat de PYTHON
    Value result = polyglot.eval("python", String.format("""
        sum = 0
        text = "%s"
        for ch in text:
          sum += ord(ch)

        sum**5 - 3 * sum ** 4 + sum - 4
        """, token));
    // utilizam metoda asInt() din variabila incarcata cu output-ul executiei,
    // pentru a mapa valoarea generica la un Int
    long resultInt = result.asLong();
    // inchidem contextul Polyglot
    polyglot.close();

    return resultInt;
  }

  // functia MAIN
  public static void main(String[] args) {
    // construim un context pentru evaluare elemente JS
    Context polyglot = Context.create();

    HashMap<Long, ArrayList<String>> words = new HashMap<>();
    // construim un array de string-uri, folosind cuvinte din pagina web:
    // https://chrisseaton.com/truffleruby/tenthings/
    Value array = polyglot.eval("js", "[\"If\",\"we\",\"run\",\"the\",\"java\"];");
    // pentru fiecare cuvant, convertim la upcase folosind R si calculam suma de
    // control folosind PYTHON
    for (int i = 0; i < array.getArraySize(); i++) {
      String element = array.getArrayElement(i).asString();
      String upper = RToUpper(element);
      long crc = Sum5Grade(upper.substring(1, upper.length() - 1));
      System.out.println(upper + " -> " + crc);

      ArrayList<String> lista = words.containsKey(crc) ? words.get(crc) : new ArrayList<>();

      lista.add(upper);
      words.put(crc, lista);
    }

    // inchidem contextul Polyglot
    polyglot.close();

    System.out.println("----------afisare cuvinte cu aceeasi suma de control: ------------");
    words.forEach((sumaControl, wordsList) -> {
      System.out.printf("%d: [ ", sumaControl);

      wordsList.forEach((word) -> {
        System.out.printf("%s ", word);
      });

      System.out.println("]");
    });
  }
}
