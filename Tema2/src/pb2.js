const [numeFisier, culoarePuncte] = Polyglot.eval(
  "python",
  "(input('Nume fisier (.png): '), input('Culoare puncte: '))"
);

Polyglot.eval(
  "R",
  `main <- function(output, color) {
    library("lattice")
    data <- read.csv('Tema2/dataset.txt')
    png(output)
    print(xyplot(x ~ y, data, type = c("p", "r"), col = color))
    dev.off()
  }`
)(numeFisier, culoarePuncte);
