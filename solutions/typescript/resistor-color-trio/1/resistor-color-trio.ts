export function decodedResistorValue(colors: Array<string>) : String {
  const color_list = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"];
  let count = 0;
  let unit = "ohms";
  for (let i = 0; i<3; i++) {
    if (i == 0) {
        count += color_list.indexOf(colors[i]) * 10;
    } else if (i == 1) {
        count += color_list.indexOf(colors[i]);
    } else {
        let exp = color_list.indexOf(colors[i]);
        count = count * Math.pow(10, exp);
        if (count >= 1000000000) {
            count /= 1000000000;
            unit = "gigaohms";
        } else if (count >= 1000000) {
            count /= 1000000;
            unit = "megaohms";
        } else if (count >= 1000) {
            count /= 1000;
            unit = "kiloohms"
        }
    }
  }
  let result = count.toString() + " " + unit;
  return result;
}