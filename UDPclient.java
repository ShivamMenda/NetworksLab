import java.net.*;
import java.io.*;

public class UDPclient {
    public static void main(String[] args) {
        try {
            Socket clientSocket = new Socket("127.0.0.1", 4444);
            BufferedReader br = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
            System.out.println(br.readLine());
            clientSocket.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}