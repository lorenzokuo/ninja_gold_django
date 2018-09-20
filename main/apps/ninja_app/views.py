from django.shortcuts import render, redirect
from time import gmtime, strftime
import random

def index(request):
    if "gold" not in request.session:
        request.session["gold"] = 0
    
    return render(request, "ninja_app/index.html")

def process(request):
    msgLost = ""
    msg = ""
    color = ""
    if request.POST["building"] == "farm":
        gold_num = random.randrange(10,20)
        msg = "Earned " + str(gold_num) + " golds from the farm!"
        color = "earned"
        request.session["gold"] += gold_num
    if request.POST["building"] == "cave":
        gold_num = random.randrange(5,10)
        msg = "Earned " + str(gold_num) + " golds from the cave!"
        color = "earned"
        request.session["gold"] += gold_num
    if request.POST["building"] == "house":
        gold_num = random.randrange(2,5)
        msg = "Earned " + str(gold_num) + " golds from the house!"
        color = "earned"
        request.session["gold"] += gold_num
    if request.POST["building"] == "casino":
        gold_num = random.randrange(-50,50)
        if gold_num >= 0:
            msg = "Earned " + str(gold_num) + " golds from the casino!"
            color = "earned"
            request.session["gold"] += gold_num
        else:
            msgLost = "Lost " + str(gold_num) + " golds from the casino!"
            color = "lost"
        request.session["gold"] += gold_num

    if "dialog" not in request.session:
        request.session["dialog"] = []
    temp_list = request.session["dialog"]
    temp_list.append({
        "color" : color,
        "msgLost" : msgLost,
        "msg" : msg,
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
        })
    request.session["dialog"] = temp_list
    return redirect("/")

def reset(request):
    request.session.clear()
    return redirect("/")