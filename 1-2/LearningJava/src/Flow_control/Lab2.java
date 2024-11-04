//package Flow_control;
//
//public class Lab2 {
//    public static void main (String [] args){
//        // 1부터 7까지의 정수를 입력받아 해당 숫자에 맞는 요일을 출력하는 프로그램을
//        // switch문 이용해 작성
//
//        // 단, 잘못된 숫자를 입력할 경우
//        // "유효하지 않은 숫자입니다. 1~7 사이의 숫자를 입력하세요."
//        // 라는 메시지를 출력하고, 올바른 값을 입력할 때까지 재입력을 받는다
//        // 토요일(6)과 일요일(7)은 “주말”로, 그 외 요일은 “주중”으로 구분하여 출력
//
//        // task1
//        // 유자로부터 1부터 7까지의 정수를 입력받는다
//        int num = 0;
//        // 잘못된 숫자를 입력할 경우 재입력를 받는다
//        while (true) {
//            System.out.println("1~7 사이의 숫자를 입력하세요: ");
//            num = 8;
//
//            if (num < 8) {
//                break;
//            }else{
//                System.out.println("유로하지 않은 숫자입니다. 1~7 사이의 숫자를 입력하세요.");
//            }
//
// //       }

        // switch문으로 알고리즘을 작성
//        String msg = "";
//        String dayOfWeek = switch (num) {
            // 1;월요일 2:화요일 3:수요일 4:목요일 5:금요일 -> "주중"
//           case 1, 2, 3, 4, 5 -> {
//                if (num == 1) {
//                    yield "월요일, 주말";
//                } else if (num == 2) {
//                    yield "화요일, 주말";
//                } else if (num == 3) {
//                    yield "수요일, 주말";
//                } else if (num == 4) {
//                    yield "목요일, 주말";
 //               } else {
//                    yield "금요일, 주말";
//                }
//            }
            // 6:토요일 7:일요일 -> 주말
//            case 6,7 -> {
//if (num == 6){
//                    yield "토요일, 주말";
 //               }else{
 //                   yield "일요일, 주말";
 //               }
  //          }

  //      };
 //       System.out.println(dayOfWeek);

  //  }
//}
//