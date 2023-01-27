import java.net.*;
import java.io.*;

public class UDPclient {
    public static void main(String[] args) {
        try {
            InetAddress acceptorHost = InetAddress.getByName("localhost");
            int serverPortNum = Integer.parseInt("4444");
            Socket clientSocket = new Socket(acceptorHost, serverPortNum);
            BufferedReader br = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
            System.out.println(br.readLine());
            clientSocket.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}