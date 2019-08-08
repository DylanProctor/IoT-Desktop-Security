import React from "react";
import { View, Text, StyleSheet, Button, TouchableOpacity } from "react-native";
import PubNubReact from 'pubnub-react';
import Modal from "react-native-modal";


export default class App extends React.Component {
  constructor(props) {
    super(props);
    this.pubnub = new PubNubReact({
      publishKey: "PUBLISH-KEY",
      subscribeKey: "SUBSCRIBE-KEY"
    });
    this.pubnub.init(this);
  }

  componentDidMount() {
    this.pubnub.subscribe({channels: ['Ch1']});
    this.pubnub.getMessage('Ch1');
  }

  state = {
    isModalVisible: false
  };

  toggleModal = () => {
    this.setState({ isModalVisible: !this.state.isModalVisible});
  };


  render() {
    const messages = this.pubnub.getMessage('Ch1');
    return (
      <View style = {styles.container}>
        <TouchableOpacity
          style = {styles.button2}
          onPress={this.toggleModal}
        >
          <Text style = {styles.buttonText}>
            Information 
          </Text>
          <Modal 
            isVisible = {this.state.isModalVisible}
          >
            <View style={styles.modalContent}>
              <Text style = {styles.heading}>
                Welcome to IoT Desktop Security!
              </Text>
              <Text style= {styles.heading}>
                To arm your motion sensor please tap "ON", and
                to disarm your motion sensor please tap "OFF"
              </Text>
              <Button title="Back" onPress={this.toggleModal} />
            </View>
          </Modal>
        </TouchableOpacity>
        <TouchableOpacity
          style = {styles.button1}
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
          style = {styles.button1}
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


const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#F5FCFF'
  },
  modalContent:{
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#F5FCFF',
    padding: 20,
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
  button1: {
    textAlign: 'center',
    padding: 10,
    marginVertical: 10, 
    shadowColor: 'rgba(0,0,0, .4)',
    shadowOffset: { height: 1, width: 1 }, 
    shadowOpacity: 1,
    shadowRadius: 1,
    backgroundColor: '#DDDDDD',
    height: 50,
    width: 100,
    justifyContent: 'center',
    alignItems: 'center',
    flexDirection: 'row',     
  },
  button2:{
    textAlign: 'center',
    padding: 10,
    marginVertical: 10, 
    shadowColor: 'rgba(0,0,0, .4)',
    shadowOffset: { height: 1, width: 1 },
    shadowOpacity: 1, 
    shadowRadius: 1, 
    backgroundColor: '#DDDDDD',
    elevation: 2,
    height: 50,
    width: 200,
    justifyContent: 'center',
    alignItems: 'center',
    flexDirection: 'row',
  }
});
