import discord
import os
import random
import time


client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("나 자신개발")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    #기본 대화
    if message.content.startswith("안녕"):
        await message.channel.send("반가워")
    if message.content.startswith("안냐세요"):
        await message.channel.send("반가워")
    if message.content.startswith("한돈맛에"):
        await message.channel.send("미아핑찍지마!")
    if message.content.startswith("위버야"):
        await message.channel.send("네 주인님")
    if message.content.startswith("김고"):
        await message.channel.send("아 윈투 김고 홍삼 김고")
    if message.content.startswith("민머리대머리"):
        await message.channel.send("맨드맨들현석이")
    if message.content.startswith("사진은뭐야"):
        await message.channel.send("사진은 빛으로 그리는 그림이죠")
    if message.content.startswith("페르마의 마지막 정리"):
        await message.channel.send("n이 3 이상의 정수일 때, x^n＋y^n＝z^n을 만족하는 양의 정수 x, y, z는 존재하지 않는다.")
    if message.content.startswith("원주율마지막"):
        await message.channel.send("ᠮᠣᠩᠭᠣᠯ이며 지구문자로 표현 할 수 없습니다")
    if message.content.startswith("/채널메시지"):
        channel = message.content[7:25]
        msg = message.content[26:]
        await  client.get_channel(int(channel)).send(msg)


    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[1]
        await message.channel.send(file=discord.File(pic))


    #설명서
    if message.content.startswith("위버야도움말"):
        await message.channel.send("""
1.사다리타기 3인용(롤) (명령어: 위버야사다리타기(3)) 각자 123456중 선택해 위버가 보여준 팀으로 간다 
2.테러 위버야테러 라고입력하면 위버가 그방에서 1000까지 숫자를 센다   """)




   #구구단
    if message.content.startswith("위버야구구단"):
        for dan in range(2,10):
            await message.channel.send(str(dan) + '단')
            for hang in range(2,10):
                number = int(dan * hang)
                await message.channel.send(str(dan) + '*' + str(hang) + '=' + str(number))

    #사다리타기 3인용팀정하기
    if message.content.startswith("위버야사다리타기(3)"):
        await message.channel.send("123456중에 숫자를 고르시요(머리속으로)")
        time.sleep(5)
        await message.channel.send("5초남았습니다")
        time.sleep(4)
        team_1 = 0
        team_2 = 0
        team_3 = 0
        team_4 = 0
        team_5 = 0
        team_6 = 0

        a = 0
        b = 0

        team_1 = random.randint(1, 2)
        if team_1 == 1:
            a += 1
        else:
            b += 1

        team_2 = random.randint(1, 2)
        if team_2 == 1:
            a += 1
        else:
            b += 1

        team_3 = random.randint(1, 2)
        if team_3 == 1:
            a += 1
        else:
            b += 1

        if a == 3:
            team_4 = 2
            team_5 = 2
            team_6 = 2
        elif b == 3:
            team_4 = 1
            team_5 = 1
            team_6 = 1

        else:
            team_4 = random.randint(1, 2)
            if team_4 == 1:
                a += 1
            else:
                b += 1

            if a == 3:
                team_5 = 2
                team_6 = 2
            elif b == 3:
                team_5 = 1
                team_6 = 1
            else:
                team_5 = random.randint(1, 2)
                if team_5 == 1:
                    a += 1
                else:
                    b += 1

                if a == 3:
                    team_6 = 2
                else:
                    team_6 = 1

        if team_1 == 1:
            await message.channel.send("1번 red")
        else:
            await message.channel.send("1번 blue")
        if team_2 == 1:
            await message.channel.send("2번 red")
        else:
            await message.channel.send("2번 blue")
        if team_3 == 1:
            await message.channel.send("3번 red")
        else:
            await message.channel.send("3번 blue")
        if team_4 == 1:
            await message.channel.send("4번 red")
        else:
            await message.channel.send("4번 blue")
        if team_5 == 1:
            await message.channel.send("5번 red")
        else:
            await message.channel.send("5번 blue")
        if team_6 == 1:
            await message.channel.send("6번 red")
        else:
            await message.channel.send("6번 blue")
#____________________________________________________
#여기까지 사다리
    if message.content.startswith("위버야테러"):
        for mumber in range(1, 1000):
            await message.channel.send(str(mumber))



access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
