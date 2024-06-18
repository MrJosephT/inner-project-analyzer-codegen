public class Box {
    private int width;
    private int height;
    public Box(int width, int height) {
        this.width = width;
        this.height = height;
    }
    public Box[] divideBox() {
        int newWidth = this.width / 2;
        Box box1 = new Box(newWidth, this.height);
        Box box2 = new Box(newWidth, this.height);
        Box[] dividedBoxes = {box1, box2};
        return dividedBoxes;
    }
}