package net.avilaylabs.learnavro;

import org.apache.avro.file.DataFileReader;
import org.apache.avro.file.DataFileWriter;
import org.apache.avro.io.DatumReader;
import org.apache.avro.io.DatumWriter;
import org.apache.avro.specific.SpecificDatumReader;
import org.apache.avro.specific.SpecificDatumWriter;

import java.io.File;
import java.io.IOException;

/**
 * Hello world!
 *
 */
public class Compiled
{
    public static void serialize(String[] args) throws IOException {
        User user1 = new User();
        user1.setName("Alyssa");
        user1.setFavoriteNumber(256);
        // Leave favorite color null

        // Alternate constructor
        User user2 = new User("Ben", 7, "red");

        // Construct via builder
        User user3 = User.newBuilder()
                .setName("Charlie")
                .setFavoriteColor("blue")
                .setFavoriteNumber(null)
                .build();

        // Serialize user1, user2, and user3 to disk
        DatumWriter<User> userDatumWriter = new SpecificDatumWriter<User>(User.class);
        DataFileWriter<User> dataFileWriter = new DataFileWriter<User>(userDatumWriter);
        dataFileWriter.create(user1.getSchema(), new File("/Users/avilay.parekh/tmp/users.avro"));
        dataFileWriter.append(user1);
        dataFileWriter.append(user2);
        dataFileWriter.append(user3);
        dataFileWriter.close();
    }

    public static void deserialize(String[] args) throws IOException {
        File file = new File("/Users/avilay.parekh/tmp/users.avro");
        DatumReader<User> userDatumReader = new SpecificDatumReader<User>(User.class);
        DataFileReader<User> dataFileReader = new DataFileReader<User>(file, userDatumReader);
//        User user = null;
//        while (dataFileReader.hasNext()) {
//            user = dataFileReader.next(user);
//            System.out.println(user);
//        }
        for (User user : dataFileReader) {
            System.out.println(user);
        }
    }

    public static void main(String[] args) throws IOException {
        deserialize(args);
    }


}
