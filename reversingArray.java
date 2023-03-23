package Test;

import java.util.ArrayList;
import java.util.Scanner;

public class reversingArray {

	public static void main(String[] args) {
		
		int[] arr = new int[4];
		
		int i=0;
		Scanner sc = new Scanner(System.in);
		
		while(sc.hasNextInt())
		{
			arr[i] = sc.nextInt();
			i++;
					
		}
		int  temp;
		int n= arr.length;
		for(i=n; i>n/2; i--)
		{
			temp = arr[i-1];
			arr[i-1] = arr[n-i];
			arr[n-i] = temp;
		}
		
		for(i=0;i<arr.length;i++)
		{
			System.out.println(arr[i]);
		}
		
		
	}

}
