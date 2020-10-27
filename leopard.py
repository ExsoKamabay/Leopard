from source import *
class Leopard(Leopard_options):
    def __init__(self):
        Leopard_options().banner();
    def leopard(self):
        setattr(self,"b",(cs(decor("star9"),super().rand_color())));
        print(getattr(self,"b")+">"+getattr(self,"b")+">"+
        getattr(self,"b")+">"+getattr(self,"b")+">"+getattr(self,"b")+">");
        setattr(self,"q",(input(getattr(self,"b")+">\n"+getattr(self,"b")+"> ")));
        setattr(self,"l",(getattr(self,"q").split()));
        if not getattr(self,"q"):
            print(cs(text2art("KOSONG","bear"),
            super().rand_color()));self.leopard();
        elif getattr(self,"q") == str("help"):
            super().banner();super().lhelp();self.leopard();
        elif getattr(self,"l")[0] == str("search"):
            super().gitsearch(getattr(self,"l")[1]);
            self.leopard();
        elif getattr(self,"l")[0] == str("execute"):
            if getattr(self,"l")[1] == str("portscan"):
                super().banner();
                super().nmap(getattr(self,"l")[2]);
                self.leopard();
            elif getattr(self,"l")[1] == str("ipgeo"):
                super().banner();
                super().ipwhois(getattr(self,"l")[2]);
                self.leopard();
            elif getattr(self,"l")[1] == str("mailspoof"):
                super().mailSpoof();
                Leopard().leopard();
            elif getattr(self,"l")[1] == str("adbtrack"):
                super().banner();
                super().adbtrack();
                self.leopard();
            else:Leopard().leopard();
        else:super().lxban();

__name__==Leopard().leopard()