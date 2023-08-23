import { DeviceScene } from './DeviceScene'

type Scene = {
    name: string
    devices: { [key: number]: DeviceScene }[]
}

// TODO: verify that the device addresses are not colliding

export { Scene }
