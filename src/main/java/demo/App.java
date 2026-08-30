package demo;

public class App {
    public static String greet(String who) {
        return "hello " + who;
    }
    public static void main(String[] args) {
        System.out.println(greet(args.length > 0 ? args[0] : "world"));
    }
}
