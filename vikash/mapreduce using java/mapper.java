import java.io.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.*;

public class LogMapper extends Mapper<Object, Text, Text, IntWritable> {

    private Text user = new Text();
    private IntWritable time = new IntWritable();

    public void map(Object key, Text value, Context context) throws IOException, InterruptedException {
        String[] parts = value.toString().split(" ");

        user.set(parts[0]); // username
        time.set(Integer.parseInt(parts[1])); // time

        context.write(user, time);
    }
}