package day2;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class p1 {
    public static void main(String[] args) throws FileNotFoundException {
        int horiz = 0;
        int depth = 0;
        File file = new File("data");
        Scanner scan = new Scanner(file);

        while (scan.hasNext()) {
            String str = scan.nextLine();
            String[] command = str.split(" ");
            if (command[0].equals("forward")) {
                horiz += Integer.parseInt(command[1]);
            }
            else if (command[0].equals("down")) {
                depth += Integer.parseInt(command[1]);
            }
            else {
                depth -= Integer.parseInt(command[1]);
            }
        }
        System.out.println("Horizontal: " + horiz);
        System.out.println("Depth: " + depth);
        System.out.println(horiz*depth);
    }
}
