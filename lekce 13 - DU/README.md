Aplikace Objednávky pizzy se spouští pomocí app.py.
Provedené (zaplacené) objednávky se ukládají do souboru orders.json. Na ukázku tři objednávky jsou už vytvořené.
Ukázkový výpis po načtení z orders.json:
    Loading Orders from File...
    Loaded Orders:
    Order 1:
      - Medium Margherita - 150.0 CZK (Toppings: No toppings)
      Total: 150.0 CZK
      Payment Method: Credit Card
    
    Order 2:
      - Large Pepperoni - 265.0 CZK (Toppings: Extra Cheese, Pineapple)
      Total: 265.0 CZK
      Payment Method: Cash
    
    Overall Sales Total: 415.0 CZK
V aplikaci jsem nedělal File Manager. Přišlo mi to zbytečné, vzhledem k tomu, že cílem mělo být vyzkoušet si rozčlenění do MVC architektury a použití návrhových vzorů. Proto jsem neřešil hromadu dalších věcí jako rušení objednávky adminem a jen stroze dal např. dvě metody platby, předzadané heslo pro admina atd.
V rámci urychlení práce jsem využíval AI a postupně přidával jednotlivé funkcionality, případně odlaďoval chyby.
Architektura se víceméně drží zadání, proto ji ani zde neuvádím.
Stručný popis:
Zákazník si vytvoří objednávku ("Order Pizza"). V rámci ní si může zvolit jakoukoliv pizzu, případně si objednat více druhů pizzy. Pokud se splete nebo si objednávku rozmyslí, může objednávku zrušit ("Cancel Current Order"). Pro kontrolu objednávky před zaplacením může zvolit ("View Current Order"). Pokud je spokojen, zadá způsob platby ("Make Payment"). Objednávka je zaplacena a uložena do souboru orders.json (zvolen json kvůli kompatibilitě). Prodejce se přihlašuje přes "Admin" menu po zadání hesla "admin". Následně se načte ze souboru přehled všech objednávek a celková částka všech objednávek.  
