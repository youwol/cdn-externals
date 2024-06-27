/**
 * The lines below are actually not exporting anything...
 */
import DefaultImport from 'mathjax/es5/tex-mml-chtml'
export { setup as webpmSetup } from './auto-generated'
export * from 'mathjax/es5/tex-mml-chtml'
export default DefaultImport

/**
 * However, they define the global MathJax symbol, re-exported here :/ .
 *
 */
export const texMmlChtml = window['MathJax']
