public class Main {
    public static void main(String[] args) {
        int[] vector = {1, 3, 2, 1};
        int[] teste = new int[10];
        teste = MaxMin4.maxMin4(vector, 0, 3);
        System.out.println("Max: " + teste[0]);
        System.out.println("Min: " + teste[1]);
    }
}
