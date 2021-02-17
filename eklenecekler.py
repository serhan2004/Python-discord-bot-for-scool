from datetime import datetime

class Ders:
    def __init__(self, ders_ismi, ogretmen, bilgi):
        self.ders_ismi = ders_ismi
        self.ogretmen = ogretmen
        self.bilgi = bilgi
    def ders_yazdir(self):
        return  f"Ders: {self.ders_ismi} \n Öğretmen: {self.ogretmen} \n Giris: {self.bilgi} "


simdiki_zaman = datetime.now()
gun = simdiki_zaman.weekday()
saat = simdiki_zaman.hour
dakika = simdiki_zaman.minute


edebiyat = Ders(ders_ismi = "Edebiyat", ogretmen= "Tuğba Yağcı", bilgi="4079105023\n 5df5ZA ")
kimya = Ders("Kimya", "Serdar Reis", "4081055576\nZ8pgBF")
beden = Ders("Beden","Ahmet Hoca", "4587437919 \n 2v0RQh")
din = Ders("Din", "Ahmet B", "4948543181 \n 3WxsGu")
almanca = Ders("Almanca", "Simge Hoca", " 7983919851\n123456")
ingilizce= Ders("İngilizce" , "Merve Hoca", "5139496502 \n 008157")
biyoloji= Ders("Biyoloji", "Şule Hoca", " 7272752155 \n 138141")
fizik= Ders("Fizik","Zehra Aygül", "8832100812 \n 254470")
resim = Ders("Resim", "Özgül kıskac", "5296728582 \n 6a4w88")
tarih= Ders("Tarih", "Alime Hoca", " 6255223788 | 8GL1Ht")
felsefe= Ders("Felse", "Ebru Hoca", "6947841095 \n qhmjF8")
matematik= Ders("Matematik", "Mehmet Hoca", " 4986677385 \n matematik")




ders_listem = [
[edebiyat,matematik,ingilizce,resim,fizik,tarih,biyoloji],
[ingilizce,biyoloji,beden,beden,edebiyat,din,kimya,kimya],
[edebiyat,edebiyat,biyoloji,biyoloji,felsefe,felsefe,matematik,biyoloji],
[fizik,fizik,tarih,matematik,matematik,ingilizce,edebiyat,din],
[almanca,almanca,matematik,matematik,kimya,kimya,fizik,ingilizce]]


@client.command(name="ders")
async def ders(ctx):
    if gun == "monday":
        if saat == 8:
            await ctx.channel.send(edebiyat.ders_yazdir())
        elif saat == 9 and dakika <40:
            await ctx.channel.send(matematik.ders_yazdir())
        elif saat ==10 and dakika >49:
            await ctx.channel.send(ingilizce.ders_yazdir())
        elif saat ==11:
            await ctx.channel.send(resim.ders_yazdir())
        elif saat ==11:
            await ctx.channel.send(resim.ders_yazdir())
        elif saat == 12:
            await ctx.channel.send(fizik.ders_yazdir())
        elif saat ==13 and dakika<50:
            await ctx.channel.send(tarih.ders_yazdir())
        elif 
        
        else:
            await ctx.channel.send("Bruuh Eğer bu satır çalıştıysa ya yazdığım kod hatalı yada ders saatleri dışında yazıyorsun")

            
    elif gun == "tuesday":
        if saat == 8:
            await ctx.channel.send(ingilizce.ders_yazdir())
        elif saat == 9 and dakika <40:
            await ctx.channel.send(biyoloji.ders_yazdir())
        elif saat ==10 and dakika >49:
            await ctx.channel.send(beden.ders_yazdir())
        elif saat ==11:
            await ctx.channel.send(beden.ders_yazdir())
        elif saat ==11:
            await ctx.channel.send(edebiyat.ders_yazdir())
        elif saat == 12:
            await ctx.channel.send(edebiyat.ders_yazdir())
        elif saat ==13:
            await ctx.channel.send(biyoloji.ders_yazdir())
        else:
            await ctx.channel.send("Bruuh Eğer bu satır çalıştıysa ya yazdığım kod hatalı yada ders saatleri dışında yazıyorsun")


    elif gun == "wednesday":
        if saat == 8:
            await ctx.channel.send(edebiyat.ders_yazdir())
        elif saat == 9 and dakika <40:
            await ctx.channel.send(matematik.ders_yazdir())
        elif saat ==10 and dakika >49:
            await ctx.channel.send(ingilizce.ders_yazdir())
        elif saat ==11:
            await ctx.channel.send(resim.ders_yazdir())
        elif saat ==11:
            await ctx.channel.send(resim.ders_yazdir())
        elif saat == 12:
            await ctx.channel.send(tarih.ders_yazdir())
        elif saat ==13:
            await ctx.channel.send(biyoloji.ders_yazdir())
        else:
            await ctx.channel.send("Bruuh Eğer bu satır çalıştıysa ya yazdığım kod hatalı yada ders saatleri dışında yazıyorsun")

    elif gun == "thursday":
        if saat == 8:
            await ctx.channel.send(edebiyat.ders_yazdir())
        elif saat == 9 and dakika <40:
            await ctx.channel.send(matematik.ders_yazdir())
        elif saat ==10 and dakika >49:
            await ctx.channel.send(ingilizce.ders_yazdir())
        elif saat ==11:
            await ctx.channel.send(resim.ders_yazdir())
        elif saat ==11:
            await ctx.channel.send(resim.ders_yazdir())
        elif saat == 12:
            await ctx.channel.send(tarih.ders_yazdir())
        elif saat ==13:
            await ctx.channel.send(biyoloji.ders_yazdir())
        else:
            await ctx.channel.send("Bruuh Eğer bu satır çalıştıysa ya yazdığım kod hatalı yada ders saatleri dışında yazıyorsun")

    elif gun == "friday":
        if saat == 8:
            await ctx.channel.send(edebiyat.ders_yazdir())
        elif saat == 9 and dakika <40:
            await ctx.channel.send(matematik.ders_yazdir())
        elif saat ==10 and dakika >49:
            await ctx.channel.send(ingilizce.ders_yazdir())
        elif saat ==11:
            await ctx.channel.send(resim.ders_yazdir())
        elif saat ==11:
            await ctx.channel.send(resim.ders_yazdir())
        elif saat == 12:
            await ctx.channel.send(tarih.ders_yazdir())
        elif saat ==13:
            await ctx.channel.send(biyoloji.ders_yazdir())
        else:
            await ctx.channel.send("Bruuh Eğer bu satır çalıştıysa ya yazdığım kod hatalı yada ders saatleri dışında yazıyorsun")

    else:
        ctx.channel.send("Hafta içi tekrar yaz koçum")
    