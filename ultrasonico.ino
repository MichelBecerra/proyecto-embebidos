#define trigPin 6         //Definimos Trigger pin
#define echoPin 7         //Definimos Echo pin
#define trigPin2 3         //Definimos Trigger pin
#define echoPin2 4
#define trigPin3 11         //Definimos Trigger pin
#define echoPin3 12

int rangoMaximo = 40;      //Rango máximo necesitado
int rangoMinimo = 0;      //Rango mínimo necesitado
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
    digitalWrite(trigPin2, HIGH);   //El siguiente ciclo trigPin / echoPin
    delayMicroseconds(1000);       //se utiliza para determinar la distancia del
    digitalWrite(trigPin2, LOW);    //objeto más cercano haciendo rebotar ondas sonoras fuera de ella
    duracion2 = pulseIn(echoPin2, HIGH);            //Determina la duración

    digitalWrite(trigPin, HIGH);   //El siguiente ciclo trigPin / echoPin
    delayMicroseconds(1000);  
    digitalWrite(trigPin, LOW);    //objeto más cercano haciendo rebotar ondas sonoras fuera de ella
    duracion = pulseIn(echoPin, HIGH);            //Determina la duración
    
    digitalWrite(trigPin3, HIGH);   //El siguiente ciclo trigPin / echoPin
    delayMicroseconds(1000);  
    digitalWrite(trigPin3, LOW);    //objeto más cercano haciendo rebotar ondas sonoras fuera de ella
    duracion3 = pulseIn(echoPin3, HIGH);            //Determina la duración

    distancia = (duracion/2) / 29.1;             //Calcula la distancia en cm
    if (distancia >= rangoMaximo || distancia <= rangoMinimo){
      Serial.println(distancia);     //Envía a la computadora por el puerto serial el mensaje: 'La casa está segura.'
    } else {    
      Serial.println(distancia); //Envía a la computadora por el puerto serial el mensaje: 'Hay un intruso en la casa.'
    }

    distancia2 = (duracion2/2) / 29.1;             //Calcula la distancia en cm
    if (distancia2 >= rangoMaximo || distancia2 <= rangoMinimo){
      Serial.println("La casa está segura2.");     //Envía a la computadora por el puerto serial el mensaje: 'La casa está segura.'
    } else {    
      Serial.println("Hay un intruso en la casa2."); //Envía a la computadora por el puerto serial el mensaje: 'Hay un intruso en la casa.'
    }
    
    distancia3 = (duracion3/2) / 29.1;             //Calcula la distancia en cm
    if (distancia3 >= rangoMaximo || distancia3 <= rangoMinimo){
      Serial.println("La casa está segura3.");     //Envía a la computadora por el puerto serial el mensaje: 'La casa está segura.'
    } else {    
      Serial.println("Hay un intruso en la casa3."); //Envía a la computadora por el puerto serial el mensaje: 'Hay un intruso en la casa.'
    } 
    delay(500);                          // Hace un retardo de 0.5 segundos antes de la próxima lectura.
}
