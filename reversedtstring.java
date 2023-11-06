class reversedtstring{
    public static void main(String []args){
        String str="hello";
        String rev="";
        int length=str.length();
        for (int i=0;i<length;i++){
            rev=str.charAt(i)+rev;
        }
        System.out.println(rev);

    }
}