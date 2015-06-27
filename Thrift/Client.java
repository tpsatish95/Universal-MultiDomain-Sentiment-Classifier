import org.apache.thrift.TException;
import org.apache.thrift.protocol.TBinaryProtocol;
import org.apache.thrift.protocol.TProtocol;
import org.apache.thrift.transport.TSocket;
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.TTransportException;

import javaThrift.*;

import java.io.*;
import java.util.*;

public class Client {

    TTransport transport;
    Sentiments.Client client = null;
    TProtocol protocol = null;
    public void Client(){
        transport = new TSocket("localhost", 8002);
        protocol = new TBinaryProtocol(transport);
        client = new Sentiments.Client(protocol);
        transport.open();
     }

    public void startClient() {

            System.out.println("Client is UP ! ;)");

            System.out.println("Enter Text to find Sentiment : ");

            Scanner s = new Scanner(System.in);

            String text = s.nextLine();

            String senti = client.getSentiment(text);

            System.out.println(senti);
    }

    protected void finalize( ) throws Throwable
    {
       transport.close()
       super.finalize( );
    }

    public static void main(String[] args) {
        Client client = new Client();
        client.startClient();
    }
}

