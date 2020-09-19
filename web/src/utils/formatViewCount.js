
/** Format View Count Value to have comma in thousands
 * @param  {Number} x View Count
 */
const formatViewCount = (x) => {
  return x.toString().replace(/\B(?<!\.\d*)(?=(\d{3})+(?!\d))/g, ",");

};

export default formatViewCount;