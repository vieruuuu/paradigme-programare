const [aruncariMonedaStr, numarulXStr] = Polyglot.eval(
  "python",
  "(input('Numarul aruncarii monedei: '), input('Numarul x (1 <= x <= nr_aruncari): '))"
);

const aruncariMoneda = parseInt(aruncariMonedaStr);
const numarulX = parseInt(numarulXStr);

if (aruncariMoneda < 0 || numarulX < 1 || numarulX > aruncariMoneda) {
  throw "da niste numere bune nu fi neserios";
}

const prob = Polyglot.eval(
  "R",
  `prob <- function(x, n) {
    return(dbinom(x, n, 0.5))
  }`
)(numarulX, aruncariMoneda);

console.log(
  `prob de a obtine cap de ${numarulX} din ${aruncariMoneda} aruncari este ${prob}`
);
