import java.net.*;
import java.io.*;
import java.util.*;

public class tcpS{
public static void main(String args[]) throws IOException
{
	System.out.println("Server started");
	ServerSocket ss= new ServerSocket (4999);
	Socket s=ss.accept();
	System.out.println("Client Connected\n");
	
	PrintWriter pr= new PrintWriter(s.getOutputStream());
	pr.write("Hello client");
	pr.flush();
	
	InputStreamReader in = new InputStreamReader(s.getInputStream());
	BufferedReader bf= new BufferedReader(in);
	
	String str=bf.readLine();
	System.out.println("Filename from client: "+str);
	
	File file=new File(str);
	try{
		Scanner openfile= new Scanner(file);
		while(openfile.hasNextLine())
		{
			System.out.println(openfile.nextLine());
		}
	openfile.close();
	}
	catch (FileNotFoundException e)
	{
	System.out.println("Does not exist");
	}
	
}
}