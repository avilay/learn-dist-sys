package net.avilaylabs.learnavro;

import org.apache.avro.Schema;
import org.apache.avro.file.DataFileReader;
import org.apache.avro.file.DataFileWriter;
import org.apache.avro.generic.GenericData;
import org.apache.avro.generic.GenericDatumReader;
import org.apache.avro.generic.GenericDatumWriter;
import org.apache.avro.generic.GenericRecord;
import org.apache.avro.io.DatumReader;
import org.apache.avro.io.DatumWriter;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * Created by avilay.parekh on 11/15/16.
 */
public class Dynamic {
    public static void serialize(String[] args) throws IOException {
        Schema schema = new Schema.Parser().parse(new File("/Users/avilay.parekh/projects/learn/learn-avro/src/main/avro/user.avsc"));

        GenericRecord user1 = new GenericData.Record(schema);
        user1.put("name", "Alyssa");
        user1.put("favorite_number", 256);
        // Leave favorite color null

        GenericRecord user2 = new GenericData.Record(schema);
        user2.put("name", "Ben");
        user2.put("favorite_number", 7);
        user2.put("favorite_color", "red");

        // Serialize user1 and user2 to disk
        File file = new File("/Users/avilay.parekh/tmp/users_dyn.avro");
        DatumWriter<GenericRecord> datumWriter = new GenericDatumWriter<GenericRecord>(schema);
        DataFileWriter<GenericRecord> dataFileWriter = new DataFileWriter<GenericRecord>(datumWriter);
        dataFileWriter.create(schema, file);
        dataFileWriter.append(user1);
        dataFileWriter.append(user2);
        dataFileWriter.close();
    }

    public static void deserialize(String[] args) throws IOException {
        File dataFile = new File("/Users/avilay.parekh/tmp/users_dyn.avro");
        File schemaFile = new File("/Users/avilay.parekh/projects/learn/learn-avro/src/main/avro/user.avsc");

        Schema schema = new Schema.Parser().parse(schemaFile);
        DatumReader<GenericRecord> datumReader = new GenericDatumReader<GenericRecord>(schema);
        DataFileReader<GenericRecord> dataFileReader = new DataFileReader<GenericRecord>(dataFile, datumReader);
        for (GenericRecord user : dataFileReader) {
            System.out.println(user);
        }
    }

    public static void dynDeserialize(String[] args) throws IOException {
        File dataFile = new File("/Users/avilay.parekh/tmp/soe_1.avro");

        DatumReader<GenericRecord> datumReader = new GenericDatumReader<GenericRecord>();
        DataFileReader<GenericRecord> dataFileReader = new DataFileReader<GenericRecord>(dataFile, datumReader);
        List<GenericRecord> rec = new ArrayList<>();
        for (GenericRecord soe: dataFileReader) {
            rec.add(soe);
        }
        System.out.println(rec.size());
        for (int i = 0; i < 3; i++) {
            System.out.println(rec.get(i));
        }

    }

    public static void main(String[] args) throws Exception {
        serialize(args);
//        deserialize(args);
//        dynDeserialize(args);
    }
}
