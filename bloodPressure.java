import java.io.*;
import java.time.LocalDate;
import java.util.Scanner;

public class bloodPressure {
    public static void main(String[] args) throws IOException {

        double weight;
        double sys = 0; //수축기 혈압
        double dia = 0; //이완기 혈압
        double pulse = 0; // 맥박수

        Scanner scanner = new Scanner(System.in);

//        System.out.println("몸무게를 입력하세요?");
//        weight = scanner.nextDouble();
//        System.out.println(weight+"kg");
        LocalDate now = LocalDate.now();

        System.out.println("1.입력하기 2.내역보기");
        int start = scanner.nextInt();
        if (start == 1) {
            System.out.println(now + " 혈압을 입력하세요?");
//        sys = scanner.nextInt();
//        dia = scanner.nextInt();
//        pulse = scanner.nextInt();
//        while로 무한 입력 반복하면서 돌때마다 i 값을 올려서 입력횟수만큼 평균값을 나중에 도출하도록;

            int i = 0;
            while (true) {
                System.out.println(i + 1 + " 회차 입력, 0으로 종료.");
                double a = scanner.nextDouble();
                double b = scanner.nextDouble();
                double c = scanner.nextDouble();
                if (a == 0 || b == 0 || c == 0) {
                    break;
                }// 스캐너a,b,c 사이사이에 끼워넣는 방식말고 깔끔하게 할수 없을까?
                sys = (sys + a);
                dia = (dia + b);
                pulse = (pulse + c);
                i++;
                System.out.println(sys / i + ", " + dia / i + ", " + pulse / i);
            }
            sys = Math.round(sys / i);
            dia = Math.round(dia / i);
            pulse = Math.round(pulse / i);
// int 라서 버림처리 되므로, 반올림 사용을 위한 방법 고려, math round 나 double이용
// 더블로 했을때 더 복잡해지거나 필요없는 문제를 처리하기 위한 방법들.
            System.out.println(now + ": " + sys + ", " + dia + ", " + pulse);
// 저장하시겠습니까? y or n. 물어보고 처리하는 방법
            if (sys != 0 || dia != 0 || pulse != 0) {
                PrintWriter pw = new PrintWriter(new FileWriter(
                        "c:/users/jhgre/ideaprojects/bloodpressure/bpdata.txt", true));
// 추가모드로 열기위해 pw안에 fw(경로,true)로 생성.
                pw.println(now);
                pw.println(sys);
                pw.println(dia);
                pw.println(pulse);
                pw.close();
            }

        }

        if (start == 2) { //내역 가져올 내용들 적기
            BufferedReader br = new BufferedReader(new FileReader(
                    "c:/users/jhgre/ideaprojects/bloodpressure/bpdata.txt"));
            while (true) {
                String line = br.readLine();
                if (line == null) break;
                System.out.println(line);
            }
        }
    }
}
//나온 값을 파일로 출력하기; + 이후 필요할때 불러와서 활용하기;
//오늘 날짜알기 LocalDate now = LocalDate.now();
//파라미터로 1.몸무게, 2.혈압 안에 들어가 또 선택해서 읽어오기
// 그래프 = line chart, XChart 활용
// 매 회차별로 모두 기록하기. 평균은 일별값으로.

//단독으로 실행되도록 gui 및 exe등 실행가능 프로그램으로 완성;
// 파이썬 변환후 PyQt 판다스로 gui,차트,데이터 분석 구현;