package com.TestAmazon.myPckage;

import java.util.Arrays;

public class AllZeroesatEnd {

	public static void main(String[] args) {
		
		
		int num[] = new int[] {0,3,1,2,0,5,0,0,9,7,0};
		
		
		int i=0;
		int j= num.length - 1;
		
		while(i<j)
		{
			if(num[i] == num[j] && num[j]==0)
			{
				j--;
			}
			else if(num[i] == 0 && num[j]!=0)
			{
				int temp = num[j];
				num[j]=num[i];
				num[i]=temp;
				i++;
				j--;
				
			}
			
			else if(num[i] != 0 && num[j]==0)
			{
				i++;
			}
			
			else
			{
				i++;
				
			}
			
		}
		
		System.out.println(Arrays.toString(num));

	}

}
