import { Device } from '../Device'

const LedParLight: Device = {
    name: 'LED Par Light',
    model: 'LPC007R',
    channels: [
        {
            type: 'plain',
            name: 'General dimming',
            channelPosition: 1,
            defaultValue: 0
        },
        {
            type: 'plain',
            name: 'Red dimming',
            channelPosition: 2,
            defaultValue: 0
        },
        {
            type: 'plain',
            name: 'Green dimming',
            channelPosition: 3,
            defaultValue: 0
        },
        {
            type: 'plain',
            name: 'Blue dimming',
            channelPosition: 4,
            defaultValue: 0
        },
        {
            type: 'plain',
            name: 'Strobe speed',
            channelPosition: 5,
            defaultValue: 0
        },
        {
            type: 'enum',
            name: 'Mode',
            channelPosition: 6,
            choices: {
                Dimming: 25,
                'Color output': 75,
                'Jump change': 125,
                Transform: 175,
                'Pulse Transform': 225,
                'Sound Activated': 252
            },
            defaultValue: 25
        },
        {
            type: 'enum',
            name: 'Sound Activated Mode',
            channelPosition: 7,
            choices: {
                Red: 15,
                Green: 45,
                Blue: 75,
                WarmWhite: 110,
                Yellow: 140,
                Violet: 170,
                Cyan: 200,
                White: 230,
                ChangeColor: 252
            },
            defaultValue: 0
        }
    ]
}

const MovingHeadBeam: Device = {
    name: 'Moving Head Beam',
    model: 'TL360ZW',
    channels: [
        {
            type: 'plain',
            name: 'General dimming',
            channelPosition: 1,
            defaultValue: 0
        },
        {
            type: 'plain',
            name: 'Red dimming',
            channelPosition: 2,
            defaultValue: 0
        },
        {
            type: 'plain',
            name: 'Green dimming',
            channelPosition: 3,
            defaultValue: 0
        },
        {
            type: 'plain',
            name: 'Blue dimming',
            channelPosition: 4,
            defaultValue: 0
        },
        {
            type: 'plain',
            name: 'Strobe speed',
            channelPosition: 5,
            defaultValue: 0
        },
        {
            type: 'plain',
            name: 'Boh6',
            channelPosition: 6,
            defaultValue: 0
        },
        {
            type: 'plain',
            name: 'Boh7',
            channelPosition: 7,
            defaultValue: 0
        },
        {
            type: 'plain',
            name: 'Boh8',
            channelPosition: 8,
            defaultValue: 0
        },
        {
            type: 'plain',
            name: 'Beam angle',
            channelPosition: 9,
            defaultValue: 0
        },
        {
            type: 'plain',
            name: 'Pan/Horizontal',
            channelPosition: 10,
            defaultValue: 0
        },
        {
            type: 'plain',
            name: 'Tilt/Vertical',
            channelPosition: 11,
            defaultValue: 0
        }
    ]
}

const MovingHeadBeamMovement: Device = {
    name: 'Moving Head Beam Movement-only',
    model: 'TL360ZW',
    channels: [
        {
            type: 'plain',
            name: 'Beam angle',
            channelPosition: 9,
            defaultValue: 0
        },
        {
            type: 'plain',
            name: 'Pan/Horizontal',
            channelPosition: 10,
            defaultValue: 0
        },
        {
            type: 'plain',
            name: 'Tilt/Vertical',
            channelPosition: 11,
            defaultValue: 0
        }
    ]
}

const MovingHeadBeamLight: Device = {
    name: 'Moving Head Beam Lights-only',
    model: 'TL360ZW',
    channels: [
        {
            type: 'plain',
            name: 'General dimming',
            channelPosition: 1,
            defaultValue: 0
        },
        {
            type: 'plain',
            name: 'Red dimming',
            channelPosition: 2,
            defaultValue: 0
        },
        {
            type: 'plain',
            name: 'Green dimming',
            channelPosition: 3,
            defaultValue: 0
        },
        {
            type: 'plain',
            name: 'Blue dimming',
            channelPosition: 4,
            defaultValue: 0
        },
        {
            type: 'plain',
            name: 'Strobe speed',
            channelPosition: 5,
            defaultValue: 0
        }
    ]
}

const Strobe: Device = {
    name: 'strobe',
    model: 'Saetta',
    channels: [
        {
            type: 'plain',
            name: 'Frequency',
            channelPosition: 1,
            defaultValue: 0
        },
        {
            type: 'plain',
            name: 'Dimming',
            channelPosition: 2,
            defaultValue: 0
        }
    ]
}

export { LedParLight, MovingHeadBeam, Strobe }
