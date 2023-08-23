import { Scene } from '../Scene'
import * as Pred from './PredefinedDeviceScenes'

const Disco2and2: Scene = {
    name: 'Disco2and2',
    devices: [
        {
            1: Pred.ParChangeStrobeMusicEffectEvery2Seconds
        },
        {
            17: Pred.ParChangeColorMusicEffectEvery2Seconds
        }
    ]
}

const AlwaysWhiteScene: Scene = {
    name: 'AlwaysWhite',
    devices: [
        {
            1: Pred.ParAlwaysWhite
        },
        {
            17: Pred.ParAlwaysWhite
        },
        {
            33: Pred.HeadAlwaysWhite
        }
    ]
}

export { Disco2and2, AlwaysWhiteScene }
