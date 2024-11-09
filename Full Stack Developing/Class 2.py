from flask import *
cards=[
    {"image":"https://m.media-amazon.com/images/I/717Ibv0mpzL._AC_SX466_.jpg",
    "title":"CyberPowerPC Gamer Xtreme VR Gaming PC",
    "description":"Intel Core i9-14900KF 3.2GHz, GeForce RTX 4070 Super 12GB, 32GB DDR5, 2TB PCIe Gen4 SSD, WiFi Ready & Windows 11 Home (GXiVR8080A38)"},

    {"image":"https://m.media-amazon.com/images/I/71RTruFctrL.__AC_SX300_SY300_QL70_FMwebp_.jpg",
    "title":"PHILIPS 22 inch Class Thin Full HD (1920 x 1080) Monitor",
    "description":"100Hz Refresh Rate, VESA, HDMI x1, VGA x1, LowBlue Mode, Adaptive Sync, 4 Year Advance Replacement Warranty, 221V8LB"}
    ]

app=Flask("__name__")

@app.route("/")
def display():
    return render_template("index2.html",details=cards)

if __name__=="__main__":
    app.run(debug=True)