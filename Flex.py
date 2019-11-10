def Flex_output(text):
    flex = {
  "type": "flex",
  "altText": "Flex Message",
  "contents": {
    "type": "bubble",
    "direction": "ltr",
    "hero": {
      "type": "image",
      "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQDYswiR8z_eWmSf2Y3e7N7knq6BuxG56r78NnhZJzupyANAHMq",
      "size": "full",
      "aspectRatio": "1.51:1",
      "aspectMode": "fit"
    },
    "body": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "text",
          "text": "แปลว่า...",
          "size": "xxl",
          "align": "start",
          "weight": "bold"
        },
        {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "spacer",
              "size": "lg"
            },
            {
              "type": "text",
              "text": text,
              "size": "sm",
              "align": "center",
              "gravity": "center",
              "weight": "regular",
              "wrap": True
            }
          ]
        },
        {
          "type": "separator",
          "margin": "lg",
          "color": "#4253B9"
        }
      ]
    },
    "footer": {
      "type": "box",
      "layout": "horizontal",
      "contents": [
        {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "button",
              "action": {
                "type": "message",
                "label": "แปลข้อความใหม่",
                "text": "แปลข้อความใหม่"
              },
              "color": "#2134D2",
              "height": "sm",
              "style": "primary"
            },
            {
              "type": "button",
              "action": {
                "type": "message",
                "label": "ออกจากการแปล",
                "text": "ออกจากการแปล"
              },
              "margin": "md",
              "height": "sm",
              "style": "secondary"
            }
          ]
        }
      ]
    }
  }
}
    return flex