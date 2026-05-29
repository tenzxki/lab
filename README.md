# LAB Checkoff øvelser

Del 1 
1.
ssh brukes til kommunikasjon mellom systemer. Kommunikasjonen er sikker og kryptert. Brukt for sikker fjernadministrasjon på tvers av alle typer nettverk. 

2.
ipconfig viser ip adresse
statisk ip adresse forblir fast over tid og er ideelle for servere, ekstern tilgang, osv. 
dynamisk ip adresser endres med jevne mellomrom via dhcp. Ofte det vanlig alternativer for hjemmetilkoblinger. 

3.
systemctl status mariadb sjekker om mariadb kjører. 
En tjeneste/service i Linux er et program som konstant kjører i bakgrunnen og tilbyr funksjonalitet til systemet eller andre programmer. For eksempel database og nettverkstjenester

4.
En port er en inngang for tilkoblinger på en datamaskin. Port brukes både som fysiske tilkoblinger og virtuell inngang for tjenester på en maskin. Eksempler som port 22 som er standard porten for SSH, port 5000 og 8000 er ofte brukt av applikasjoner og utviklingsservere.

5.
Jeg åpnet port 5000 og det kan være nødvendig for å kjøre en lokal utviklingsserver for eksempel flask som skal nås fra andre enheter


Del 2 

6.
create database lab;

7.
CREATE TABLE brukere ( id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, brukernavn VARCHAR (255) NOT NULL, password_hash VARCHAR (255) NOT NULL );

8.
INSERT INTO brukere (brukernavn, password_hash) VALUES ('test', 'test1234');

9.
SELECT * FROM brukere

10.
WHERE brukes for å filtrere rader i en SELECT, UPDATE eller DELETE. Bare de radene som oppfyller en betingelse påvirkes eller returneres. Eksempel SELECT * FROM brukere WHERE id = 1
