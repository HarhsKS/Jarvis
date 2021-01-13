int datafromUser=0;
const int led = 8; //Define the led Pin address insted of 8
void setup() {
  // put your setup code here, to run once:
  pinMode( led , OUTPUT );
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0)
  {
    datafromUser=Serial.read();
  }

  if(datafromUser == '1')
  {
    digitalWrite( led , HIGH );
  }
  else if(datafromUser == '0')
  {
    digitalWrite( led, LOW);
  }
  
}
