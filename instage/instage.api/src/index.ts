import express from 'express'
//import { MqttGateway, MqttConfig } from './gateways/MqttGateway'
import mqtt from 'mqtt'
import { connect } from 'mqtt'
import { getArray } from './models/ArrayValues'

const app = express()
const PORT = 3000

interface MqttConfig {
    host: string
    topic: string
    port?: number
}
// Usage
const mqttConfig: MqttConfig = {
    host: '192.168.1.126',
    topic: 'test',
    port: 1883
}

const clientId = `mqtt_${Math.random().toString(16).slice(3)}`

const connectUrl = `mqtt://${mqttConfig.host}:${mqttConfig.port}`

const client = connect(connectUrl)

// const client = mqtt.connect(connectUrl, {
//     clientId,
//     clean: true,
//     connectTimeout: 4000,
//     reconnectPeriod: 1000
// })

client.on('connect', () => {
    console.log('Connected')

    function send() {
        client.publish(mqttConfig.topic, getArray(), { qos: 0, retain: false }, error => {
            if (error) {
                console.error(error)
            }
        })
    }

    const intervalId = setInterval(send, 500)
})

// const service = new MqttGateway(mqttConfig)
// const dataArray: number[] = [...Array(512).keys()]
// service.send(dataArray)

////////////////////////////////////////////////////////////////

app.get('/', (req, res) => {
    res.send('Hello World!')
})

app.get('/x', (req, res) => {
    throw new Error('This is an example exception.')
})

app.listen(PORT, () => {
    console.log('Server listening on port ${PORT}')
})
