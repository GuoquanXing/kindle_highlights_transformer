# Introduction

This script helps transform highlights and notes file `My Clippings.txt` exported from your kindle to a json file and save it as `data.json` at your current folder by default.

## Usage

**Python 2.x is not supported, please use python 3.x instead.**

`python3 parse_kindle_ntoes.py 'FILE_PATH' [TARGET_PATH]`

## Sample

Below is a sample transformed JSON file:
```JSON
{
    "contents": [{
            "bookName": "围城 (钱钟书)",
            "notes": [{
                    "note": "“天下只有两种人。譬如一串葡萄到手，一种人挑最好的先吃，另一种人把最好的留在最后吃。照例第一种人应该乐观，因为他每吃一颗都是吃剩的葡萄里最好的；第二种应该悲观，因为他每吃一颗都是吃剩的葡萄里最坏的。不过事实上适得其反，缘故是第二种人还有希望，第一种人只有回忆。”从恋爱到白头偕老，好比一串葡萄，总有最好的一颗，最好的只有一颗，留着做希望，多么好？",
                    "timestamp": "添加于 2018年4月1日星期日 下午9:24:11",
                    "location": "- 您在位置 #3628-3631的标注"
                },
                {
                    "note": "一个人应该得意，得意的人谈话都有精彩，譬如辛楣。自己这一年来，牢骚满腹，一触即发；因为一向不爱听人家发牢骚，料想人家也未必爱听自己的牢骚，留心管制，像狗戴了嘴罩，谈话都不痛快",
                    "timestamp": "添加于 2018年4月1日星期日 下午9:42:07",
                    "location": "- 您在位置 #3788-3789的标注"
                }
            ]
        },
        {
            "bookName": "Name",
            "notes": [{
                    "note": "I Love You",
                    "timestamp": "Gakki 9:42:07",
                    "location": "- 您在位置 #3788-3789的标注"
                },
                {
                    "note": "I Love You",
                    "timestamp": "Stefanie 9:42:07",
                    "location": "- 您在位置 #3788-3789的标注"
                }
            ]
        }
    ],
    "title": "Kindle Notes and Highlights"
}
```