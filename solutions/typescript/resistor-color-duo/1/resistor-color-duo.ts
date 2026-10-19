export function decodedValue(input: Array<string>): Number {
  const colors = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white'];
  let count = 0;
  for (let i = 0; i < 2; i++) {
    count += colors.indexOf(input[i]);
    if (i == 0) {
        count *= 10;
    }
  }
  return count;
}