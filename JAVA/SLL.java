public class SLL {
    // Node class
    private static class Node {
        int data;
        Node next;

        Node(int data) {
            this.data = data;
            this.next = null;
        }
    }

    private Node head;

    // Constructor
    public SLL() {
        this.head = null;
    }

    // Method to add a node at the end
    public void add(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
        } else {
            Node current = head;
            while (current.next != null) {
                current = current.next;
            }
            current.next = newNode;
        }
    }

    // Method to display the list
    public void display() {
        Node current = head;
        while (current != null) {
            System.out.print(current.data + " -> ");
            current = current.next;
        }
        System.out.println("null");
    }

    // Method to delete a node by value
    public void delete(int data) {
        if (head == null) return;

        if (head.data == data) {
            head = head.next;
            return;
        }

        Node current = head;
        while (current.next != null && current.next.data != data) {
            current = current.next;
        }

        if (current.next != null) {
            current.next = current.next.next;
        }
    }

    public static void main(String[] args) {
        SLL
 list = new SLL
();
        list.add(1);
        list.add(2);
        list.add(3);
        list.display(); // Output: 1 -> 2 -> 3 -> null

        list.delete(2);
        list.display(); // Output: 1 -> 3 -> null
    }
}