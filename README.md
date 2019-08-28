# IoT-Desktop-Security
With a raspberry Pi, a PIR sensor, and PubNub's publishing and subscribing technology, you can create your own desktop security app. Once properly programmed, the motion sensor will be able to detect an intruder, and will then publish a message directly to the app. There is also potential to configure additional features, such as a raspberry Pi camera to photograph the intruder.

![](mgs.gif)

# Requirements to run:
* Latest version of Python
* PubNub's sdk's for python and react installed
* React Native CLI
* Node 
* watchman
* Xcode and iOS simulator
* Things like react-native-modal or react-navigation installed and link if you wanted to intergrate that into your app

# How To Run:
1.) First, you need to make sure you install the latest version of Node and watchman. Type this command `brew install node` and `brew install watchman` in your terminal

2.) Then, install react native CLI with `npm install -g react-native-cli` in your terminal.

3.) Then, to create your new app type `react-native init NameOfProject` in your terminal.

4.) You can then go into project now named NameOfProject and edit the App.js file to your chooising.

5.) To use pubnub type this commmand `npm install --save pubnub pubnub-react` in the terminal, while in your project's directory. 

6.) You can find your free API keys and other sdk's at [PubNub's website](https://www.pubnub.com/).

7.) Then, you can now add in features for your apps like react native navigation or react native modal. For my project I used react native modal.

8.) While still in your project's directory, type `npm install --save react-native-modal` in your terminal to obtain the library. You also wiil most likely need to manually link the library, to do so type `react-native link react-native-modal` in your terminal.

9.) Next, make sure your pi is updated and ssh is enabled. 

10.) Change your director into your project folder containing the python file that will be opperated by the pi and type `pip install 'pubnub>=4.1.5'` to install PubNub's sdk. You can find free API keys at [PubNub's website](https://www.pubnub.com/).

11.) Now you are fully setup to run this project. 

# Additional steps to use the Pi camera:
1.)  To enable the camera feature, type `sudo raspi-config` in the terminal to pull up the configuration menu.

2.) If the camera option is not present run the commands `sudo apt-get update` and `sudo apt-get upgrade`.

3.) Then if you type `sudo raspi-config` in again you should see the camera option. Scroll down and enable it.

4.) Include this line `from picamera import PiCamera` at the top of your code to use the camera's functions in your python code.
