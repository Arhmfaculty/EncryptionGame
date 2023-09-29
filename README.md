#Encryption Game

A game designed to introduce individuals to knowledge of learning about cryptography. The game focuses
on how individuals can analyze a cyphertext and decode it using a provided key. The game consists of 
sentences that are encrypted using ceaser cipher. Series of sentence are randomly generated for the user
using looping, with a random cipher key which randomly turn the sentence The user will be asked to provide 
the decrypted sentence by using the key we have provided. Once the sentence is provided, the system will 
take up the sentences and break it down to lists of words. The user’s works will be compared to our works 
for accuracy. In the case where the users type less words than required, they will be notified about that, and 
the correct sentence will be provided. The same thing will be done whenever the user types more words 
than expected. There will be a timer countdown to test how fast the user decodes the message. If they guess 
correctly, they will be notified and congratulates for getting it correct. We are using the tkinter module due 
to its user friendliness. We are using it to implement the window for the typing, with selected color, 
geometry, and other features. Our timer module is also implemented on the front-end part of our project, 
such that the user can see while typing. After the user has run our program, the interface will appear and 
will allow them to start. Once the user clicks on the start button, now the timer function is triggered to start 
counting. We have also included the input are for the user to type their decrypted words. Because we can 
call multiple functions at the same time, we use threading module. This module helps to implement 
multitasking during our timer module. 

CONCEPTS USED IN THE GAME:

• Cryptography 
• Tkinter
• Loops
• Iterations
• Sequence
• Threading module
• Time module
