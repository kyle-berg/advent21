package day1;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class p1 {

    public static int depthCount() {

        Scanner scan = null;
        int currentDepth = 0;
        int lastDepth = 0;
        int increases = 0;
        File file = new File("data");

        try {
            scan = new Scanner(file);
            while (scan.hasNextInt()) {
                lastDepth = currentDepth;
                currentDepth = scan.nextInt();
                if (currentDepth > lastDepth) {
                    increases++;
                }
            }

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        return increases;
    }

    public static void main(String[] args) {
        System.out.println(depthCount());
    }
}
