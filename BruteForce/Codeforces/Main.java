import java.io.*;
import java.util.*;

public class Main {
    private static MyScanner in;
    private static PrintStream out;

    public static void main(String[] args) throws IOException {
    
        boolean LOCAL_TEST = false;
        out = System.out;
        if (LOCAL_TEST) {
            in = new MyScanner("E:\\zin2.txt");
        }
        else {
            boolean usingFileForIO = false;
            if (usingFileForIO) {
                in = new MyScanner("input.txt");
                out = new PrintStream("output.txt");
            }
            else {
                in = new MyScanner();
                out = System.out;
            }
        }

        solve();
    }

    private static void solve() throws IOException
    {
        int n = in.nextInt();
        int m = in.nextInt();
        int[][] a = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                a[i][j] = in.nextInt();
            }
        }

        int res = Integer.MAX_VALUE;
        boolean[] isPrm = GetPrimeTable(200000);
        int[] nextPrm = new int[200001];
        int curPrm = 200000;
        while (!isPrm[curPrm])
            curPrm--;

        for (int i = curPrm; i >= 1; i--) {
            if (isPrm[i]) {
                curPrm = i;
            }
            nextPrm[i] = curPrm;
        }

        for (int i = 0; i < n; i++) {
            int step = 0;
            for (int j = 0; j < m; j++) {
                int num = a[i][j];
                step += nextPrm[num] - num;
            }
            res = Math.min(res, step);
        }
        for (int j = 0; j < m; j++) {
            int step = 0;
            for (int i = 0; i < n; i++) {
                int num = a[i][j];
                step += nextPrm[num] - num;
            }
            res = Math.min(res, step);
        }
        out.println(res);
    }

    public static boolean[] GetPrimeTable(int maxNum) {
        boolean[] isPrime = new boolean[maxNum + 1];
        for (int i = 0; i < isPrime.length; i++) {
            isPrime[i] = true;
        }
        isPrime[0] = isPrime[1] = false;
        int sqrtMaxNum = (int) Math.sqrt(maxNum) + 1;
        for (int i = 2; i <= sqrtMaxNum; i++) {
            if (!isPrime[i])
                continue;
            int k = i * i;
            while (k <= maxNum) {
                isPrime[k] = false;
                k += i;
            }
        }
        return isPrime;
    }

    static class MyScanner {
        Scanner inp = null;

        public MyScanner() throws IOException
        {
            inp = new Scanner(System.in);
        }

        public MyScanner(String inputFile) throws IOException {
            inp = new Scanner(new FileInputStream(inputFile));
        }

        public int nextInt() throws IOException {
            return inp.nextInt();
        }

        public long nextLong() throws IOException {
            return inp.nextLong();
        }

        public double nextDouble() throws IOException {
            return inp.nextDouble();
        }

        public String nextString() throws IOException {
            return inp.next();
        }

    }

}