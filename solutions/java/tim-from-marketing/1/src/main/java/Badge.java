class Badge {
    public String print(Integer id, String name, String department) {
        String label = "";
        if (id != null) {
            label = "[" + Integer.toString(id) + "] - ";
        }
        label = label + name + " - ";
        if (department != null) {
            label = label + department.toUpperCase();
        } else {
            label = label + "OWNER";
        }
        return label;
    }
}
