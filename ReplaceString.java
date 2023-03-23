package com.TestAmazon.myPckage;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.CharBuffer;

public class ReplaceString {

	public static void main(String[] args) {
		//Replace "Amazon" Text in a given file to "It"
		
		
		try {
			BufferedReader bf = new BufferedReader(new FileReader("/Users/ujwal.koteesh/Documents/filename.rtf"));
			
			String line=null;
			String oldcontent = "";
			
			
			while((line = bf.readLine()) != null)
			{
				oldcontent = oldcontent + line + System.lineSeparator();	
				
			}
			String newcontent = oldcontent.replaceAll("Amazon", "It");
			
			
			FileWriter fw = new FileWriter("/Users/ujwal.koteesh/Documents/filename.rtf");
			
			fw.write(newcontent);
			
			bf.close();
			
			
	
			
			
			
			
			
			
			
			
			bf.close();
			fw.close();
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		
		
		
	}

}
