public class JedliksToyCar {
    private int battery = 100;
    private int meters;
    
    public static JedliksToyCar buy() {
        JedliksToyCar newCar = new JedliksToyCar();
        return newCar;
    }

    public String distanceDisplay() {
        String display = "Driven " + Integer.toString(this.meters) + " meters";
        return display;
    }

    public String batteryDisplay() {
        String display = "Battery ";
        if (this.battery > 0) {
            display = display + "at " + Integer.toString(this.battery) + "%";
        } else {
            display = display + "empty";
        }
        return display;
    }

    public void drive() {
        if (this.battery > 0) {
            this.meters = this.meters + 20;
            this.battery = this.battery - 1;
        }
    }
}
