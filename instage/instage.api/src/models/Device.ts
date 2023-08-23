type Device = {
    name: string
    model: string
    channels: Channel[]
}

type PlainChannel = {
    type: 'plain'
    name: string
    channelPosition: number
    defaultValue: number
}

type EnumChannel = {
    type: 'enum'
    name: string
    channelPosition: number
    choices: { [key: string]: number }
    defaultValue: number
}

type Channel = PlainChannel | EnumChannel

export { Device, Channel, PlainChannel, EnumChannel }
