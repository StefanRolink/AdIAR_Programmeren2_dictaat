#include <Ethernet.h>

byte mac[] = {0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF};
byte ip[] = {192,168,1,3};
EthernetServer server = EthernetServer(23); //Gebruik poort 23 (telnet)

void setup() 
{
  Ethernet.begin(mac,ip); // init EthernetShield
  server.begin();
}

void loop() 
{
  EthernetClient client = server.available();   

  if(client)                                    // Wacht op een nieuwe client
  {
    while(client.connected())                   // Zolang client is verbonden:
    {
      client.println("Hallo vanuit Arduino!");  // Stuur bericht
    }
  }
}
