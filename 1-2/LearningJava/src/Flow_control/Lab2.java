package Flow_control;

import java.util.Scanner;

public class Lab2 {
    public static void main(String [] args){
        // 1부터 7까지의 정수를 입력받아 해당 숫자에 맞는 요일을 출력하는 프로그램을
        // switch문 이용해 작성
        // 단, 잘못된 숫자를 입력할 경우
        // "유효하지 않은 숫자입니다. 1~7 사이의 숫자를 입력하세요."
        // 라는 메시지를 출력하고, 올바른 값을 입력할 때까지 재입력을 받는다
        // 토요일(6)과 일요일(7)은 “주말”로, 그 외 요일은 “주중”으로 구분하여 출력

        // 1~7 사이의 정수를 입력을 받는다
        Scanner sc = new Scanner(System.in);
        int input = 0;

        while (true) {
            System.out.println("숫자를 입력하세요: ");
            // 잘못된 숫자를 입력할 경우 재입력을 받는다
            input = sc.nextInt();

            if (input > 1 && input < 7){
                break;
            }
            System.out.println("유효하지 않은 숫자입니다. 1~7 사이의 숫자를 입력하세요.");
        }

        // 해당 숫자에 맞는 요일을 출력
        String msg = "";
        switch (input){
            // 1:월 2:화 3:수 4:목 5:금 -> 주중
            case 1:
                msg ="월요일, 주중";
                break;
            case 2:
                msg = "화요일, 주중";
                break;
            case 3:
                msg = "수요일, 주중";
                break;
            case 4:
                msg = "목요일, 주중";
                break;
            case 5:
                msg = "금요일, 주중";
                break;
            // 6:토요일 7:일요일 -> 주말
            case 6:
                msg = "토요일, 주말";
                break;
            case 7:
                msg = "일요일, 주말";
                break;
        }

        //결과를 출력
        System.out.println(msg);
    }
}
