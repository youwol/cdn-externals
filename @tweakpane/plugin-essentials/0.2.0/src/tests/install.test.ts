import { install } from '@youwol/cdn-client'
import './mock-requests'
import { cleanDocument, installPackages, setupPyYouwolBackend } from './common'
// The following import does not work in jest:
//  export { ButtonCellApi, ButtonGridApi, ButtonGridController, CubicBezier, CubicBezierApi, CubicBezierAssembly, CubicBezierController, CubicBezierGraphController, CubicBezierGraphView, CubicBezierPickerController, CubicBezierPickerView, CubicBezierPreviewView, CubicBezierView, FpsGraphBladeApi, FpsGraphController, FpsView, Fpswatch, Interval, IntervalAssembly, IntervalConstraint, RadioCellApi, RadioController, RadioGridApi, RadioGridController, RadioView, RangeSliderController, RangeSliderTextController, RangeSliderTextView, RangeSliderView, TpRadioGridChangeEvent, css, id, plugins };
//  ^^^^^^
// all these case are asserted in the test below
// import * as originalPackage from '@tweakpane/plugin-essentials'

beforeAll(async () => {
    // If the package does requires dependencies from webPM, turn off the option 'localOnly'
    setupPyYouwolBackend({ port: 2001, localOnly: false })
    // Be sure to have run the 'cdn-local' step of the pipeline through dev-portal before running the test.
    // It generates the 'cdn.zip' files used below
    await installPackages(['../../cdn.zip'])
})

beforeEach(() => {
    cleanDocument()
    // need @youwol/cdn-client#2.1.1 to be enabled
    // State.clear()
})

test('install @tweakpane/plugin-essentials', async () => {
    const notExported: string[] = [
        // Provide the name of the symbols that are not exported for a good reason + give the reason
    ]
    const { tweakpane, plugins } = (await install({
        modules: ['@tweakpane/plugin-essentials#0.2.0'],
        aliases: {
            plugins: '@tweakpane/plugin-essentials',
            tweakpane: 'tweakpane',
        },
    })) as unknown as { tweakpane; plugins }
    // 2 scripts: tweakpane & @tweakpane/plugin-essentials
    expect(document.scripts).toHaveLength(2)
    const webpmPackage = globalThis['@tweakpane/plugin-essentials_APIv02']
    expect(webpmPackage).toBeTruthy()
    const originalProperties =
        'ButtonCellApi, ButtonGridApi, ButtonGridController, CubicBezier, CubicBezierApi, CubicBezierAssembly, CubicBezierController, CubicBezierGraphController, CubicBezierGraphView, CubicBezierPickerController, CubicBezierPickerView, CubicBezierPreviewView, CubicBezierView, FpsGraphBladeApi, FpsGraphController, FpsView, Fpswatch, Interval, IntervalAssembly, IntervalConstraint, RadioCellApi, RadioController, RadioGridApi, RadioGridController, RadioView, RangeSliderController, RangeSliderTextController, RangeSliderTextView, RangeSliderView, TpRadioGridChangeEvent, css, id, plugins'.split(
            ', ',
        )
    const notFound = originalProperties.filter((p) => !webpmPackage[p])
    if (notFound.length > 0) {
        console.warn(
            `${notFound.length} properties out of ${originalProperties.length} of lodash are not found:`,
            notFound,
        )
    }
    const missing = notFound.filter((p) => !notExported.includes(p))
    if (missing.length > 0) {
        console.error(
            `${missing.length} properties out of ${originalProperties.length} of lodash are not found but required`,
            missing,
        )
    }
    expect(missing).toHaveLength(0)
    const pane = new tweakpane.Pane()
    pane.registerPlugin(plugins)
})
