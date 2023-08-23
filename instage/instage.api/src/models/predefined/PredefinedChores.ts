import { Chore } from '../Chore'
import * as Pred from './PredefinedScenes'

const ChoreDisco: Chore = {
    name: 'choreDisco',
    scenes: [Pred.Disco2and2],
    timer: 300
}

const ChoreAlwaysWhite: Chore = {
    name: 'choreDisco',
    scenes: [Pred.Disco2and2],
    timer: 0
}

export { ChoreDisco }
