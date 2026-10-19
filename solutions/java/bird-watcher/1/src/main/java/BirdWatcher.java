
class BirdWatcher {
    private final int[] birdsPerDay;

    private final int[] lastWeek = new int[] { 0, 2, 5, 3, 7, 8, 4 };

    public BirdWatcher(int[] birdsPerDay) {
        this.birdsPerDay = birdsPerDay.clone();
    }

    public int[] getLastWeek() {
        return lastWeek;
    }

    public int getToday() {
        int length = birdsPerDay.length;
        return birdsPerDay[length - 1];
    }

    public void incrementTodaysCount() {
        int length = birdsPerDay.length;
        birdsPerDay[length - 1]++;
    }

    public boolean hasDayWithoutBirds() {
        for (int birds: birdsPerDay) {
            if (birds == 0) {
                return true;
            }
        }
        return false;
    }

    public int getCountForFirstDays(int numberOfDays) {
        if (numberOfDays > birdsPerDay.length) {
            numberOfDays = birdsPerDay.length;
        }
        int count = 0;
        for (int i = 0; i < numberOfDays; i++) {
            count = count + birdsPerDay[i];
        }
        return count;
    }

    public int getBusyDays() {
        int busyDays = 0;
        for (int day: birdsPerDay) {
            if (day >= 5) {
                busyDays++;
            }
        }
        return busyDays;
    }
}
