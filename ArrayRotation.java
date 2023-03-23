package com.TestAmazon.myPckage;

public class ArrayRotation {

	public static void main(String[] args) {
		
		int[] arr = new int[] {10,20,30,40,50};
		int i=0 , j=arr.length-1;
		
		// output = 50,10,20,30,40
		
		while(i<j)
		{
			int temp = arr[i];
			arr[i++] = arr[j];
			arr[j] = temp;
			
			
		}
		System.out.println("Shift Left....");

		for( i=0 ; i< arr.length;i++)
		System.out.println(arr[i]);
		
		// To rotate right
		
		// 20,30,40, 50,10
		
		int[] array = new int[] {10,20,30,40,50};
		 i=0 ; j=array.length-1;
		
		
		while(i<j)
		{
			int temp = array[i];
			array[i] = array[j];
			array[j--] = temp;
			
			
		}
		System.out.println("Shift Right....");

		for( i=0 ; i< array.length;i++)
		System.out.println(array[i]);
	}

}
