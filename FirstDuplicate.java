package Test;

import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Scanner;

public class FirstDuplicate {
	
	static LinkedHashMap<Integer,Integer> occurance(int[] arr)
	{
		LinkedHashMap<Integer,Integer> arrays = new LinkedHashMap<>();
		int n = arr.length;
		for(int i=0;i<n;i++)
		{
			if(arrays.containsKey(arr[i]))
			{
				
					arrays.put(arr[i], arrays.get(arr[i])+1);
					
			}
			else {
				arrays.put(arr[i], 1);
			}
					
		}
		return arrays;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		System.out.print("Enter the number of integers in an array");
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] arr = new int[n];
		int i=0;
		
		while(i<n)
		{
			arr[i]=sc.nextInt();
			//System.out.println(arr[i]);
			i++;
			
		}
		
		
				
		LinkedHashMap <Integer, Integer> arrays =   occurance(arr);
		
		// Logic to find first duplicate
		System.out.println(arrays);
		
		
		for(i=0;i<n;i++)
		{
			if(arrays.get(arr[i])==1)
				
			{
				System.out.println("The first non-duplicate is:" + arr[i]);
				break;
			}
			
		}
		
		
	}

}
