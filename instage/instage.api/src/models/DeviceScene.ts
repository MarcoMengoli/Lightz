import { Device } from './Device'

type DeviceScene = {
    profile: Device
    timer: number
    values: { [key: number]: number }[]
}

export { DeviceScene }
