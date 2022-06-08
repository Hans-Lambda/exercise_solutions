def loogin():

    global user_name
    user_name=input("type your username: ")

    return user_name
#def sorting():
    #if

if __name__ == '__main__':

     chosen_messengers=[]
     prioritized_user_list = []
     messages=[]
     list_of_users = ["a", "b", "c", "d"]
     messengers_list = ["whatsapp","Messenger","Telegram"]
     print("✵✵✵✵✵✵✵✵USER´s✵✵✵✵✵✵✵✵")
     print(*list_of_users, sep="\n")
     print("✵✵✵✵✵✵✵✵MESSENGER´s✵✵✵✵✵✵✵")
     print(*messengers_list, sep="\n")




     num=int(input("how many users u want to prioritized: "))

     for i in range(num):
         pu = input("select a user: ")
         msngr = input("select a messenger")
         msg = input("enter your message: ")
         if pu in list_of_users:
          prioritized_user_list.append(pu)
          chosen_messengers.append(msngr)
          messages.append(msg)
     print(prioritized_user_list)
     loogin()

     num2 = len(prioritized_user_list)
     for i in range(num2):


        print(f"i will send {messages[i]} to {prioritized_user_list[i]} via {chosen_messengers[i]}")























