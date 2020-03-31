import time
from datetime import datetime
from gtts import gTTS
import os
months=[31,28,31,30,31,30,31,30,31,31,30,31,31]
h=0
m=0
s=0
crd=datetime.now().day
crm=datetime.now().month
cry=datetime.now().year
bd=int(input())
bm=int(input())
by=int(input())
cy=0
cm=0
cd=0
count=0
days=0
if bd > crd : 
    crd=crd+months[bm-1]
    crm=crm-1
if bm > crm :
    cry=cry-1
    crm=crm+12
cd=crd-bd 
cm=crm-bm
cy=cry-by
days=cy*365
i=1
while(i<=cm):
    days+=months[i-1]
    i=i+1
days+=cd
b1=0
b1=by
while(b1 <= cry):
   if b1%4==0 and b1%100!=0 or b1%400==0:
    count+=1
   b1+=1
days+=count
print("Present Age Years:",cy)
print("number of months",cy*12+cm)
print ("no.of days:",days)
h=0
m=0
s=0
h=days*24
m=h*60
s=m*60
print("hours",h)
print("minutes",m)
print("seconds",s)
cy = by-1900
cy = cy/4
cy = cy+by-1900
if bm==1 or bm==10 :
   cm = 1
elif bm==2 or bm==3 or bm==11:
   cm = 4
elif bm==7 or bm==4:
	cm = 0
elif bm== 5:
    cm = 2
elif bm==6:
    cm = 5
elif bm==8:
    cm = 3
elif bm== 9 or bm==12:
	cm = 6
cy = cy + cm
cy = cy+ bd
if (by>1900) and (by%4==0) and (bm<2):
 cy=cy-1
cd=cy%7
cd=int(cd)
if cd==0:
   print("Day is SATURDAY")
elif cd==1:
    print("Day is SUNDAY")
elif cd==2:
    print("Day is MONDAY")
elif cd==3:
    print("Day is TUESDAY")
elif cd==4:
    print("Day is WEDNESDAY")
elif cd==5:
    print("Day is THURSDAY")
elif cd==6:
    print("Day is FRIDAY")
if bm == 12:
	astro_sign = 'Sagittarius' if (bd < 22) else 'capricorn'
elif bm == 1:
	astro_sign = 'Capricorn' if (bd < 20) else 'aquarius'
elif bm == 2:
	astro_sign = 'Aquarius' if (bd < 19) else 'pisces'
elif bm == 3:
	astro_sign = 'Pisces' if (bd < 21) else 'aries'
elif bm ==4:
	astro_sign = 'Aries' if (bd < 20) else 'taurus'
elif bm == 5:
	astro_sign = 'Taurus' if (bd < 21) else 'gemini'
elif bm == 6:
	astro_sign = 'Gemini' if (bd < 21) else 'cancer'
elif bm == 7:
	astro_sign = 'Cancer' if (bd < 23) else 'leo'
elif bm == 8:
	astro_sign = 'Leo' if (bd < 23) else 'virgo'
elif bm == 9:
	astro_sign = 'Virgo' if (bd < 23) else 'libra'
elif bm == 10:
	astro_sign = 'Libra' if (bd < 23) else 'scorpio'
elif bm == 11:
	astro_sign = 'scorpio' if (bd < 22) else 'sagittarius'
print("Your Astrological sign is :",astro_sign)
if bm==1:
    mytext="If you were born in January, you are ruled by the number 1.You are independent, analytic, and a born leader. You need to stand out from the crowd and are known for your creativity, ingenuity, and ability to make things happen. Chances are you will lead a more traditional life than others.Stubborn. Ambitious and serious. Loves to teach and be taught. Never looks at peoples flaws or weaknesses. Hardworking and productive. Smart, neat and organized. Sensitive and has deep thoughts. Knows how to make others happy. Quiet unless excited or tense. Rather reserved. Highly attentive. Resistant to illnesses but prone to colds. Loving and loyal. Loves children. Has great social abilities. Money cautious, can budget successfully."
elif bm==2:
     mytext="Abstract thoughts. Loves reality and abstract. Intelligent and clever. Changing personality. Attractive. Temperamental. Quiet, shy and humble. Honest and loyal. Determined to reach goals. Loves freedom. Rebellious when restricted. Loves aggressiveness. Too sensitive and easily hurt. Gets angry really easily but does not show it. Dislike unnecessary things. Loves making friends but rarely shows it. Daring and stubborn. Ambitious. Realizing dreams and hopes. Sharp. Loves entertainment and leisure. Romantic on the inside not outside. Superstitious and ludicrous. Spendthrift."
elif bm==3:
    mytext=" Attractive personality. Affectionate. Shy and reserved. Secretive. Naturally honest, generous and sympathetic. Loves peace and serenity. Sensitive to others. Loves to serve others. Easily angered. Trustworthy. Appreciative and returns kindness. Observant and assesses others. Revengeful. Loves to dream and fantasize. Loves traveling. Loves attention. Hasty decisions in choosing partners. Loves home decor. Musically talented. Loves special things. Moody.You have an ability to make a lot of money, but also lose it just as quickly."
elif bm==4:
     mytext="You may be perceived as being stubborn, bossy, and impulsive. On the other hand, you are also very creative and intelligent. You are a born leader who is very ambitious and your natural charisma will have you attracting many friends . Once you apply yourself, nothing stops you from achieving your goal.Active and dynamic. Decisive and hastey but tends to regret. Attractive and affectionate to oneself. Strong mentality. Loves attention. Diplomatic. Consoling, friendly and solves peoples problems. Brave and fearless. Adventurous. Loving and caring. Suave and generous. Emotional. Aggressive. Hasty. Good memory. Moving Motivates oneself and others."
elif bm==5:
    mytext=" Self expression may be important to you and you may be a talented musician, actor, or writer. You have a high respect for authority. You value your friends above anything else and spend a lot of time socializing. Time spent alone in nature is very good for helping you find your balance.Stubborn and hard-hearted. Strong-willed and highly motivated. Sharp thoughts. Easily angered. Attracts others and loves attention. Deep feelings. Beautiful physically and m entally. Firm Standpoint. Needs no motivation. Easily consoled. Systematic (left brain). Loves to dream. Strong clairvoyance. Understanding. Sickness usually in the ear and neck. Good imagination. Good physical. Weak breathing. Loves literature and the arts. Loves traveling. Dislike being at home. Restless. Not having many children. Hardworking. High spirited. Spendthrift."
elif bm==6:
    mytext="  You are a very romantic individual, but also a very jealous one. You are also very sensual and a fantastic lover. Your love life tends to be very complex and it is easy for your sign to get too hung up on the past. A career in the creative arts suits you best. you are a very kind hearted and philanthropic individual. You do not like children, but older relatives in your family mean a lot to you. Easily influenced by kindness. Polite. Has lots of ideas. Sensitive. Active mind. Hesitates, tends to put things off. Choosy and always wants the best. Temperamental. Funny and humorous. Loves to joke. Good debating skills. Talkative. Daydreamer. Friendly. Makes friends easily. Shows character. Easily hurt. Prone to getting colds. Easily bored. Fussy and stubborn. Seldom shows emotions. Takes time to recover when hurt. Brand conscious."
elif bm==7:
    mytext=" You are a sincere, candid, and sympathetic individual. You care deeply for your family and will go to great lengths to maintain and protect your relationships. People born in this birth month can be very eccentric, especially when it comes to the way they dress and some of their lifestyle habits. Many people born in July are geniuses, but they are also very sensitive and prone to depression.Fun to be with. Secretive. Sometimes difficult to understand. Quiet unless excited or tense. Takes pride in oneself. Has reputation for hard work. Honest. Concerned about peoples feelings. Tactful. Friendly, but not always approachable. Emotionally temperamental. Moody and easily hurt. Witty. Not mean or revengeful. Forgiving but never forgets. Dislikes nonsensical and illogical things. Sensitive and forms friendships carefully. Caring and loving. Treats others equally. Wary and sharp. Judges people through observations. No difficulties in studying. Loves to be alone. Broods about the past and misses old friends. Has difficulty making new friends. Prone to having dieting problems. Easily hurt but takes long to recover."
elif bm==8:
    mytext=" You are destined to become a pillar of the community. You are a loving,  strives to see the good in everyone. Often you are known for your philanthropy, team spirit, and ability to inspire others to be the very best that they can be in life. Money comes to you very easily.Loves to joke. Attractive. Suave and caring. Brave and fearless. Firm and has leadership qualities. Knows how to console others. Too generous and egoistic. Takes high pride of oneself. Thirsty for praises. Extraordinary spirit. Easily angered. Angry when provoked. Easily jealous. Observant. Careful and cautious. Thinks quickly. Independent thoughts. Loves to lead and to be led. Loves to dream. Talented in the arts, music and defense. Sensitive but not petty. Learns to relax. Hasty and trusty. Loving and caring. Loves to make friends."
elif bm==9:
    mytext="You are destined to play many roles in your lifetime because you are so intelligent and flexible. You are also very organized. You are highly intelligent and spiritual, but tend to take adversity very personally. Your biggest weakness is becoming depressed. In order to succeed, you need to turn off the voice of your inner critic sometimes. A tendency to over analyze situations can also get you into trouble.Suave and compromising. Careful, cautious and organized. Stubborn. Quiet. comfortable if have to talk to a group. Calm. Sympathetic. Concerned and detailed. Loyal. Does work well. Very confident. Sensitive. Thinking generous. Good memory. Clever and knowledgeable. Loves to look for information. Must control oneself when criticizing. Able to motivate oneself. Understanding. Secretive. Loves sports and leisure Hardly shows emotions. Tends to bottle up feelings. Very choosy, especially in relationships."
elif bm==10:
    mytext=" You are naturally very lucky. When you decide on a goal, you almost always meet it. If you can deal with your inner demons, you can succeed beyond your wildest dreams in life. You have the potential to be a well known leader in your field.Loves to chat. Loves those who loves them. Loves to takes things at the center. Inner and physical beauty. Gets angry often. Treats friends importantly. Always making new friends. Easily hurt but recovers easily. Day dreamer. Loyal. Opinionated. Does not care of what others think. Emotional. Decisive. Strong clairvoyance. Loves to travel, the arts and literature. Touchy and easily jealous. Honest, does not pretend. Concerned. Loves outdoors. Just and fair. Spendthrift. Easily influenced. Easily loses confidence. Loves children."
elif bm==11:
    mytext=" You are psychic, empathic, and positive. However, sometimes you get overwhelmed by your own sensitivity and develop stress related health and psychological problems, such as chronic fatigue and depression. You often set an example for others and make a great teacher.Has a lot of ideas. Thinks forward. Unique and brilliant. Extraordinary ideas. Sharp thinking. Fine and strong clairvoyance. Can become good doctors. Dynamic in personality. Secretive. Inquisitive. Knows how to dig secrets. Always thinking. Less talkative but amiable. Brave and generous. Patient. Stubborn and hard-hearted. If there is a will, there is a way. Determined. Never give up. Hardly becomes angry unless provoked. Loves to be alone. Thinks differently from others. Sharp-minded. Motivates oneself. Does not appreciate praises. High-spirited. Well-built and toug! h. Deep love and emotions. Romantic. Uncertain in relationships. Homely. Hardworking. High abilities. Trust worthy. Honest and keeps secrets. Not able to control emotions."
elif bm==12:
    mytext=" You are a practical philosopher who values a stable lifestyle. You are also unusually lucky and wealth and love find you easily. You also have an active social life, but to the extent that you sometimes ignore your responsibilities. The danger is that you consider yourself to be so lucky that you take dangerous risks sometimes. The key to success for people born in this month is to realize that they are not immortal.Loyal and generous. Sexy. Patriotic. Active in games and interactions. Impatient and hasty. Ambitious. Influential in organizations. Fun to be with. Loves to socialize. Loves praises. Loves attention. Loves to be loved. Honest and trustworthy.. Not pretending. Short tempered. Changing personality. Not egotistic. Takes high pride in oneself. Hates restrictions."
if bm==1:
   mytext=mytext+"your lucky colour is DARK RED"
elif bm==2:
    mytext=mytext+"your lucky colour is PURPLE"
elif bm==3:
    mytext=mytext+"your lucky colour is PALE BLUE"
elif bm==4:
    mytext=mytext+"your lucky colour is COLOURLESS"
elif bm==5:
    mytext=mytext+"your lucky colour is BRIGHT GREEN"
elif bm==6:
    mytext=mytext+"your lucky colour is CREAM"
elif bm==7:
    mytext=mytext+"your lucky colour is RED"
elif bm==8:
    mytext=mytext+"your lucky colour is PALE GREEN"
elif bm==9:
    mytext=mytext+"your lucky colour is DEEP BLUE"
elif bm==10:
    mytext=mytext+"your lucky colour is VARIEGATED"
elif bm==11:
    mytext=mytext+"your lucky colour is YELLOW"
elif bm==12:
    mytext=mytext+"your lucky colour is SKY BLUE"
lang='en'
output=gTTS(text=mytext,lang=lang,slow=False)
output.save("output7.mp3")
os.system("start output7.mp3")
