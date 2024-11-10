package SelfStudy;

import java.util.Scanner;

public class problem5 {
    public static void main(String [] args){
        // 仮想株取引プラットフォームのためのシミュレータを作成
        // 初期資本⾦で株式を購⼊し、以後、株式価格が変動した後に
        // 株式を販売することによって得られる利益または発⽣する損失を計算する

        // task1
        // 初期資本⾦,株式の購⼊価格,購⼊する株式の数,販売時の株価の入力を受ける
        Scanner sc = new Scanner(System.in);
        // 初期資本⾦
        System.out.println("初期資本⾦");
        int money = sc.nextInt();
        // 株式の購⼊価格
        System.out.println("株式の購⼊価格");
        int price = sc.nextInt();
        // 株数
        System.out.println("株数");
        int value = sc.nextInt();
        // 販売時の株価
        System.out.println("販売時の株価");
        int buyMoney = sc.nextInt();

        // 株総購⼊費⽤　＝　購⼊価格　x　株数
        float totalBuy = price * value;

        // 残りの資本⾦　＝　初期資本⾦　－　総購⼊費⽤
        float restMoney = money - totalBuy;

        // 売上予想利益　＝　（　販売時の株価　X　株数　）―　総購⼊費⽤
        float sell = (buyMoney * value) - totalBuy;

        // 株式購⼊後に残った資本⾦と株式販売時の予想利益または損失を出力
        System.out.printf("購入後残った資本金は%.2f\n",restMoney);
        System.out.printf("予想利益は%.2f\n",sell);

        // 利益発⽣ -> 「予想される利益です」を、
        // 損失 -> 「予想される損失です」を出力
        String msg = "";
        if (sell > 0){
            msg = "利益";
        }else {
            msg = "損失";
        }
        System.out.println("予想される" + msg + "です。");

    }
}
