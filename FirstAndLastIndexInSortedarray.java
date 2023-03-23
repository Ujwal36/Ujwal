package com.TestAmazon.myPckage;

public class FirstAndLastIndexInSortedarray {

	public static void main(String[] args) throws Exception{
		
		int[] a = new int[] {10,10,20,30,40,50,60,60};
		int target = 0;
		int i=0,j=0;
		for( i=0 ; i<a.length-1 ; i++)
		{
			if(a[i] == target)
			{
				for( j=i+1 ; j<a.length;j++)
				{
					if(a[i]==a[j])
					{
						continue;
					}
					else {
						j--;
						break;
					}
				}
				if(j==a.length) j--;
				break;
			}
			
		}
		
		if(target == a[i])
		{
			if(i==a.length-1)
			{
				// This is the last element
				System.out.println(i + " " + i);
			
			}
			else System.out.println(i + " , " + j);
		}
		else {
			System.out.println(" 404 Not found");
		}
		
		//System.out.println(i + " , " + j);
	
		
	}

}
