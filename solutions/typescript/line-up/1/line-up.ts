export function format(name: string, number: number): string {
  let card = ""
  switch (number % 10) {
    case 1:
        card = number % 100 === 11 ? "th" : "st"
        break;
    case 2:
        card = number % 100 === 12 ? "th" : "nd"
        break;
    case 3:
        card = number % 100 === 13 ? "th" : "rd"
        break;
    default:
        card = "th"
        break;
  }
  return `${name}, you are the ${number}${card} customer we serve today. Thank you!`
}