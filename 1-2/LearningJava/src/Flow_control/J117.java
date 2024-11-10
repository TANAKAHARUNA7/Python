package Flow_control;

import java.util.Random;

public class J117 {
    public static void main(String [] args){
        Random random1 = new Random(1255);
        Random random2 = new Random(1255);
        // シード値がないため実行時現在時間を

        System.out.println("random1: " + random1.nextInt());
        System.out.println("random2: " + random2.nextInt());
        System.out.println("--------------------");

        //////////////////////////////////////////////////////

        for(int i = 0 ; i < 5 ; i++ ){
        Random random3 = new Random();
        System.out.println("random3: " + random3.nextInt());

        }
    }
}
