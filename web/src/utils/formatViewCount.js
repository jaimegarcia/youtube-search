
/** Format View Count Value to have comma in thousands
 * @param  {Number} x View Count
 */
const formatViewCount = (x) => {
  return parseInt(x).toLocaleString('en');

};

export default formatViewCount;