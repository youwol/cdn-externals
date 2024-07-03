import { Config } from 'jest'

const jestConfig: Config = {
    preset: '@youwol/jest-preset',
    // modulePathIgnorePatterns: [],
    transform: {
        '^.+\\.js$': 'jest-esm-transformer',
    },
}
export default jestConfig
