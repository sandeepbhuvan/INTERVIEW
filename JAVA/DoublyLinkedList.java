public class DoublyLinkedList {

    class Node {
        int data;
        Node prev;
        Node next;

        Node(int data) {
            this.data = data;
        }
    }

    private Node head;
    private Node tail;

    // Add a node at the end of the list
    public void append(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = tail = newNode;
            head.prev = null;
            tail.next = null;
        } else {
            tail.next = newNode;
            newNode.prev = tail;
            tail = newNode;
            tail.next = null;
        }
    }

    // Add a node at the beginning of the list
    public void prepend(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = tail = newNode;
            head.prev = null;
            tail.next = null;
        } else {
            head.prev = newNode;
            newNode.next = head;
            head = newNode;
            head.prev = null;
        }
    }

    // Print the list from head to tail
    public void printForward() {
        Node current = head;
        while (current != null) {
            System.out.print(current.data + " ");
            current = current.next;
        }
        System.out.println();
    }

    // Print the list from tail to head
    public void printBackward() {
        Node current = tail;
        while (current != null) {
            System.out.print(current.data + " ");
            current = current.prev;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        DoublyLinkedList dll = new DoublyLinkedList();
        dll.append(10);
        dll.append(20);
        dll.append(30);
        dll.prepend(5);
        dll.printForward();  // Output: 5 10 20 30
        dll.printBackward(); // Output: 30 20 10 5
    }
}