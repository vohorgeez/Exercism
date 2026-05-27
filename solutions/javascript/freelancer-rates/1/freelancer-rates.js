export function dayRate(ratePerHour) {
  return 8*ratePerHour;
}

export function daysInBudget(budget, ratePerHour) {
  return Math.floor(budget / dayRate(ratePerHour));
}

export function priceWithMonthlyDiscount(ratePerHour, numDays, discount) {
  let monthCost = dayRate(ratePerHour) * 22;
  let discountedMonthCost = monthCost * (1 - discount);
  let fullMonths = Math.floor(numDays / 22);
  let remainingDays = numDays % 22;
  let total = (fullMonths*discountedMonthCost) + (remainingDays*dayRate(ratePerHour))
  return Math.ceil(total);
}
