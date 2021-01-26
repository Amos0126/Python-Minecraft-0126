from mcpi.minecraft import Minecraft
a = Minecraft.create()

while True:
    username = input("your name:")
    message = input("you want to say:")
    a.postToChat("<"+username + "> " + message)