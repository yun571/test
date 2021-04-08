class HelloWorld{
    private native void print();
    public static void main(String[] args){
        new HelloWorld().print();
    }
        static{
            System.load("/home/xujiaxin/test/libHellWorld.so");
        }
    }