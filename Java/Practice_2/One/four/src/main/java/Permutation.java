import java.util.Scanner;
public class Permutation {

    static void combinationUtil(int arr[], int n, int r, int index, int data[], int i)
    {
        if (index == r)
        {
            for (int j=0; j<r; j++)
                System.out.print(data[j]+" ");
            System.out.println("");
            return;
        }

        if (i >= n)
            return;
        data[index] = arr[i];
        combinationUtil(arr, n, r, index+1, data, i+1);
        combinationUtil(arr, n, r, index, data, i+1);
    }

    static void printCombination(int arr[], int n, int r)
    {
        int data[]=new int[r];
        combinationUtil(arr, n, r, 0, data, 0);

    }

    public static void main (String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter array length: ");
        int size = input.nextInt();
        int r = size-1;
        if (size==1){
            System.out.println("1");
        }
        else {
            int arr[] = new int[size];

            for (int i = 0; i < size; i++) {
                System.out.printf("number %d is ", i+1);
                arr[i] = input.nextInt();
            }

            System.out.println();


            for (int i=0; i<size; i++){
                System.out.printf("%d ",arr[i]);

            }
            int n = arr.length;
            System.out.println();
            for (int i=0; i<size; i++){
                System.out.println(arr[i]);

            }

            printCombination(arr, n, r);
        }


    }
}
