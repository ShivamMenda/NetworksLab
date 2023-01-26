
import java.net.*;
import java.io.*;

public class tcpClient {
    public static void main(String[] args) throws Exception {
        Socket sock=new Socket("127.0.0.1",4000);
        System.out.println("Enter filename");
        BufferedReader keyRead=new BufferedReader(new InputStreamReader(System.in));
        String fname=keyRead.readLine();
        OutputStream oStream=sock.getOutputStream();
        PrintWriter printWriter=new PrintWriter(oStream,true);
        printWriter.println(fname);
        InputStream inputStream=sock.getInputStream();
        BufferedReader sockRead=new BufferedReader(new InputStreamReader(inputStream));
        String str;
        while ((str=sockRead.readLine())!=null) {
            System.out.println(str);
            
        }
        printWriter.close();
        sockRead.close();
        keyRead.close();
        sock.close();
    }
}