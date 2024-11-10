package special_class;

import java.util.Scanner;

public class test5 {
    public static void main(String[] args) {
        // 가위, 바위, 보 게임 만들기
        // 사용자로부터 Scissors, Rock, Paper 중 하나 입력
        //  - 예시 : Scissors, Rock, Paper 중 하나를 입력 하세요:
        // 컴퓨터가 난수를 이용해, 가위-바위-보 중 하나 선택
        // 결과 출력
        //  - 예 1) 승리 : 사용자 - 가위, 컴퓨터-보
        //  - 예 2) 패배 : 사용자 - 가위, 컴퓨터-바위
        //  - 예 3) 무승부 : 사용자 - 가위, 컴퓨터 가위
        // 그리고 게임 재실행

        // 사용자로부터 Scissors, Rock, Paper 입력 예외 처리
        //  - Scissors, Rock, Paper 이외의 값이 입력 될 경우
        //    "잘못된 입력 값 입니다, Scissors, Rock, Paper 중 하나를 입력 하세요"
        //    출력 후 재입력
        // "quit"를 입력하면 프로그램 종료
        // 3. 승리 시 보너스 포인트 1점 증가, 패배 시 보너스 포인트 1점 차감
        //    연속으로 승리 시 보너스 포인트 3점 추가
        // 4. 결과값 판별 후 현재 포인트 출력
        //    예) 현재포인트 : 1점
        // 5. 게임 종료 조건 추가
        //    사용자 포인트가 7점 이상 또는 -7점 이하이면 종료
        //     7점 이상이면 : "축하합니다. 승리~~~"
        //     -7점 이하이면 : "다음 기회에~~~"

        ///////////////////////////////////////////////////////////////

        // task1
        // 사용자로부터 Scissors, Rock, Paper 중 하나 입력을 받는다
        Scanner sc = new Scanner(System.in);
        String inputList [] = {"Scissors", "Rock", "Paper"};
        String input = "";

        // 포인트
        int point = 0;

        //　보너스 포인트
        int bornus = 0;

        while (true) {
            System.out.println("Scissors, Rock, Paper 중 하나 입력하세요.");
            input = sc.nextLine();
            // 입력을 받는 문자형을 숫자형에 변환
            int num = switch (input) {
                case "Sc" -> 0;
                case "Ro" -> 1;
                case "Pa" -> 2;
                case "quit" -> 3;
                default -> 4;
            };

            // "quit"를 입력하면 프로그램 종료
            if (num == 3) {
                System.out.println("프로그램 종료");
                break;
            }

            else if (num == 4) {
                System.out.println("잘못 입력입니다");
                continue;
            }

            //　컴퓨터 가위-바위-보 리스트를 생성
            String com [] = {"Scissors", "Rock", "Paper"};
            // 난수를 생성
            int comrandom = (int) (Math.random() * 3);

            // 반단 코드
            String msg = "";
            if (num == comrandom){
                msg = "무승부";

                // bornus 초기화
                bornus = 0;

            }else if(num == 0 && comrandom == 1 || num == 1 && comrandom == 2
                    || num == 2 && comrandom == 0){
                msg = "패배";
                // 패배 시 포인트 1점 차감
                point --;

                // bornus 초기화
                bornus = 0;

            }else{
                msg = "승리";
                // 승리 시 포인트 1점 증가
                point ++;

                // bornus + 2
                bornus ++;
            }


            // 결과 출력
            System.out.println(msg + ": 사용자 - "+ inputList[num] + ", 컴퓨터 - " + com[comrandom]);
            String msg2 = "";
            if (bornus > 1){
                point += 2;
                System.out.println("포인트 3점추가 ^^ 🌟");
            }
            System.out.println("현재포인트 : " + point + "점");



            // 사용자 포인트가 7점 이상 또는 -7점 이하이면 종료
            //     7점 이상이면 : "축하합니다. 승리~~~"
            if (point >= 7){
                System.out.println("축하합니다. 승리~~~");
                break;
            }
            //     -7점 이하이면 : "다음 기회에~~~"
            if (point <= -7){
                System.out.println("다음 기회에~~~");
            }
        }
    }
}

