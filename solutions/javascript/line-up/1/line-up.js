//
// This is only a SKELETON file for the 'Line Up' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const format = (name, number) => {
    const exceptions = [11, 12, 13];
    let suff = null
    if (exceptions.includes(number % 100)) {
        suff = 'th';
    } else {
        switch (number % 10) {
            case 1:
                suff = 'st';
                break;
            case 2:
                suff = 'nd';
                break;
            case 3:
                suff = 'rd';
                break;
            default:
                suff = 'th';
        };
    };

    return `${name}, you are the ${number}${suff} customer we serve today. Thank you!`
};