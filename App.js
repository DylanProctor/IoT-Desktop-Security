import React from "react";
import { View, Text, StyleSheet, Button, TouchableOpacity } from "react-native";
import { createStackNavigator, createAppContainer } from "react-navigation";
import PubNubReact from 'pubnub-react';
import Modal from "react-native-modal";


class HomeScreen extends React.Component {
  render() {
    return (
      <View style = {styles.container}>
        <Text style = {styles.heading}>
          Welcome to IoT Desktop Security
        </Text>
        <TouchableOpacity
          style = {styles.button}
          onPress={() => this.props.navigation.navigate('Details')}
        >
          <Text style = {styles.buttonText}>
            Details
          </Text>
        </TouchableOpacity>
      </View>
    );
  }
}


class DetailsScreen extends React.Component {
  constructor(props) {
    super(props);
    this.pubnub = new PubNubReact({
      publishKey: "pub-c-964c6e62-8094-417b-a4bd-979dd56a7d52",
      subscribeKey: "sub-c-d11e8f9a-9871-11e9-8994-3e832ec25d8b"
    });
    this.pubnub.init(this);
  }

  componentDidMount() {
    this.pubnub.subscribe({channels: ['Ch1']});
    this.pubnub.getMessage('Ch1');
  }

  render() {
    const messages = this.pubnub.getMessage('Ch1');
    return (
      <View style = {styles.container}>
        <Text style = {styles.heading}>
          Press "ON" to enable the motion sensor and "OFF" to diable the motion sensor
        </Text>
        <TouchableOpacity
          style = {styles.button}
          onPress={() => this.props.navigation.navigate('Home')}
        >
          <Text style = {styles.buttonText}>
            Home
          </Text>
        </TouchableOpacity>
        <TouchableOpacity
          style = {styles.button}
          onPress={() => this.pubnub.publish({
            message: 'ON',
            channel: 'Ch2'
          })}
        >
          <Text style = {styles.buttonText}>
            ON
          </Text>
        </TouchableOpacity>
        <TouchableOpacity
          style = {styles.button}
          onPress={() => this.pubnub.publish({
            message: 'OFF',
            channel: 'Ch2'
          })}
        >
          <Text style = {styles.buttonText}>
            OFF
          </Text>
        </TouchableOpacity>
        {messages.map((m) => <Text style = {styles.alert}>{m.message}</Text>)}
      </View>
    );
  }
}


const RootStack = createStackNavigator(
  {
    Home: {
      screen: HomeScreen,
    },
    Details: {
      screen: DetailsScreen,
    },
  },
  {
    initialRouteName: 'Home',
  }
);


const AppContainer = createAppContainer(RootStack);

export default class App extends React.Component{
  render() {
    return <AppContainer/>;
  }
}


const styles = StyleSheet.create({
  container: {
      flex: 1,
      justifyContent: 'center',
      alignItems: 'center',
      backgroundColor: '#F5FCFF'
  },
  heading: {
      fontSize: 25,
      textAlign: 'center',
      margin: 10
  },
  buttonText:{
      fontSize: 20,
      textAlign: 'center'
  },
  alert: {
      fontSize: 30,
      textAlign: 'center',
      color: 'red'
  },
  button: {
      textAlign: 'center',
      padding: 10,
      marginVertical: 10, 
      shadowColor: 'rgba(0,0,0, .4)', // IOS
      shadowOffset: { height: 1, width: 1 }, // IOS
      shadowOpacity: 1, // IOS
      shadowRadius: 1, //IOS
      backgroundColor: '#DDDDDD',
      elevation: 2, // Android
      height: 50,
      width: 100,
      justifyContent: 'center',
      alignItems: 'center',
      flexDirection: 'row',     
  }
});
