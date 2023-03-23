package com.TestAmazon.myPckage;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.Arrays;

public class FileOperations {

	public static void main(String[] args) {
		
		
		String line = null;
		String s[];
		int count =0;
		
		try {
			
		
		
		BufferedReader bf = new BufferedReader(new FileReader("/Users/ujwal.koteesh/Documents/filename.rtf"));
		
		
		
		while((line = bf.readLine())!=null)
		{
			System.out.println(line);
			line = line.trim();
			System.out.println(line);

			s=line.split(" ");
			count += s.length;
			System.out.println(Arrays.toString(s));
		}
		
		bf.close();
		
		System.out.println(count);

	}
		catch(Exception e)
		{
			e.printStackTrace();
		}
	
	}

}
