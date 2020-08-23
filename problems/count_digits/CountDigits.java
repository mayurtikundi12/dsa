public class CountDigits {
    public CountDigits(){}
    public int count_digits(int num ){
        if (num ==0) {
            return 0;
        }
        return 1+ count_digits(num/10);
    }

    public static void main(String[] args){
        CountDigits cd = new CountDigits();
        int result = cd.count_digits(14205);
        System.out.println("Number of digits is "+result);
    }
}