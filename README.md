# Scraper01

Zorg ervoor dat in je Virtual Machine (VM) python3 en pip3 hebt geïnstalleerd. 

Voor deze opdracht hebben we deze packages nodig:
- BeautifulSoup from bs4 
- requests
- pandas
- DataFrame from pandas
- time

Hierna maak ik een functie aan die alle informatie van de website gaat scrapen.
Hier importeer ik de url van de website via de requests package en maak ik een lege dataframe aan.
Daarna ga ik alle informatie scrapen, dit deel ik in vier kolommen (hash, hour, amountBTC & amountUSD). 
Deze data stop ik in een tweede dataframe die ik ga omkeren, de kolommen worden rijen en die rijen worden kolommen. Deze dataframe ga ik dan toevoegen aan de lege dataframe die ik eerder had gemaakt. 

Dan ga ik de data in de vierde (amountUSD) kolom (of 3e gezien we beginnen met tellen vanaf 0) vervangen. Het dollar teken verwijderen we en de komma vervangen we door niets. We zetten het type van de kolom als float zo kunnen we steeds het maximum bedrag van de kolom nemen. Dit resultaat return ik dan. 

Als laatste stap neem ik een loop hierin gaan we de functie uitvoeren en uitprinten en dan wachten we één minuut voor de volgende output. 

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Mongo02

Voor deze opdracht hebben we deze packages nodig:
- BeautifulSoup from bs4
- requests
- pandas
- DataFrame from pandas
- time
- pymongo
- json

Voor de tweede opdracht heb ik een bash file gemaakt die je kan runnen zodat Mongo wordt gedownload op je VM. Dit script kan je vinden onder de naam myscript_download.sh. In het pythonscript mongo02.py vind je de code die het gevraagde resultaat opslaagt in de database. Hoe we op het resultaat komen is hierboven reeds vermeld. Het verschil is dat ik nu eerst nog een nieuwe database aanmaak in mongo en hier ook een nieuwe collectie aan toevoeg. Wanneer ik dan op het resultaat kom door de website te scrapen zet ik het resultaat in de reeds aangemaakte collectie. Verder vind je nog myscript_run_realtime.sh, wanneer je deze file runt gaat het python script automatisch elke 60 seconden opnieuw runnen.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Redis03

Voor het eerste deel van deze opdracht hebben we deze packages nodig:
- BeautifulSoup from bs4
- requests
- pandas
- DataFrame from pandas
- time

Voor het tweede deel hebben we deze packages nodig:
- pymongo
- redis
- pandas
- time

In het bestand script_download_redis.sh vind je hoe je redis moet downloaden op je VM. Voor dit programma hebben we twee bestanden nodig. Het eerste is Redis03.py hierin scrapen we de website zoals in de vorige oefeningen reeds uitgelegd. Er zijn maar enkele veranderingen die we moeten doen. We declareren eerst Redis zodat we onze data kunnen doorsturen. Verder converten we onze dataframe naar een string zodat er geen problemen zijn al we de data doorsturen. Hierna gaan we de data dan echt doorsturen met de set methode.
Dan gaan we verder met de tweede stap, hier gaan we de data die we in Redis hebben gestoken bekijken en de hoogste waarde bepalen. De hoogste waarde gaan we dan doorsturen naar Mongo. Dit script kunnen we vinden onder de naam Redis_to_Mongo.py. Als eerste declareren we ook hier redis, we gaan de data daarna inlezen met de get methode van Redis. Dan converten we dan string terug naar een dataframe. Als volgende declareren we Mongo, we maken een database aan en een collectie. De volgende stap is dan de hoogste waarde gaan bepalen, dit is ook eerder al uitgelegd bij de eerste oefening. Verder bepalen we de index van het bekomen bedrag zodat we de andere data ook kunnen bepalen. Hierna gaan we de data initialiseren en aan de collectie in Mongo toevoegen. De laatste stap in dit script is het leegmaken van Redis na 60 seconden met de methode expire.
