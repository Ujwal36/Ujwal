package com.TestAmazon.myPckage;

import net.bytebuddy.implementation.bytecode.Throw;

public class ReturnIndicesofTarget {
	
	
	
	public int[] findIndex(int[] arr, int target) throws Exception
	{
		int i,j;
		
		for(i=0; i<arr.length;i++)
		{
			int compliment = target -arr[i];
			for(j=i+1;j<arr.length;j++)
			{
				if(arr[j]==compliment)
				{
					return new int[] {i,j};
				}
			}
		}
		
		throw  new Exception("No indices found");
		//return new int[] {0,0};
		
		
		
	}

}
