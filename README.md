# IoT-Desktop-Security
With a raspberry Pi, a PIR sensor, and PubNub's publishing and subscribing technology, you can create your own desktop security app. Once properly programmed, the motion sensor will be able to detect an intruder, and will then publish a message directly to the app. There is also potential to configure additional features, such as a raspberry Pi camera to photograph the intruder, or a speaker to sound once the intruder is detected.

![](mgs.gif)

# Requirements to run:
* Latest version of Python
* PubNub's sdk's for python and react installed
* React Native CLI
* Node 
* Xcode and iOS simulator
* Things like react-native-modal or react-navigation installed and link if you wanted to intergrate that into your app

# How To Run
1.) First, you need to make sure you install the latest version of Node. Type this command 'brew install node' in your terminal
2.) Then, instal react native CLI with 'npm install -g react-native-cli' in your terminal.
3.) Then, to create your new app type 'react-native init NameOfProject' in your terminal.
4.) You can then go into this folder named NameOfProject and edit the App.js file
5.) Inorder to use PubNub's publishing and subscribing methods you will need to change directories in to your project and type this commmand 'npm install --save pubnub pubnub-react'
6.) Then, you can now add in features for your apps like react native navigation or react native modal. For my project I used react native modal.
7.) While still in your project's directory, type 'npm install --save react-native-modal' in your terminal to obtain the library. You also wiil most likely need to manually link the library, to do so type 'react-native link react-native-modal' in your terminal.
8.) Next, make sure your pi is updated and ssh is enabled. 
9.) Change your director into your project folder containing the python file that will be opperated by the pi and type 'pip install 'pubnub>=4.1.5'' to install PubNub's sdk.
10.) Now you are fully setup to run this project 