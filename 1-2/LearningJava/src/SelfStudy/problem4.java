package SelfStudy;

import java.util.Scanner;

public class problem4 {
    public static void main(String [] args){
        // 3つの科⽬のスコアの入力を受けて平均スコアを計算し、平均に基づいて単位評価を付与するプログラム

        // task1
        // 数学、科学、英語のスコアの入力を受ける
        Scanner sc = new Scanner(System.in);
        System.out.println("数学の点数を入力してください");
        int math = sc.nextInt();
        System.out.println("英語の点数を入力してください");
        int english = sc.nextInt();
        System.out.println("科学の点数を入力してください");
        int science = sc.nextInt();

        // 平均スコアを計算。
        float avr = (float) (math + english + science) / 3;

        // 平均スコアに応じて単位評価
        char score = '\u0000';
        // A: 90점 이상
        if (avr >= 90 ){
            score = 'A';

        }// B: 80점 이상 90점 미만
        else if (80 <= avr && 90 > avr) {
            score = 'B';
        }// C: 70점 이상 80점 미만
        else if (70 <= avr && 80 > avr) {
            score = 'C';
        }// D: 60점 이상 70점 미만
        else if (60 <= avr && 70 > avr) {
            score = 'D';
        }// F: 60점 미만
        else {
            score = 'F';
        }                               //
        System.out.printf("平均点数は%.2f点で、単位は%cです", avr,score );
    }
}
