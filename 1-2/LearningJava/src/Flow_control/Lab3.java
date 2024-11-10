package Flow_control;

import java.util.Scanner;

public class Lab3 {
    public static void main(String []args) {
        // 학생의 성적 등급과 출석 등급을 입력받아 장학금 지급 여부와 권장 사항 판별하는 프로그램을 작성
        // switch expression과 yield를 사용하여 구현한다

        // 성적 등급과 출석 등급에 따라 다음과 같은 규칙으로 장학금 지급 여부와 권장 사항을 결정한다
        //– 성적:A 출석:Excellent -> ＂전액 장학금 및 추가 지원금 지급 “
        //– 성적:A 출석:Average인 -> ＂전액 장학금“
        //– 성적:B 출석:Excellent -> "반액 장학금“

        // 성적 등급이 C, D인 경우
        // 출석:Poor -> "장학금 없음, 재수강 권장“
        // 출석:Excellent 또는 Average -> "장학금 없음“
        //– 성적:F -> "장학금 없음, 재수강 권장“
        //– 이외 ->  “장학금 없음”으로 출력

        // 잘못된 성적 등급 또는 출석 등급이 입력된 경우 ->  "잘못된 입력입니다“
        // 성적 등급은 A, B, C, D, F 중 하나로 입력받고, 출석 등급은 Excellent, Average, Poor 중 하나로 입력받는다
        // 키보드로부터 입력받은 영문자는 모두 대문자로 변환하여 처리한다 (예: poor → POOR). 직접 구현 할 것
        // 재입력 기능을 구현하여 잘못된 입력이 있을 경우 다시 입력받도록 한다

        ///////////////////////////////////////////////////////////////////////////////

        Scanner sc = new Scanner(System.in);
        // 성적 값 초기화
        char Grades = '\u0000';

        // 출석 값 초기화
        String attendance = "";

        while (true) {
            // 성적을 입력받는다 (A, B, C, D, F)
            System.out.println("성적 등급을 입력하세요 (A, B, C, D, F): ");
            Grades = sc.next().charAt(0);

            // 출석을 입력받는다 (Excellent, Average, Poor)
            System.out.println("출석 등급을 입력하세요 (Excellent, Average, Poor): ");
            sc.nextLine();
            attendance = sc.nextLine();

            // 잘못된 입력이 있을 경우 다시 입력받도록 한다




            //  영문자는 모두 대문자로 변환하여 처리

            // 결과 출력


        }
    }
}