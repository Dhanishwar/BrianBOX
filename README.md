# Detecting depression using EEG sensor. 
The main motive of the project is to detect mental illness such as depression, anxiety using EEG sensor. Currently the psychiatrists are using various Q&A sessions and Lab test to diagnose the mental condition of a person. Such methods are strenuous for psychiatrists and excruciating for the patients who undergo them. Because of such reasons we have come up with a solution which was to diagnose depression and other mental related issues using EEG sensor. 
![alt text](https://www.riecktron.co.za/image/cache/data/products/14455-02-600x600.jpg)
Here the patient just need to wear a EEG headset which would look like the one that is shown in the image. We have used Neurosky MindWave Mobile 2.
# Working of the Program
We are using `NeuroPy` class to get the raw value from EEG sensor and convert it to Alpha, Beta, Gamma waves. This program can also detect a person attention level, concentration. And then we are using `brainbox.py` program to classify, compare the **beta, alpha, gamma waves**. This result is then sent as a message to the number enrolled in the **Twilio** account.
