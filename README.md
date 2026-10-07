Utmaning 1 – Bok i ett bibliotek
Du ska skapa en klass som representerar en bok.
Klassen ska heta:
class Book:
Din klass ska innehålla följande egenskaper:
title – bokens titel
author – bokens författare
pages – antal sidor
Alla värden ska anges när objektet skapas.
Din uppgift
Skapa klassen Book.
Skapa en __init__-metod.
Lagra title, author och pages med hjälp av self.
Skapa två olika bokobjekt.
Skriv ut information om båda böckerna.
Programmet skulle exempelvis kunna skriva ut:
Title: The Hobbit
Author: J.R.R. Tolkien
Pages: 310
Extra utmaning
Lägg till en metod som heter:
show_info()
När metoden används ska information om boken skrivas ut.
Du ska då kunna skriva:
book1.show_info()
och få information om boken utskriven.

Utmaning 2 – Temperaturmätare
Du ska skapa en klass som representerar en temperaturmätare.
Klassen ska heta:
class TemperatureSensor:
Temperaturmätaren ska innehålla:
location – var sensorn sitter
temperature – aktuell temperatur
Exempel på platser kan vara:
Kitchen
Bedroom
Garage
Outside
Din uppgift
Skapa klassen TemperatureSensor.
Skapa en __init__-metod.
Låt location och temperature anges när sensorn skapas.
Skapa minst två olika sensorer.
Skriv ut deras temperaturer.
Lägg sedan till metoden:
increase_temperature()
Varje gång metoden körs ska temperaturen öka med 1 grad.
Exempel:
sensor1.increase_temperature()
sensor1.increase_temperature()
Om temperaturen från början var 20 ska den nu vara 22.
Extra utmaning
Skapa även metoden:
decrease_temperature()
Den ska minska temperaturen med 1 grad varje gång den används.
Skapa slutligen:
show_temperature()
som exempelvis skriver:
Kitchen: 22 degrees

Utmaning 3 – Produktlager
Du arbetar med ett enkelt lagersystem och ska skapa en klass som representerar en produkt.
Klassen ska heta:
class Product:
Varje produkt ska innehålla:
name – produktens namn
price – produktens pris
stock – hur många som finns i lager
Exempel:
product1 = Product("Keyboard", 399, 10)
Det betyder att produkten:
heter Keyboard
kostar 399 kr
har 10 exemplar i lager
Din uppgift
Skapa klassen och lägg sedan till följande metod:
sell()
När sell() används ska antalet produkter i lager minska med 1.
Exempel:
product1.sell()
Om lagersaldot tidigare var:
10
ska det efter försäljningen vara:
9
Viktigt!
En produkt får inte kunna säljas om lagersaldot är 0.
Använd därför en if-sats i metoden.
Om produkten är slut ska programmet exempelvis skriva:
Product is out of stock!
Lägg även till
Skapa en metod:
show_info()
Den ska skriva ut produktens information, exempelvis:
Product: Keyboard
Price: 399 kr
Stock: 9
Extra utmaning
Skapa metoden:
restock(amount)
Den ska kunna fylla på lagret.
Exempel:
product1.restock(5)
Om lagersaldot tidigare var 9 ska det nu vara 14.

