package com.TestAmazon.myPckage;

public class HitachiAutoTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int[] a = new int[] {3, 9, 50, 15, 99, 7, 98, 65};


		int curr_min =0;
		int min = Integer.MAX_VALUE;

		for(int I=0 ; I<a.length -1; I++)
		{
			for(int j=I+1; j<a.length ; j ++)
			{
				curr_min = a[j] - a[I];
				if(curr_min < min)
					min = curr_min;
			}
		}
				
			System.out.println(min);
	}

}
