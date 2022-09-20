class FinalParentClass {
    public void print () {
        System.out.println("This is final method");
    }
} 
public final class ChildClass extends FinalParentClass {
    public void print() {
        System.out.println("This is overridden method”");
    }
}