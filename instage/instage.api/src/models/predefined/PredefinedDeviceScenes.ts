import { LedParLight, MovingHeadBeam } from './PredefinedDevices'
import { DeviceScene } from '../DeviceScene'

const ParChangeColorsEverySecond: DeviceScene = {
    profile: LedParLight,
    timer: 1000,
    values: [
        { 1: 255, 2: 255 },
        { 1: 255, 3: 255 },
        { 1: 255, 4: 255 }
    ]
}

const ParChangeStrobeMusicEffectEvery2Seconds: DeviceScene = {
    profile: LedParLight,
    timer: 2000,
    values: [
        { 6: 252, 7: 15 },
        { 6: 252, 7: 45 },
        { 6: 252, 7: 75 },
        { 6: 252, 7: 110 },
        { 6: 252, 7: 140 },
        { 6: 252, 7: 170 },
        { 6: 252, 7: 200 },
        { 6: 252, 7: 230 }
    ]
}

const ParChangeColorMusicEffectEvery2Seconds = {
    profile: LedParLight,
    timer: 2000,
    values: [{ 6: 252, 7: 252 }]
}

const ParAlwaysWhite: DeviceScene = {
    profile: LedParLight,
    timer: 0,
    values: [{ 1: 255, 2: 255, 3: 255, 4: 255 }]
}

const HeadAlwaysWhite: DeviceScene = {
    profile: MovingHeadBeam,
    timer: 0,
    values: [{ 1: 255, 2: 255, 3: 255, 4: 255 }]
}

export { ParChangeColorsEverySecond, ParChangeStrobeMusicEffectEvery2Seconds, ParChangeColorMusicEffectEvery2Seconds, ParAlwaysWhite, HeadAlwaysWhite }
