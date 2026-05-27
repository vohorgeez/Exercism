public class Lasagna {
    public static int expectedMinutesInOven() {
        return 40;
    }

    public int remainingMinutesInOven(int cooking_minutes) {
        return expectedMinutesInOven() - cooking_minutes;
    }

    public int preparationTimeInMinutes(int layers) {
        return layers*2;
    }

    public int totalTimeInMinutes(int layers, int cooking_minutes) {
        return preparationTimeInMinutes(layers) + cooking_minutes;
    }
}
