package addTwoNubers;

/**
 * ListNode
 */
public class ListNode {
    int val;
    ListNode next;

    public ListNode() {
    }

    public ListNode(int val) {
        this.val = val;
    }

    public ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode l3 = new ListNode();
        ListNode curr = l3;
        int carry = 0;

        // head node
        l3.val = l1.val + l2.val;
        if (l3.val >= 10) {
            carry = 1;
            l3.val -= 10;
        }
        l1 = l1.next;
        l2 = l2.next;
        // middle node
        while (l1 != null || l2 != null || carry != 0) {
            if (l1 == null && l2 == null && carry != 0) {
                ListNode node = new ListNode(1);
                carry = 0;
                curr.next = node;
                break;
            }
            ListNode node = new ListNode();
            if (l1 != null && l2 != null) {
                node.val = l1.val + l2.val + carry;
            } else if (l1 == null && l2 != null) {
                node.val = l2.val + carry;
            } else if (l1 != null && l2 == null) {
                node.val = l1.val + carry ;
            }
            
            curr.next = node;
            carry = 0;
            if (node.val >= 10) {
                carry = 1;
                node.val -= 10;
            }
            if (l1 != null)
                l1 = l1.next;
            if (l2 != null)
                l2 = l2.next;
            curr = curr.next;
        }
        return l3;
    }

    private static void printList(ListNode list) {
        while (list != null) {
            System.out.println(list.val);
            list = list.next;
        }
    }
    

    public static void main(String[] args) {
        ListNode a = new ListNode(5);
        ListNode b = new ListNode(6, a);
        ListNode c = new ListNode(7, b);

        ListNode A = new ListNode(4);
        ListNode B = new ListNode(5, A);
        ListNode C = new ListNode(6, B);

        ListNode test = addTwoNumbers(c, C);
        printList(test);
        



    }

    
    
    
}