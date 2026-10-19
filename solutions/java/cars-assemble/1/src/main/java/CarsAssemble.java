public class CarsAssemble {

    public double productionRatePerHour(int speed) {
        int production = speed * 221;
        if (speed == 0) {
            return 0;
        } else if (speed >= 1 && speed <= 4) {
            return production;
        } else if (speed >= 5 && speed <= 8) {
            return production * 0.9;
        } else if (speed == 9) {
            return production * 0.8;
        } else if (speed == 10) {
            return production * 0.77;
        } else {
            return 0;
        }
    }

    public int workingItemsPerMinute(int speed) {
        double perHour = productionRatePerHour(speed);
        int perMinute = (int) perHour / 60;
        return perMinute;
    }
}
