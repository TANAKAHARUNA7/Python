package SelfStudy;

import java.util.Scanner;

public class problem2 {
    public  static void main(String [] args){
        // 사용자가 입력한 세 개의 수를 변의 길이로 하는 삼각형이 형성될수 있는지,
        // 그리고 가능하다면 어떤 유형의 삼각형인지 판별한다.

        // 세 변의 길이가 모두 같다 -> '정삼각형
        // 세 변 중 두 변의 길이가 같다 -> '이등변삼각형'
        // 세 변의 길이가 모두 다르다 -> '부등변삼각형'
        // 어느 두 변의 길이 합이 나머지 한 변의 길이보다 작거나 같다 -> "삼각형을 형성할수없다".

        // task1
        // – 사용자로부터 세 변의 길이를 입력으로 받는다.
        Scanner sc = new Scanner(System.in);
        System.out.println("세 변의 길이를 입력하세요: ");
        int triangle1 = sc.nextInt();
        int triangle2 = sc.nextInt();
        int triangle3 = sc.nextInt();

        String msg = "";
        // – 세 변의 길이가 삼각형을 형성할 수 있는 조건을 만족하는지 검사한다
        if (triangle1 + triangle2 <= triangle3 || triangle1 + triangle3 <= triangle2
                || triangle2 + triangle3 <= triangle1){
            // 형성할 수 없는 경우에는, 이유를 출력.
            System.out.println("삼각형을 형성할 수 없다");
            return;
        } else {
            if (triangle1 == triangle2 && triangle2 == triangle3){
                System.out.println("정삼각형");
            } else if (triangle1 == triangle2 || triangle1 == triangle3 || triangle2 == triangle3) {
                System.out.println("이등변삼각형");
            } else {
                System.out.println("부등변삼각형");
            }
        }

    }
}
