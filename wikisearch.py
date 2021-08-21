import speech_recognition as sr
import pyttsx3 
import wikipedia
from mediawiki import MediaWiki
 

  
# Initialize the recognizer 
r = sr.Recognizer() 
  
# Function to convert text to
# speech
def SpeakText(command):
      
    engine = pyttsx3.init('nsss')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    #engine.setProperty("rate", 178)
    engine.say(command) 
    engine.runAndWait()
      

def wiki(title):
    """para = wikipedia.summary(title , sentences = 2)
    print(para)
    SpeakText(para)"""
    try:
        wikipedia = MediaWiki()
        p = wikipedia.summary(title,sentences = 2)
        print(p)
        SpeakText(p)

    except:
        SpeakText("Sorry , cant find an adequate paragraph about this title")
        pass

    return 

      
# Loop infinitely for user to
# speak
def internet():
    while(1):    
          
        # Exception handling to handle
        # exceptions at the runtime
        try:
              
            # use the microphone as source for input.
            with sr.Microphone() as source2:
                  
                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level 
                SpeakText('adjusting noises for clear inputs')
                r.adjust_for_ambient_noise(source2, duration=1)
                print("speak now")
                SpeakText("what do you want to know ? speak the title")
                #listens for the user's input 
                audio2 = r.listen(source2)
                  
                # Using ggogle to recognize audio
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()
      
                print("Did you say "+MyText)
                SpeakText("searching for " + MyText)

                wiki(MyText)
                #SpeakText("thanks for asking !")
                #exit() 
                return 
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
              
        except sr.UnknownValueError:
            print("unknown error occured")

internet()