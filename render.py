from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
S=2
im=Image.new('RGB',(1024*S,1024*S),'#f7eedb'); d=ImageDraw.Draw(im)
def box(b,fill,outline=None,w=3,r=0):
 b=tuple(int(v*S) for v in b)
 if r:d.rounded_rectangle(b,r*S,fill,outline,w*S)
 else:d.rectangle(b,fill,outline,w*S)
def line(p,c='#203842',w=4):d.line([(int(x*S),int(y*S)) for x,y in p],fill=c,width=w*S)
def ellipse(b,f,o=None,w=3):d.ellipse(tuple(int(v*S) for v in b),f,o,w*S)
def text(t,xy,size,fill='#203842',center=False):
 f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',size*S)
 d.text((xy[0]*S,xy[1]*S),t,font=f,fill=fill,anchor='mt' if center else 'lt')
# headline
text('WE NEED TO TALK', (512,38),67,center=True)
text('ABOUT YOUR PROMPTS.',(512,119),62,center=True)
box((38,222,986,984),'#e5dac4',r=24)
# office window and chart-free architectural details
box((84,260,380,549),'#a7d6d5','#203842',5,12)
line([(232,263),(232,546)]);line([(87,405),(377,405)])
box((86,497,377,546),'#8ab8b6')
# boss chair
box((582,295,891,689),'#203842',r=55)
box((600,312,873,660),'#3a5660',r=44)
# robot suit and head
box((595,492,875,731),'#698e99','#203842',5,45)
box((655,459,796,535),'#b9d4d3','#203842',4,15)
box((605,315,848,485),'#d7e8e3','#203842',6,35)
box((625,348,827,431),'#203842',r=20)
ellipse((653,375,676,398),'#82f4ce');ellipse((777,375,800,398),'#82f4ce')
line([(703,454),(751,454)],'#203842',5)
line([(726,315),(726,287)],w=5);ellipse((714,270,738,294),'#e6ab51','#203842')
# tie and lapels
d.polygon([(655*S,505*S),(726*S,548*S),(686*S,600*S)],fill='#e7eeea')
d.polygon([(796*S,505*S),(726*S,548*S),(767*S,600*S)],fill='#e7eeea')
d.polygon([(726*S,539*S),(746*S,563*S),(738*S,641*S),(715*S,641*S),(706*S,563*S)],fill='#d86b4e')
# anxious human, hunched in visitor chair
box((111,659,334,906),'#bf7155','#203842',5,25)
box((153,565,366,826),'#e7b65d','#203842',5,50)
ellipse((179,408,321,570),'#efbb93','#203842',5)
d.pieslice((175*S,392*S,325*S,514*S),180,355,fill='#473b37')
ellipse((277,468,287,480),'#203842')
line([(265,452),(293,459)],w=4)
line([(276,521),(297,513)],w=4)
# sweat
ellipse((324,455,336,480),'#69afbf')
# desk
box((361,663,951,913),'#c47f50','#203842',5,12)
box((345,644,966,688),'#e3ad70','#203842',5,12)
line([(401,913),(401,959)],w=12);line([(916,913),(916,959)],w=12)
# arm sliding review toward employee
line([(831,558),(872,607),(701,642)],'#203842',40)
line([(831,558),(872,607),(701,642)],'#9ab9bd',29)
# document shown frontward, oversized for instant reading
box((363,704,940,939),'#fffdf5','#203842',5,10)
text('PERFORMANCE',(651,729),39,center=True)
text('IMPROVEMENT PLAN',(651,778),39,center=True)
line([(389,834),(914,834)],'#d86b4e',4)
text('prompt quality down 47%',(651,851),30,center=True)
text('this quarter',(651,890),30,center=True)
ellipse((674,620,734,654),'#c4dbd8','#203842',4)
# human hands clenched at desk edge
ellipse((329,639,382,677),'#efbb93','#203842',4)
im.resize((1024,1024),Image.Resampling.LANCZOS).save(Path(__file__).parent/'assets/entry.png',optimize=True)
