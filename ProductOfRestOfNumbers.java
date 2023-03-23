package Test;

import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Scanner;

public class ProductOfRestOfNumbers {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int[] nums = new int[5];
		
		System.out.println("Enter number of elements");
		
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int product = 1;
		int Actualproduct =1;
		int i=0;
		if(n==1)
		{
			System.out.print("Please enter atleast 2 elements");
		}
		while(i<n)
		{
			nums[i]= sc.nextInt();
			if(nums[i] ==0)
			{
				
				product = 0;
				//product*=nums[i];
				i++;
			}
			else
			{
				Actualproduct*=nums[i];
				i++;
			}
		}
		
		LinkedHashMap<Integer,Integer> hm = new LinkedHashMap<>();
		
		
		
		for(i=0;i<nums.length;i++)
		{
			
			int complement  = 0;
			if(nums[i]==0)
			{
				// There are some elements which are 0
				complement = Actualproduct;
				
				
			}
			else
			{
				if(product ==0)
				{
					complement = 0;
				}
				else {
						complement = Actualproduct/nums[i];
				}
			}
			hm.put(nums[i], complement);
			
		}
		
		System.out.print(hm);

	}

}
