import java.io.Serializable;

public class Person implements Serializable {
    private String name;
    private int id;

    public Person() {}

    public Person(int id, String name) {
        this.name = name;
        this.id = id;
    }

    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getId() {
        return this.id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public void show() {
        StringBuilder sb = new StringBuilder();
        sb.append("id: ");
        sb.append(this.id);
        sb.append(", Name: ");
        sb.append(this.name);
        System.out.println(sb.toString());
    }
}
