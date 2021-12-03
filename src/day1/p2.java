package day1;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class p2 {

    public static void main(String[] args) throws FileNotFoundException {
        int window1 = 0;
        int window2 = 0;
        int increases = 0;

        File file = new File("data");
        Scanner scan = new Scanner(file);

        ArrayList<Integer> depths = new ArrayList<Integer>();
        while (scan.hasNextInt()) {
            depths.add(scan.nextInt());
        }

        for (int i = 3; i < depths.size(); i++) {
            window1 = depths.get(i - 1) + depths.get(i - 2) + depths.get(i - 3);
            window2 = depths.get(i) + depths.get(i - 1) + depths.get(i - 2);

            if (window2 > window1) {
                increases++;
            }
        }
        System.out.println(increases);
    }
}

