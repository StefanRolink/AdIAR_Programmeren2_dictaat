#include <Ethernet.h>

byte mac[] = {0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED};
IPAddress ip(192, 168, 1, 3);

EthernetServer server(80); // start http server on port 80

void setup()
{
  Ethernet.begin(mac, ip);

  server.begin();
}
