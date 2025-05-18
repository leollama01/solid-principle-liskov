# Princípio da Substituição de Liskov (L - SOLID)

Este repositório tem como objetivo explicar o **Princípio da Substituição de Liskov (Liskov Substitution Principle - LSP)**, que é a letra **L** do acrônimo **SOLID**, um conjunto de princípios de design orientado a objetos.

## 📚 O que é o LSP?

O Princípio da Substituição de Liskov afirma que:

> "Objetos de uma classe derivada devem ser substituíveis por objetos da classe base, sem alterar o comportamento desejado do programa."
> "Se algo se comporta como outro, então pode ser usado no lugar do outro sem dar erro."

Ou seja, se uma classe `Filha` herda de uma classe `Pai`, você deve conseguir usar a `Filha` no lugar da `Pai` sem problemas.

## ✅ Por que isso é importante?

- Garante código mais **flexível**, **reutilizável** e **manutenível**.
- Evita **quebras inesperadas** quando usamos herança de forma incorreta.
