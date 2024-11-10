package SelfStudy;

import java.util.Scanner;

public class probrem1 {
    public static void main(String [] args){
        // 도서관에서는 나이에 따라 다양한 이용권을 제공함.
        // 사용자의 나이를 입력받아, 해당 사용자에게 적합한 도서관 이용권을 판별하는 프로그램을 작성.
        // – 어린이 이용권: 12세 이하
        // – 청소년 이용권: 13세 ~ 18세
        // – 성인 이용권: 19세 이상

        // task1
        // – 사용자의 나이를 입력받는다.
        Scanner sc = new Scanner(System.in);

        System.out.println("나이를 입력하세요: ");
        int age = sc.nextInt();

        // – 입력받은 나이에 따라 적합한 도서관 이용권을 판별
        String msg = "";

        // – 어린이 이용권: 12세 이하
        if (age <= 12){
            msg = "어린이 이용권";
        // – 청소년 이용권: 13세 ~ 18세
        } else if (age <= 18) {
            msg = "청소년 이용권";
        }else{
            msg = "성인 이용권";
        }

        // 결과를 출력하세요.
        System.out.println(msg);




    }
}
