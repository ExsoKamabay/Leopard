from source.src.pkg_import import * ;
from source.src.poc import Leopard_scrap ;
class Leopard_options(Leopard_scrap):
    def rand_color(self):
        return choice([
            "#ff00ff","#40ff00","#00ffbf","#0080ff","#8000ff","#ff00ff"]);
    def ipwhois(self,query):
        setattr(self,"urlq",(decode("aHR0cHM6Ly9pcHdob2lzLmFwcC9qc29uLyVz")));        
        setattr(self,"setq",(getattr(self,"urlq")%(query)));
        setattr(self,"getq",(get(getattr(self,"setq")).json()));
        print(cs(dumps(getattr(self,"getq"),indent=2,sort_keys=True),self.rand_color()));
    def banner(self):
        with open("source/src/xban.txt","r") as f:
            print(cs(f.read(),self.rand_color()));
    def lxban(self):
        print(cs(text2art("leopard","merlin2"),self.rand_color()));
    def adbtrack(self):
        with open("source/shodan_apikey.cfg","r") as api:
            setattr(self,"config",(Shodan(api.readlines())));
            for s in getattr(self,"config").search("android debug bridge")["matches"]:
                setattr(self,"lt",(str(s["location"]["latitude"])));
                setattr(self,"lg",(str(s["location"]["longitude"])));
                android_controller.connect((s["ip_str"]));
                android_controller.checkConnections()
                print(cs(
                    "Country : "+s["location"]["country_name"]+"   "+
                    "Location : "+getattr(self,"lt")+","+
                    getattr(self,"lg"),"#0080ff"));
    def mailSpoof(self):
        setattr(self,"target",(
            decode("aHR0cHM6Ly9rYW1hYmF5LjAwMHdlYmhvc3RhcHAuY29tLyVz")%(
            decode("ZXhzb2thbWFiYXlfbWFpbHNwb29mZXIteHRvb2xzL2luZGV4LnBocA"))));
        create_window("Mail-Spoofed",getattr(self,"target"),min_size=(1000,650));start();
    def gitsearch(self,query):
        setattr(self,"page_1",(super().page1(query)["page1"]));
        try:
            for uzip,ugit,lang,date,dec,like in zip(
                getattr(self,"page_1")["url_zip"],getattr(self,"page_1")["url_git"],
                getattr(self,"page_1")["lang"],getattr(self,"page_1")["update"],
                getattr(self,"page_1")["title"],getattr(self,"page_1")["like"]):
                print(cs(str(
                    text2art("leopard","lalia",True,"arrow_wave2")+"\n\n"+
                    "git :- "+ugit+"\nzip :- "+uzip+"\n"+
                    "languange:-"+lang+"  :-"+date+"  :-"+
                    like.strip('need help').replace('\n','')+"\n"+dec+"\n"
                ),self.rand_color()));
        except:print(cs(text2art("query not found!","lalia"),self.rand_color()));
    def lhelp(self):
        print(cs(
            "input : <mode>  <query>\n"+
            "mode  : <search  or  execute>\n"+
            "execute mode >  mailspoof, adbtrack, ipgeo <targetIP>, portscan <targetIP>\n"+
            "search mode >  enter the name you are looking for\n\n"+
            "example :\n"+"search 'tools pentesting'\nexecute ipgeo 127.0.0.1\nexecute adbtrack",
            self.rand_color()));
    def nmap(self,host):
        setattr(self,"hst",(Nmap().scan_top_ports(host,default=15)));
        try:
            for i in getattr(self,"hst")[str(host)]:
                print(cs(text2art("leopard","fancy5",True,"block1"),"#8000ff"));
                print(cs(text2art(str(
                    i["protocol"]+" "+i["host"]+":"+i["portid"]+"\n"+
                    i["reason"]+" "+i["reason_ttl"]+" "+i["state"]+"\n"+
                    i["service"]["conf"]+" "+i["service"]["method"]+" "+
                    i["service"]["name"])+"\n","lalia"),"#40bf80"));
        except:print(cs(text2art(f"Host Name Invalid! {host}","lalia"),self.rand_color()));
    