package com.TestAmazon.myPckage;

public class BinarySearch {

	public static void main(String[] args) {
		//To find the first and last index of target in a num array
		
		int [] a = new int[] {1,1,4,5,6,6,6,7,8};
		
		int target = 6;
		int index = -1;
		
		int i=0;
		int j=a.length-1;
		int mid=-1;
		
		while(i<=j)
		{
			mid = (i+j)/2;
			 System.out.println(mid);

			
			 if(target <= a[mid])
			{
				j=mid-1;
			}
			  if(target>a[mid])
			 {
				 i=mid+1;
			 }
			 if(target==a[mid])
			 {
				 index=mid;
			 }
				
		}
		
		System.out.println(index);
		
		
		i=0;
		 j=a.length-1;
		 mid=-1;
		
		while(i<=j)
		{
			mid = (i+j)/2;
			// System.out.println(mid);

			
			 if(target < a[mid])
			{
				j=mid-1;
			}
			  if(target>=a[mid])
			 {
				 i=mid+1;
			 }
			 if(target==a[mid])
			 {
				 index=mid;
			 }
				
		}
		
		System.out.println(index);
		
		
	}

}
