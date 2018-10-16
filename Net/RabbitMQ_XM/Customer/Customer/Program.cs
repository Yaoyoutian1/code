using System;
using System.Text;
using RabbitMQ.Client;
using RabbitMQ.Client.Events;

namespace Customer
{
    class Program
    {
        static void Main(string[] args)
        {
            fun();

        }

        /// <summary>
        ///(1)：创建ConnectionFactory，并且设置一些参数，比如hostname,portNumber等等
        ///(2)：利用ConnectionFactory创建一个Connection连接
        ///(3)：利用Connection创建一个Channel通道
        ///(4)：将queue和Channel进行绑定，注意这里的queue名字要和前面producer创建的queue一致
        ///(5)：创建消费者Consumer来接收消息，同时将消费者和queue进行绑定
        /// </summary>
        public static void fun()
        {
            var factory = new ConnectionFactory() { HostName = "localhost", UserName = "guest", Password = "guest" };       //设置本地   创建ConnectionFactory，并且设置一些参数，比如hostname,portNumber等等
            using (var connection = factory.CreateConnection())             //创建socket连接
            using (var channel = connection.CreateModel())                  //创建channel通道
            {
                channel.QueueDeclare(queue: "Hello", durable: false, exclusive: false, autoDelete: false, arguments: null);   //创建了一个queue队列

                var consumer = new EventingBasicConsumer(channel);                  //创建基本消费者
                consumer.Received += (mode, ea) =>
                {                                //用户收到信息
                    var body = ea.Body;
                    var msg = Encoding.UTF8.GetString(body);
                    Console.WriteLine(" [x] 收到 {0}", msg);
                };
                channel.BasicConsume(queue: "Hello",
                                    autoAck: true,
                                    consumer: consumer);
                Console.WriteLine("接收消息结束");
                Console.ReadLine();
            }
        }

    }
}
