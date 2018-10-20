int incomingByte = 0;   // for incoming serial data
char data = 0;            //Variable for storing received data

void setup() {
  Serial.begin(115200);   // opens serial port, sets data rate to 9600 bps
  
  pinMode(50,OUTPUT);
  pinMode(51,OUTPUT);
  pinMode(7,OUTPUT);
  digitalWrite(7,0);

  pinMode(40,OUTPUT);
  pinMode(41,OUTPUT);
  pinMode(6,OUTPUT);
  digitalWrite(6,0);

  
}

void loop() {
  int velocity = 255;

  if(Serial.available() > 0)      // Send data only when you receive data:
   {
    
      data = Serial.read();             //Read the incoming data & store into data
      if(data != '\n' && data != '\r'){
        Serial.print(data);          //Print Value inside data in Serial monitor
        Serial.print("\n");        

        if(data == '1') {
          Serial.print("succ");
          movement('R',velocity);
          movement('L',velocity * .90);
        }
        else if (data == '0') {
          movement('R',-velocity);
          movement('L',-velocity * .95);
        }
        else if (data == '2') {
          leftStop();
          rightStop();
        }
        Serial.print("Post Data: ");
        Serial.print(data);
        Serial.print("\n");
      }
   }
}

void movement(char wheel, int velocity)
{
  if(wheel == 'R')
  {
    if(velocity >= 0)
      rightForward(velocity);
    else
      rightBackward(velocity);
  }
  else if(wheel == 'L')
  {
    if(velocity >= 0)
      leftForward(velocity);
    else
      leftBackward(velocity);
  }
}

void rightForward(int velocity)
{
  
  analogWrite(7,velocity);
  digitalWrite(50,HIGH);
  digitalWrite(51,LOW);
  Serial.print("R Forward   ");
}

void leftForward(int velocity)
{
  analogWrite(6,velocity);
  digitalWrite(40,HIGH);
  digitalWrite(41,LOW);
  Serial.print("L Forward   ");
}

void rightBackward(int velocity)
{
  velocity = abs(velocity);
  analogWrite(7,velocity);
  digitalWrite(50,LOW);
  digitalWrite(51,HIGH);
  Serial.print("R BACK   ");
}

void leftBackward(int velocity)
{
  velocity = abs(velocity);
  analogWrite(6,velocity);
  digitalWrite(40,LOW);
  digitalWrite(41,HIGH);
  Serial.print("L BACK   ");
}

void rightStop()
{
  analogWrite(7,0);
  digitalWrite(50,LOW);
  digitalWrite(51,LOW);
  Serial.print("R STOP   ");  
}

void leftStop()
{
  analogWrite(6,0);
  digitalWrite(40,LOW);
  digitalWrite(41,LOW);
  Serial.print("L STOP   ");  
}
