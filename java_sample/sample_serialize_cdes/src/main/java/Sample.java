import java.io.*;

public class Sample {
    public static void main(String args[]) {
        Person person = new Person(1, "taro");
        String filename = "person.ser";

        // save
        try(ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(filename))) {
            oos.writeObject(person);
        } catch (IOException e) {
            e.printStackTrace();
        }

        // load
        Person person2 = new Person();
        try(ObjectInputStream ois = new ObjectInputStream(new FileInputStream(filename))) {
            person2 = (Person) ois.readObject();
        } catch (IOException e) {
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }

        person.show();
        person2.show();
        System.out.println("DONE");
    }
}
