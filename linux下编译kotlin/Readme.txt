1.下载/kotlin-compiler-1.2.20-eap-11.zip编译器
2.配置环境
(vscode)code ~/.bashrc:
export KOTLIN_HOME=/home/xujiaxin/Android/kotlin-compiler-1.2.20-eap-11/kotlinc
export PATH="$PATH:$KOTLIN_HOME/bin"
3.新建Hello.kt文件,code:
fun main(args: Array<String>) {
    println("Hello, World!")
}
4.编译Hello.kt生成HelloKt.class
kotlinc Hello.kt
执行kotlin HelloKt
输出Hello, World!