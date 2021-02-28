#include <Debounce.h>

/*--------------------------------------------------------
TP "Shibuya Trafic Ligths"
(C)F6EQN 2017

Une application Arduino pour réguler les flux dans un carrefour
Version séquence "Jour" & "Nuit"
-------------------------------------------------------
*/

//Déclaration variables:

int attente;// variable pour la temporisation (utilisation de delay)
int time,old_time;//varialble pour la temporisation (utilisation de millis)
char niveau;// variable pour la conversion int/char pour l'écriture dans les ports
int i,j,mot;//variables de pointage (pointeurs) et de destination pour lecture en table
#define bouton 3 // variable pour enregistrer l'appui sur le bouton d'appel pietons
boolean pieton=false, pieton_2=false;
const int sensorPin=A0;unsigned sensorVal=0; //identifie l'entree analogique pour la LDR
//-----------------------------------------------------
//table des séquences
//sequence "jour"
int sequence_j[6][10]={

  {1,0,0,1,0,1,0,1,0,0},
  {0,0,1,1,0,0,1,1,0,0},
  {0,1,0,1,0,1,0,1,0,0},
  {1,0,0,1,0,1,0,1,0,0},
  {1,0,0,0,1,1,0,0,0,1},
  {1,0,0,1,0,1,0,0,1,0}
};
// table des temporisations
unsigned long duree_j[6]={1000,10000,3000,1000,10000,3000};  
//sequence "nuit"
int sequence_n[6][10]={

  {0,1,0,1,0,1,0,0,1,0},
  {0,0,0,0,0,0,0,0,0,0},
  {0,1,0,1,0,1,0,0,1,0},
  {0,0,0,0,0,0,0,0,0,0},
  {0,1,0,1,0,1,0,0,1,0},
  {0,0,0,0,0,0,0,0,0,0},
  
};
long duree_n[6]={1000,1000,1000,1000,1000,1000};

//sequence "pietons"
int sequence_p[3][10]={

  {0,1,0,1,0,1,0,0,1,0},
  {1,0,0,0,1,0,1,1,0,0},
  {1,0,0,1,0,1,0,1,0,0},
  
  
};
long duree_p[3]={3000,10000,3000};


//-------------------------------------------------------
//Sous programme temposisation
//
void tempo(int attente){
 
  // boucle while pour temporisation en utilisant le temporisateur millis() et une itération de 10 ms
  while (time-old_time<attente && pieton==false){
    time=millis();
    delay(10);
  };
  old_time=time;
}
//-------------------------------------------------------
//Sous programme temposisation pour la sequence pieton
//
void tempo_2(int attente){
 
  delay(attente);// version avec delay()
  
}

//--------------------------------------------------------
// Sous programme "Jour"
//--------------------------------------------------------
void jour(){
  for(int j=0; j<6; j++){
  
    for(int i=0; i<=10; i++){ 
    // boucle "pour" écriture des bits de séquence
      if (sequence_j[j][i]==0){
        digitalWrite(i+4,LOW);}
      else{digitalWrite(i+4,HIGH);}
  
  }
   attente=duree_j[j];
    tempo(attente);// appel sbr temporisation dont la valeur est indexée dans une table
   }
}
//--------------------------------------------------------
// Sous programme "Nuit"
//--------------------------------------------------------
void nuit(){
  for(int j=0; j<6; j++){
  
    for(int i=0; i<=10; i++){ 
    // boucle "pour" écriture des bits de séquence
      if (sequence_n[j][i]==0){
        digitalWrite(i+4,LOW);}
      else{digitalWrite(i+4,HIGH);}
  
  }
   attente=duree_n[j];
    tempo(attente);// appel sbr temporisation dont la valeur est indexée dans une table
   }
}
//--------------------------------------------------------
// SBR "Pietons"
//--------------------------------------------------------
void pedestrian(){
  detachInterrupt(digitalPinToInterrupt(bouton)); // inhibe l'interruption pour permettre les tempos du sbr "pieton"
  for(int j=0; j<3; j++){
  
    for(int i=0; i<=10; i++){ 
    // boucle "pour" écriture des bits de séquence
      if (sequence_p[j][i]==0){
        digitalWrite(i+4,LOW);}
      else{digitalWrite(i+4,HIGH);}
  Serial.print(i);Serial.println(j);
  }
   attente=duree_p[j];
    tempo_2(attente);// appel sbr temporisation dont la valeur est indexée dans une table
   }
     attachInterrupt(digitalPinToInterrupt(bouton),interrupt_1,FALLING);// réactive l'interruption
     pieton=false;pieton_2=false; //rearme l indicateur de demande
}
//--------------------------------------------------------
// SBR Interruption INT1 -> SBR "Pietons"
//--------------------------------------------------------
void interrupt_1(){
   pieton=true;pieton_2=true; //signalent la demande des pietons. Utilise deux variables (pour la tempo et pour le test) pour simplifier
}
//--------------------------------------------------------
// SBR Lecture LDR
//--------------------------------------------------------
void lect_LDR(){
  int sensor_read=analogRead(sensorPin);// lit le port A0
  delay(10); //delai pour la conversion
  sensorVal=map(sensor_read,0,1023,0,255);
  
  
}

//--------------------------------------------------------
// Initialisation
//--------------------------------------------------------

void setup() {
  Serial.begin(9600);// init de la liaison série pour visualisation écriture
  // initialisatin des ports D4 à D13 en sortie
  for(int p=4; p<=13; p++){
  pinMode(p,OUTPUT);
  }
  // initialise les port D1 et D2 en entrée (pour les boutons poussoirs)
  for(int p=2; p<=3; p++){
  pinMode(p,INPUT_PULLUP);
  }
  attachInterrupt(digitalPinToInterrupt(bouton),interrupt_1,FALLING);
}
//--------------------------------------------------------
// MAIN program
//--------------------------------------------------------
void loop() {
  lect_LDR();Serial.println(sensorVal);
  if (sensorVal>100){
    jour();}
    else{nuit();}
  if (pieton_2==true){pedestrian();};//teste la demande pieton et appelle le sbr "pieton"

}
