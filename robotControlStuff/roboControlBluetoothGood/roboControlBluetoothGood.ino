int incomingByte = 0;   // for incoming serial data
char data = 0;            //Variable for storing received data

const byte numChars = 32;
char receivedChars[numChars];
char tempChars[numChars];        // temporary array for use when parsing

      // variables to hold the parsed data
char wheelSide = '0';
int velocity = 0;
float floatFromPC = 0.0;

boolean newData = false;

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
  

  if(Serial.available() > 0)      // Send data only when you receive data:
   {
    recvWithStartEndMarkers();
    if (newData == true) {
        strcpy(tempChars, receivedChars);
            // this temporary copy is necessary to protect the original data
            //   because strtok() used in parseData() replaces the commas with \0
        parseData();
        makeGo();
        newData = false;
    } 
   }  
}

void recvWithStartEndMarkers() {
    static boolean recvInProgress = false;
    static byte ndx = 0;
    char startMarker = '<';
    char endMarker = '>';
    char rc;

    while (Serial.available() > 0 && newData == false) {
        rc = Serial.read();

        if (recvInProgress == true) {
            if (rc != endMarker) {
                receivedChars[ndx] = rc;
                ndx++;
                if (ndx >= numChars) {
                    ndx = numChars - 1;
                }
            }
            else {
                receivedChars[ndx] = '\0'; // terminate the string
                recvInProgress = false;
                ndx = 0;
                newData = true;
            }
        }

        else if (rc == startMarker) {
            recvInProgress = true;
        }
    }
}

void parseData() {      // split the data into its parts

    char * strtokIndx; // this is used by strtok() as an index

    strtokIndx = strtok(tempChars,",");      // get the first part - the string
    //strcpy(wheelSide, strtokIndx); // copy it to wheelSide
    wheelSide = strtokIndx[0];
  
    strtokIndx = strtok(NULL, ","); // this continues where the previous call left off
    velocity = atoi(strtokIndx);     // convert this part to an integer

}

void makeGo() {
    Serial.print("Wheel: ");
    Serial.println(wheelSide);
    Serial.print("Velocity: ");
    Serial.println(velocity);

    movement(wheelSide, velocity);
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

void leftForward(int velocity)
{
  
  analogWrite(7,velocity);
  digitalWrite(50,HIGH);
  digitalWrite(51,LOW);
  Serial.print("R Forward   ");
}

void rightForward(int velocity)
{
  analogWrite(6,velocity);
  digitalWrite(40,HIGH);
  digitalWrite(41,LOW);
  Serial.print("L Forward   ");
}

void leftBackward(int velocity)
{
  velocity = abs(velocity);
  analogWrite(7,velocity);
  digitalWrite(50,LOW);
  digitalWrite(51,HIGH);
  Serial.print("R BACK   ");
}

void rightBackward(int velocity)
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
