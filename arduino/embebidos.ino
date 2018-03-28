#define trigPin 3         //Definimos Trigger pin
#define echoPin 4
#define trigPin2 6         //Definimos Trigger pin
#define echoPin2 7         //Definimos Echo pin
#define trigPin3 11         //Definimos Trigger pin
#define echoPin3 12

int duracion, distancia;
int duracion2, distancia2;
int duracion3, distancia3;
void setup() {
    Serial.begin (9600);
    pinMode(trigPin, OUTPUT);
    pinMode(echoPin, INPUT);
    pinMode(trigPin2, OUTPUT);
    pinMode(echoPin2, INPUT);
    pinMode(trigPin3, OUTPUT);
    pinMode(echoPin3, INPUT);
}

void loop() {   

    digitalWrite(trigPin, HIGH);   //El siguiente ciclo trigPin / echoPin
    //delayMicroseconds(1000);  
    digitalWrite(trigPin, LOW);    //objeto más cercano haciendo rebotar ondas sonoras fuera de ella
    duracion = pulseIn(echoPin, HIGH);            //Determina la duración
  
    digitalWrite(trigPin2, HIGH);   //El siguiente ciclo trigPin / echoPin
    //delayMicroseconds(1000);       //se utiliza para determinar la distancia del
    digitalWrite(trigPin2, LOW);    //objeto más cercano haciendo rebotar ondas sonoras fuera de ella
    duracion2 = pulseIn(echoPin2, HIGH);            //Determina la duración
    
    digitalWrite(trigPin3, HIGH);   //El siguiente ciclo trigPin / echoPin
    //delayMicroseconds(1000);  
    digitalWrite(trigPin3, LOW);    //objeto más cercano haciendo rebotar ondas sonoras fuera de ella
    duracion3 = pulseIn(echoPin3, HIGH);            //Determina la duración

    distancia = (duracion/2) / 29.1;             //Calcula la distancia en cm

    distancia2 = (duracion2/2) / 29.1;             //Calcula la distancia en cm
    
    distancia3 = (duracion3/2) / 29.1;             //Calcula la distancia en cm

    Serial.print(distancia);
    Serial.print(" ");
    Serial.print(distancia2);
    Serial.print(" ");
    Serial.println(distancia3);
}
