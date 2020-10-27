from source.src.pkg_import import * ;
class Leopard_scrap:
    def page1(self,query):
        setattr(self,"urlq",["aHR0cDovL2dpdGh1Yi5jb20vc2VhcmNoP3E9JXM"])
        dt = {
            "results":[],
            "page1":{
                "url_git":[],
                "url_zip":[],
                "title":[],
                "like":[],
                "lang":[],
                "update":[],
            },
        };
        setattr(self,"query",query.replace(" ","+"));
        setattr(self,"url0",(decode(getattr(self,"urlq")[0])%(getattr(self,"query"))));
        setattr(self,"req0",(get(getattr(self,"url0")).content));
        setattr(self,"sup0",(BeautifulSoup(getattr(self,"req0"),"html.parser")));
        for p1_url in getattr(self,"sup0").findAll("a",{"class":"v-align-middle"}):
            dt["page1"]["url_git"].append("https://github.com"+p1_url["href"]+".git");
            dt["page1"]["url_zip"].append("https://github.com"+p1_url["href"]+"/archive/master.zip");
        for p1_lng in getattr(self,"sup0").findAll("span",{"itemprop":"programmingLanguage"}):
            dt["page1"]["lang"].append(p1_lng.text.strip());
        for p1_pgf in getattr(self,"sup0").findAll("p",{"class":"mb-1"}):
            dt["page1"]["title"].append(p1_pgf.text.strip());
        for p1_dte in getattr(self,"sup0").findAll("relative-time",{"class":"no-wrap"}):
            dt["page1"]["update"].append(p1_dte["datetime"]);
        for p1_lke in getattr(self,"sup0").findAll("a",{"class":"muted-link"}):
            dt["page1"]["like"].append(p1_lke.text.strip());
        for results in getattr(self,"sup0").findAll("div",{"class":"d-flex flex-column flex-md-row flex-justify-between border-bottom pb-3 position-relative"}):
            dt["results"].append(results.h3.text.strip());
        data = dumps(dt,indent=2,sort_keys=True);return loads(data);
    def page2(self,query):
        setattr(self,"urlq",
        ["aHR0cDovL2dpdGh1Yi5jb20vc2VhcmNoP3A9MiZxPSVzJnJlZj1zaW1wbGVzZWFyY2gmdHlwZT1SZXBvc2l0b3JpZXM",
        "aHR0cDovL2dpdGh1Yi5jb20vc2VhcmNoP3A9MyZxPSVzJnJlZj1zaW1wbGVzZWFyY2gmdHlwZT1SZXBvc2l0b3JpZXM",
        "aHR0cDovL2dpdGh1Yi5jb20vc2VhcmNoP3A9NCZxPSVzJnJlZj1zaW1wbGVzZWFyY2gmdHlwZT1SZXBvc2l0b3JpZXM"]);
        dt = {
            "page2":{
                "url_git":[],
                "url_zip":[],
                "title":[],
                "like":[],
                "lang":[],
                "update":[],
                },
            "page3":{
                "url_git":[],
                "url_zip":[],
                "title":[],
                "like":[],
                "lang":[],
                "update":[],
                },
            "page4":{
                "url_git":[],
                "url_zip":[],
                "title":[],
                "like":[],
                "lang":[],
                "update":[],
                },
            };
        setattr(self,"query",query.replace(" ","+"));
        setattr(self,"url0",(decode(getattr(self,"urlq")[0])%(getattr(self,"query"))));
        setattr(self,"url1",(decode(getattr(self,"urlq")[1])%(getattr(self,"query"))));
        setattr(self,"url2",(decode(getattr(self,"urlq")[2])%(getattr(self,"query"))));
        setattr(self,"req0",(get(getattr(self,"url0")).content));
        setattr(self,"req1",(get(getattr(self,"url1")).content));
        setattr(self,"req2",(get(getattr(self,"url2")).content));
        setattr(self,"sup0",(BeautifulSoup(getattr(self,"req0"),"html.parser")));
        setattr(self,"sup1",(BeautifulSoup(getattr(self,"req1"),"html.parser")));
        setattr(self,"sup2",(BeautifulSoup(getattr(self,"req2"),"html.parser")));
        for p2_url ,p3_url ,p4_url in zip(
            getattr(self,"sup0").findAll("a",{"class":"v-align-middle"}),
            getattr(self,"sup1").findAll("a",{"class":"v-align-middle"}),
            getattr(self,"sup2").findAll("a",{"class":"v-align-middle"})):
                dt["page2"]["url_git"].append("https://github.com"+p2_url["href"]+".git");
                dt["page3"]["url_git"].append("https://github.com"+p3_url["href"]+".git");
                dt["page4"]["url_git"].append("https://github.com"+p4_url["href"]+".git");
                dt["page2"]["url_zip"].append("https://github.com"+p2_url["href"]+"/archive/master.zip");
                dt["page3"]["url_zip"].append("https://github.com"+p3_url["href"]+"/archive/master.zip");
                dt["page4"]["url_zip"].append("https://github.com"+p4_url["href"]+"/archive/master.zip");
        for p2_lng ,p3_lng ,p4_lng in zip(
            getattr(self,"sup0").findAll("span",{"itemprop":"programmingLanguage"}),
            getattr(self,"sup1").findAll("span",{"itemprop":"programmingLanguage"}),
            getattr(self,"sup2").findAll("span",{"itemprop":"programmingLanguage"})):
                dt["page2"]["lang"].append(p2_lng.text.strip());
                dt["page3"]["lang"].append(p3_lng.text.strip());
                dt["page4"]["lang"].append(p4_lng.text.strip());
        for p2_pgf ,p3_pgf ,p4_pgf in zip(
            getattr(self,"sup0").findAll("p",{"class":"mb-1"}),
            getattr(self,"sup1").findAll("p",{"class":"mb-1"}),
            getattr(self,"sup2").findAll("p",{"class":"mb-1"})):
                dt["page2"]["title"].append(p2_pgf.text.strip());
                dt["page3"]["title"].append(p3_pgf.text.strip());
                dt["page4"]["title"].append(p4_pgf.text.strip());
        for p2_dte ,p3_dte ,p4_dte in zip(
            getattr(self,"sup0").findAll("relative-time",{"class":"no-wrap"}),
            getattr(self,"sup1").findAll("relative-time",{"class":"no-wrap"}),
            getattr(self,"sup2").findAll("relative-time",{"class":"no-wrap"})):
                dt["page2"]["update"].append(p2_dte["datetime"]);
                dt["page3"]["update"].append(p3_dte["datetime"]);
                dt["page4"]["update"].append(p4_dte["datetime"]);
        for p2_lke ,p3_lke ,p4_lke in zip(
            getattr(self,"sup0").findAll("a",{"class":"muted-link"}),
            getattr(self,"sup1").findAll("a",{"class":"muted-link"}),
            getattr(self,"sup2").findAll("a",{"class":"muted-link"})):
                dt["page2"]["like"].append(p2_lke.text.strip());
                dt["page3"]["like"].append(p3_lke.text.strip());
                dt["page4"]["like"].append(p4_lke.text.strip());
        data = dumps(dt,indent=2,sort_keys=True);return loads(data);
    