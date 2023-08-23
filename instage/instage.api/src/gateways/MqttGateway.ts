import mqtt, { Client } from 'mqtt'

interface MqttConfig {
    host: string
    topic: string
    port?: number
}

class MqttGateway {
    private client: Client

    constructor(private config: MqttConfig) {
        this.client = mqtt.connect({
            host: config.host,
            port: config.port || 1883 // default MQTT port
        })

        this.client.on('connect', () => {
            console.log('Connected to MQTT broker')
        })
    }

    public send(data: number[]): void {
        // if (data.length !== 512) {
        //     console.error('Invalid data length. Expected 512 values.')
        //     return
        // }

        // Convert the array into a dictionary
        const dictionary = data.reduce<Record<number, number>>((acc, value, index) => {
            acc[index] = Math.max(0, Math.min(255, value))
            return acc
        }, {})

        const jsonData = JSON.stringify(dictionary)
        this.client.publish(this.config.topic, jsonData, {}, err => {
            if (err) {
                console.error('Failed to send MQTT message:', err)
            }
        })
    }
}

export { MqttConfig, MqttGateway }
