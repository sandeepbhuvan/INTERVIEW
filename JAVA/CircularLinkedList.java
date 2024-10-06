public class CircularLinkedList {
    private Node head = null;
    private Node tail = null;

    // Node class
    private class Node {
        int data;
        Node next;

        public Node(int data) {
            this.data = data;
        }
    }

    // Add a node to the list
    public void add(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
            tail = newNode;
            newNode.next = head;
        } else {
            tail.next = newNode;
            tail = newNode;
            tail.next = head;
        }
    }

    // Display the nodes in the list
    public void display() {
        Node current = head;
        if (head != null) {
            do {
                System.out.print(current.data + " ");
                current = current.next;
            } while (current != head);
        }
    }

    public static void main(String[] args) {
        CircularLinkedList list = new CircularLinkedList();
        list.add(1);
        list.add(2);
        list.add(3);
        list.add(4);

        list.display();
    }
}