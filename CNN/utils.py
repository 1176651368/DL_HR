vgg_model_urls = {
    '11': 'https://download.pytorch.org/models/vgg11-8a719046.pth',
    '13': 'https://download.pytorch.org/models/vgg13-19584684.pth',
    '16': 'https://download.pytorch.org/models/vgg16-397923af.pth',
    '19': 'https://download.pytorch.org/models/vgg19-dcbb9e9d.pth',
    '11_bn': 'https://download.pytorch.org/models/vgg11_bn-6002323d.pth',
    '13_bn': 'https://download.pytorch.org/models/vgg13_bn-abd245e5.pth',
    '16_bn': 'https://download.pytorch.org/models/vgg16_bn-6c64b313.pth',
    '19_bn': 'https://download.pytorch.org/models/vgg19_bn-c79401a0.pth',
}

LAYER_PARAMS_DICT = {

    'resnet': {18: [{"BasicBlock": [[64, 64], [64, 64]], 'down_sample': False},
                    {"BasicBlock": [[64, 128], [128, 128]], 'down_sample': True},
                    {"BasicBlock": [[128, 256], [256, 256]], 'down_sample': True},
                    {"BasicBlock": [[256, 512], [512, 512]], 'down_sample': True},
                    ],
               34: [{"BasicBlock": [[64, 64]] + [[64, 64]] * 2, 'down_sample': False},
                    {"BasicBlock": [[64, 128]] + [[128, 128]] * 3, 'down_sample': True},
                    {"BasicBlock": [[128, 256]] + [[256, 256]] * 5, 'down_sample': True},
                    {"BasicBlock": [[256, 512]] + [[512, 512]] * 2, 'down_sample': True},
                    ],
               50: [{"BasicBlock": [[64, 64, 256], [256, 64, 256], [256, 64, 256]], 'down_sample': True,
                     'down_sample_stride': 1},
                    {"BasicBlock": [[256, 128, 512]] + [[512, 128, 512]] * 3, 'down_sample': True,
                     'down_sample_stride': 2},
                    {"BasicBlock": [[512, 256, 1024]] + [[1024, 256, 1024]] * 5, 'down_sample': True,
                     'down_sample_stride': 2},
                    {"BasicBlock": [[1024, 512, 2048]] + [[2048, 512, 2048]] * 2, 'down_sample': True,
                     'down_sample_stride': 2},
                    ],
               101: [{"BasicBlock": [[64, 64, 256], [256, 64, 256], [256, 64, 256]], 'down_sample': True,
                      'down_sample_stride': 1},
                     {"BasicBlock": [[256, 128, 512]] + [[512, 128, 512]] * 3, 'down_sample': True,
                      'down_sample_stride': 2},
                     {"BasicBlock": [[512, 256, 1024]] + [[1024, 256, 1024]] * 22, 'down_sample': True,
                      'down_sample_stride': 2},
                     {"BasicBlock": [[1024, 512, 2048]] + [[2048, 512, 2048]] * 2, 'down_sample': True,
                      'down_sample_stride': 2},
                     ],
               152: [{"BasicBlock": [[64, 64, 256], [256, 64, 256], [256, 64, 256]], 'down_sample': True,
                      'down_sample_stride': 1},
                     {"BasicBlock": [[256, 128, 512]] + [[512, 128, 512]] * 7, 'down_sample': True,
                      'down_sample_stride': 2},
                     {"BasicBlock": [[512, 256, 1024]] + [[1024, 256, 1024]] * 36, 'down_sample': True,
                      'down_sample_stride': 2},
                     {"BasicBlock": [[1024, 512, 2048]] + [[2048, 512, 2048]] * 3, 'down_sample': True,
                      'down_sample_stride': 2},
                     ],
               },
    "vgg": {
        11: {"conv1": [64], "pool1": 'M', "conv2": [128], "pool2": "M", "conv3": [256, 256], "pool3": "M",
             "conv4": [512, 512], "pool4": "M", "conv5": [512, 512], "pool5": "M"},
        13: {"conv1": [64, 64], "pool1": 'M', "conv2": [128, 128], "pool2": "M", "conv3": [256, 256], "pool3": "M",
             "conv4": [512, 512], "pool4": "M", "conv5": [512, 512], "pool5": "M"},
        16: {"conv1": [64, 64], "pool1": 'M', "conv2": [128, 128], "pool2": "M", "conv3": [256, 256, 256], "pool3": "M",
             "conv4": [512, 512, 512], "pool4": "M", "conv5": [512, 512, 512], "pool5": "M"},
        19: {"conv1": [64, 64], "pool1": 'M', "conv2": [128, 128], "pool2": "M", "conv3": [256, 256, 256, 256],
             "pool3": "M", "conv4": [512, 512, 512, 512], "pool4": "M", "conv5": [512, 512, 512, 512],
             "pool5": "M"},
        'fc_params': {"linear1": [25088, 4096],'activation1':True, "drop1": True, "linear2": [4096, 4096], 'activation2':True, "drop2": True,
                      "linear3": [4096, 1000]}

    }

}