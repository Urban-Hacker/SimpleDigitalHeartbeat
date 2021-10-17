# Simple service to check the status:
import os

from config import *


class HtmlPage:

    def __init__(self, file):
        self._html = open(file, "r").read()

    def add_data(self, key, data):
        if (key == "popup"):
            data = self._gen_popup(data)
        self._html = self._html.replace("[[" + key + "]]", data)

    def _gen_popup(self, data):
        if data == "":
            return data
        return '<div class="section alert">' + data + '</div>'

    def get_html(self):
        return self._html


class HtmlRender:

    def status(service, result):
        page = HtmlPage("templates/entry.html")
        page.add_data("service", service)
        state = "ok"
        if result != 0:
            state = "fail"
        page.add_data("state", state)
        return page.get_html()

    def text(section):
        page = HtmlPage("templates/section.html")
        page.add_data("title", section["title"])
        page.add_data("content", "<tr><td>" + section["desc"] + "</td></tr>")
        return page.get_html()

    def tests(section):
        global g_errors
        tests = section["tests"]
        page = HtmlPage("templates/section.html")
        page.add_data("title", section["title"])
        html = ""
        error = 0
        for test in tests:
            a = os.system(test["cmd"])
            if a > 0:
                error += 1
            html += HtmlRender.status(test["name"], a)
        g_errors += error

        page.add_data("content", html)
        if error > 0:
            page.add_data("state", "alert")
        else:
            page.add_data("state", "allclear")
        return page.get_html()

    def graph():
        try:
            historicaldata = open("old.db", "r").read().replace(
                "[", "").replace("]", "").split(",")
        except:
            a = open("old.db", "w")
            a.write(str([]))
            historicaldata = []

        # Padding
        graph = ""
        if len(historicaldata) < config["history"]:
            for i in range(0, config["history"] - len(historicaldata)):
                graph += '<abbr title="(No data)"><span class="square"></span></abbr>'

        newdata = []

        for i in historicaldata:
            i = int(i)
            newdata.append(i)
            if i > 0:
                graph += '<abbr title="('
                graph += str(i) + \
                    ' outage(s) detected)"><span class="square dot-fail"></span></abbr>'
            else:
                graph += '<abbr title="(No outages)"><span class="square dot-ok"></span></abbr>'

        newdata.append(g_errors)

        if len(newdata) > config["history"]:
            newdata = newdata[-config["history"]:]

        a = open("old.db", "w")
        a.write(str(newdata))

        return graph


page = HtmlPage("templates/main.html")
page.add_data("title", config["title"])
page.add_data("desc", config["desc"])


g_errors = 0
html = ""
for section in config["sections"]:
    sectionhtml = ""
    if section["type"] == "tests":
        sectionhtml = HtmlRender.tests(section)
    if section["type"] == "text":
        sectionhtml = HtmlRender.text(section)
    html += sectionhtml

page.add_data("graph", HtmlRender.graph())

if g_errors > 0:
    page.add_data("popup", config["popup"])
else:
    page.add_data("popup", '')

page.add_data("content", html)
with open("status.html", "w") as status_out:
    status_out.write(page.get_html())
