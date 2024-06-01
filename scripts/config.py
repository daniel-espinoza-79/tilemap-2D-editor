from scripts.utils import load_image

assets ={
    'BLOCK':{
            "WALL":{
                "subtype":"WALL",
                "image":load_image('elements/touchable/block/wall.png', 50, 50),
                "size":(50,50)
            },
            "OVERWORLD":{
                "subtype":"OVERWORLD",
                "image":load_image('elements/touchable/block/overworld.png', 50, 50),
                "size":(50,50)
            }
    }
    ,
    'PIPE': {
        "SMALL_PIPE":{   
            "subtype":"SMALL_PIPE",
            "image":load_image('elements/touchable/pipe/small-pipe.png',150,250),
             "size":(150,250)
        },
        "MEDIUM_PIPE":{
            "subtype":"MEDIUM_PIPE",
            "image":load_image('elements/touchable/pipe/medium-pipe.png',150,350),
             "size":(150,350)
        },
        "BIG_PIPE":{
            "subtype":"BIG_PIPE",
            "image":load_image('elements/touchable/pipe/big-pipe.png',150,450),
             "size":(150,450)
        }
    },
    'CLOUD':{
        "SMALL_CLOUD":{
            "subtype":"SMALL_CLOUD",
            "image":load_image('elements/non_touchable/cloud/small-cloud.png', 150, 100),
            "size":(150,100)
        },
        "MEDIUM_CLOUD":{
            "subtype":"MEDIUM_CLOUD",
            "image":load_image('elements/non_touchable/cloud/medium-cloud.png', 300, 250),
            "size":(300,250)
        },
        "BIG_CLOUD":{
            "subtype":"BIG_CLOUD",
            "image":load_image('elements/non_touchable/cloud/big-cloud.png', 400, 300),
            "size":(400,300)
        }
    }
}
