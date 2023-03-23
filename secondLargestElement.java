package Test;

import java.util.Scanner;

public class secondLargestElement {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		System.out.println(" Enter the number of elements");
		int n = sc.nextInt();
		int elements[] = new int[n];
		
		if(n > 0)
		{
		System.out.println(" Enter the " + n  + " elements");
		
		for(int i =0; i<n; i++)
		{
			elements[i] = sc.nextInt();
			
					
					
		}
		
		
			if(n==1) {
				
				System.out.println(" There is only one element so "+ elements[n-1] + " is the only largest");
				
			}
			else {
		
				int firstlargest = elements[0];
				int secondLargest = elements[1]; // --> This is a problem
				for (int i =1 ; i<n; i++)
				{
					if(elements[i] > firstlargest)
					{
						secondLargest = firstlargest;
						firstlargest = elements[i];
						
					}
					else if(elements[i]> secondLargest) 
					{
						secondLargest = elements[i];
					}
				}
				System.out.println("Second Largest is: " + secondLargest);
			}
		}
			
			else {
				
				System.out.println("No elements present...");
			}
		
		}
		
			
		
		
		
		
		

	}


