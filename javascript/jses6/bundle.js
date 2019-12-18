"use strict";

function imprime() {
  setTimeout(function () {
    console.log("printou");
  }, 2000);
}

function nada() {
  return regeneratorRuntime.async(function nada$(_context) {
    while (1) {
      switch (_context.prev = _context.next) {
        case 0:
          _context.next = 2;
          return regeneratorRuntime.awrap(imprime());

        case 2:
          _context.next = 4;
          return regeneratorRuntime.awrap(imprime());

        case 4:
        case "end":
          return _context.stop();
      }
    }
  });
} //nada();


imprime();
