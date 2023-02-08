import java.util.*;
import java.net.*;
import java.io.*;

public class tcpC{
public static void main(String args[] )throws IOException{
	Socket s=new Socket("localhost",4999);
	PrintWriter pr= new PrintWriter(s.getOutputStream());
	Scanner in = new Scanner(System.in);
	System.out.println("Enter file name:");
	pr.println(in.nextLine());
	pr.flush();
	InputStreamReader ir= new InputStreamReader(s.getInputStream());
	BufferedReader bf=new BufferedReader(ir);
	
	String str=bf.readLine();
	System.out.println("Server: "+str);
}}