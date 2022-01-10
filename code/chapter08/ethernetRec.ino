#include <Ethernet.h>

byte mac[] = {0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF};
byte ip[] = {192,168,1,3};  // Pas aan naar eigen netwerkconfiguratie
EthernetServer server = EthernetServer(23);  // Gebruik poort 23 (telnet)

void setup() 
{
  Serial.begin(9600);     // Init Serial
  Ethernet.begin(mac,ip); // Init EthernetShield
  server.begin();
}

void loop() 
{
  EthernetClient client = server.available();   // Wacht op een nieuwe client
  if(client)
  {
    while(client.available() > 0)               // Als client is verbonden
    {
      char data = client.read();                // Haal verstuurde data op
      Serial.print(data);                       // en schrijf naar het scherm
    }
  }
}
