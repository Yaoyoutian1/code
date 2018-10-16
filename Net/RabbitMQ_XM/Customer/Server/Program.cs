using System;
using System.Text;
using RabbitMQ.Client;

namespace Server
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("请开始你的表演,安回车键发送:");
            while (true)
            {
                var msg = Console.ReadLine();
                fun(msg);
            }
        }

        /// <summary>
        ///(1)：创建ConnectionFactory，并且设置一些参数，比如hostname,portNumber等等
        ///(2)：利用ConnectionFactory创建一个Connection连接
        ///(3)：利用Connection创建一个Channel通道
        ///(4)：创建queue并且和Channel进行绑定
        ///(5)：创建消息，并且发送到队列中
        /// </summary>
        public static void fun(string msg)
        {

            var factory = new ConnectionFactory() { HostName = "localhost", UserName= "guest", Password="guest" };       //设置本地   创建ConnectionFactory，并且设置一些参数，比如hostname,portNumber等等
            using (var connection = factory.CreateConnection())             //创建socket连接
            using (var channel = connection.CreateModel())                  //创建channel通道
            {
                channel.QueueDeclare(queue: "Hello", durable: false, exclusive: false, autoDelete: false, arguments: null);   //创建了一个queue队列

                var body = Encoding.UTF8.GetBytes(msg);         //把消息转换为字节流

                //注意: (routingKey)  路由密钥必须小于255字节。
                channel.BasicPublish(exchange: "", routingKey: "Hello", basicProperties: null, body: body);

                Console.WriteLine("[send:] sent :{0}", msg);
            }
        }
    }
}
