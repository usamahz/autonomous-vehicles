<h2>Performance Evaluation of Deep Learning Techniques for Object Detection in Autonomous Vehicles.</h2>

Object detection which has seen a rise in recent years being embedded in autonomous cars to perform the localization of objects on roadways by the computer imitating human behaviour and controlling the various blocks of the systems based on the conclusions obtained. The algorithms available which can perform this task are multiple and not all of them are suitable to be deployed in these safety–critical applications, hence the best of them should be chosen, but keeping in mind other challenges as well such as training of these algorithms to be able to perform adequately on the unseen data. Secondly, the main challenge of the ‘training’ phase can be solved to some extent by the pre-trained models available, but they do not guarantee efficient performances on the new data.

Hence, to solve these problems, the algorithms were studied in detail, evaluated and benchmarked against each other, with the use of standard metrics and pre-trained models to find the best performing one. Further, the best performing algorithm was chosen and made suitable to be performed efficiently on the new data by a method, by which a new re-trained model is obtained suitable for a new specific application with the use of previous pre-trained model data. Finally, from the performance results of the new model, it was clear that this technique is effective and could serve as an efficient practice, thus solving the problem.

```json
{
  "type": "excalidraw",
  "version": 2,
  "source": "https://excalidraw.com",
  "elements": [
    {
      "type": "rectangle",
      "version": 79,
      "versionNonce": 1742306192,
      "isDeleted": false,
      "id": "bVflS5usYd8okXrQ16CaQ",
      "fillStyle": "hachure",
      "strokeWidth": 1,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "angle": 0,
      "x": -794.9151528098366,
      "y": -340.3223578713156,
      "strokeColor": "#000000",
      "backgroundColor": "transparent",
      "width": 350,
      "height": 230,
      "seed": 1086430064,
      "groupIds": [],
      "roundness": {
        "type": 3
      },
      "boundElements": [
        {
          "type": "text",
          "id": "QwRRAaXp"
        },
        {
          "id": "FCOxKT6jegMzf0o21eCU7",
          "type": "arrow"
        }
      ],
      "updated": 1676223082071,
      "link": null,
      "locked": false
    },
    {
      "type": "text",
      "version": 45,
      "versionNonce": 1015384976,
      "isDeleted": false,
      "id": "QwRRAaXp",
      "fillStyle": "hachure",
      "strokeWidth": 1,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "angle": 0,
      "x": -686.9151528098366,
      "y": -294.3223578713156,
      "strokeColor": "#000000",
      "backgroundColor": "transparent",
      "width": 134,
      "height": 137,
      "seed": 357985680,
      "groupIds": [],
      "roundness": null,
      "boundElements": [],
      "updated": 1676223162942,
      "link": null,
      "locked": false,
      "fontSize": 36,
      "fontFamily": 1,
      "text": "Pre\nTrained\nModel",
      "rawText": "Pre\nTrained\nModel",
      "baseline": 123,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "bVflS5usYd8okXrQ16CaQ",
      "originalText": "Pre\nTrained\nModel"
    },
    {
      "type": "rectangle",
      "version": 310,
      "versionNonce": 1241283952,
      "isDeleted": false,
      "id": "QMCEAkmYp-y110_09_mDr",
      "fillStyle": "hachure",
      "strokeWidth": 1,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "angle": 0,
      "x": -321.21747560398603,
      "y": -344.2549315420432,
      "strokeColor": "#000000",
      "backgroundColor": "transparent",
      "width": 350,
      "height": 230,
      "seed": 1582082960,
      "groupIds": [],
      "roundness": {
        "type": 3
      },
      "boundElements": [
        {
          "id": "OmZq3QN-mpYi8hIhyzFqS",
          "type": "arrow"
        },
        {
          "type": "text",
          "id": "CZQWnj5H"
        },
        {
          "id": "FCOxKT6jegMzf0o21eCU7",
          "type": "arrow"
        }
      ],
      "updated": 1676223189173,
      "link": null,
      "locked": false
    },
    {
      "type": "text",
      "version": 117,
      "versionNonce": 1076384144,
      "isDeleted": false,
      "id": "CZQWnj5H",
      "fillStyle": "hachure",
      "strokeWidth": 1,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "angle": 0,
      "x": -191.71747560398603,
      "y": -252.2549315420432,
      "strokeColor": "#000000",
      "backgroundColor": "transparent",
      "width": 91,
      "height": 46,
      "seed": 1319829904,
      "groupIds": [],
      "roundness": null,
      "boundElements": [],
      "updated": 1676223189173,
      "link": null,
      "locked": false,
      "fontSize": 36,
      "fontFamily": 1,
      "text": "CNNs",
      "rawText": "CNNs",
      "baseline": 32,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "QMCEAkmYp-y110_09_mDr",
      "originalText": "CNNs"
    },
    {
      "type": "rectangle",
      "version": 334,
      "versionNonce": 242059632,
      "isDeleted": false,
      "id": "rhtxB7rwjtn8HCLdrgqpp",
      "fillStyle": "hachure",
      "strokeWidth": 1,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "angle": 0,
      "x": 141.30424906211488,
      "y": -345.0202607186991,
      "strokeColor": "#000000",
      "backgroundColor": "transparent",
      "width": 350,
      "height": 230,
      "seed": 2060555632,
      "groupIds": [],
      "roundness": {
        "type": 3
      },
      "boundElements": [
        {
          "id": "OmZq3QN-mpYi8hIhyzFqS",
          "type": "arrow"
        },
        {
          "id": "wR2833D17vsYcMf0fGBai",
          "type": "arrow"
        },
        {
          "type": "text",
          "id": "o3jWaxYD"
        }
      ],
      "updated": 1676223194656,
      "link": null,
      "locked": false
    },
    {
      "type": "text",
      "version": 150,
      "versionNonce": 1967504,
      "isDeleted": false,
      "id": "o3jWaxYD",
      "fillStyle": "hachure",
      "strokeWidth": 1,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "angle": 0,
      "x": 227.30424906211488,
      "y": -322.0202607186991,
      "strokeColor": "#000000",
      "backgroundColor": "transparent",
      "width": 178,
      "height": 182,
      "seed": 529906064,
      "groupIds": [],
      "roundness": null,
      "boundElements": [],
      "updated": 1676223194656,
      "link": null,
      "locked": false,
      "fontSize": 36,
      "fontFamily": 1,
      "text": "Best\nPerforming\nAlgorithm\nSelected",
      "rawText": "Best\nPerforming\nAlgorithm\nSelected",
      "baseline": 169,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "rhtxB7rwjtn8HCLdrgqpp",
      "originalText": "Best\nPerforming\nAlgorithm\nSelected"
    },
    {
      "type": "rectangle",
      "version": 296,
      "versionNonce": 578420592,
      "isDeleted": false,
      "id": "FhZ13FAFuuKvs9E5yE-UQ",
      "fillStyle": "hachure",
      "strokeWidth": 1,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "angle": 0,
      "x": 590.5567320144851,
      "y": -346.52230904319066,
      "strokeColor": "#000000",
      "backgroundColor": "transparent",
      "width": 350,
      "height": 230,
      "seed": 80787856,
      "groupIds": [],
      "roundness": {
        "type": 3
      },
      "boundElements": [
        {
          "id": "wR2833D17vsYcMf0fGBai",
          "type": "arrow"
        },
        {
          "type": "text",
          "id": "QLns1lve"
        }
      ],
      "updated": 1676223183106,
      "link": null,
      "locked": false
    },
    {
      "type": "text",
      "version": 92,
      "versionNonce": 1505488784,
      "isDeleted": false,
      "id": "QLns1lve",
      "fillStyle": "hachure",
      "strokeWidth": 1,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "angle": 0,
      "x": 686.5567320144851,
      "y": -300.52230904319066,
      "strokeColor": "#000000",
      "backgroundColor": "transparent",
      "width": 158,
      "height": 137,
      "seed": 998883696,
      "groupIds": [],
      "roundness": null,
      "boundElements": [],
      "updated": 1676223183106,
      "link": null,
      "locked": false,
      "fontSize": 36,
      "fontFamily": 1,
      "text": "Transfer\nLearning\nApplied",
      "rawText": "Transfer\nLearning\nApplied",
      "baseline": 123,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "FhZ13FAFuuKvs9E5yE-UQ",
      "originalText": "Transfer\nLearning\nApplied"
    },
    {
      "type": "arrow",
      "version": 252,
      "versionNonce": 1263349136,
      "isDeleted": false,
      "id": "FCOxKT6jegMzf0o21eCU7",
      "fillStyle": "hachure",
      "strokeWidth": 1,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "angle": 0,
      "x": -443.9151528098366,
      "y": -232.35451326419124,
      "strokeColor": "#000000",
      "backgroundColor": "transparent",
      "width": 117.39771993045997,
      "height": 1.7215240968242256,
      "seed": 818169712,
      "groupIds": [],
      "roundness": {
        "type": 2
      },
      "boundElements": [],
      "updated": 1676223189173,
      "link": null,
      "locked": false,
      "startBinding": {
        "elementId": "bVflS5usYd8okXrQ16CaQ",
        "focus": -0.03796250204394003,
        "gap": 1
      },
      "endBinding": {
        "elementId": "QMCEAkmYp-y110_09_mDr",
        "focus": 0.06349639657258986,
        "gap": 5.299957275390625
      },
      "lastCommittedPoint": null,
      "startArrowhead": null,
      "endArrowhead": "arrow",
      "points": [
        [0, 0],
        [117.39771993045997, -1.7215240968242256]
      ]
    },
    {
      "type": "arrow",
      "version": 687,
      "versionNonce": 1466356624,
      "isDeleted": false,
      "id": "OmZq3QN-mpYi8hIhyzFqS",
      "fillStyle": "hachure",
      "strokeWidth": 1,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "angle": 0,
      "x": 30.15096123954345,
      "y": -228.24413187601192,
      "strokeColor": "#000000",
      "backgroundColor": "transparent",
      "width": 105.36108205191763,
      "height": 2.02047478701445,
      "seed": 2115041648,
      "groupIds": [],
      "roundness": {
        "type": 2
      },
      "boundElements": [],
      "updated": 1676223194656,
      "link": null,
      "locked": false,
      "startBinding": {
        "elementId": "QMCEAkmYp-y110_09_mDr",
        "gap": 1.36843684352944,
        "focus": 0.03725043449957832
      },
      "endBinding": {
        "elementId": "rhtxB7rwjtn8HCLdrgqpp",
        "gap": 5.792205770653742,
        "focus": 0.031357439845209084
      },
      "lastCommittedPoint": null,
      "startArrowhead": null,
      "endArrowhead": "arrow",
      "points": [
        [0, 0],
        [105.36108205191763, -2.02047478701445]
      ]
    },
    {
      "type": "arrow",
      "version": 740,
      "versionNonce": 677765520,
      "isDeleted": false,
      "id": "wR2833D17vsYcMf0fGBai",
      "fillStyle": "hachure",
      "strokeWidth": 1,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "angle": 0,
      "x": 496.5298061130697,
      "y": -230.8177465809532,
      "strokeColor": "#000000",
      "backgroundColor": "transparent",
      "width": 88.00052211351073,
      "height": 1.224905691533479,
      "seed": 1164997488,
      "groupIds": [],
      "roundness": {
        "type": 2
      },
      "boundElements": [],
      "updated": 1676223194656,
      "link": null,
      "locked": false,
      "startBinding": {
        "elementId": "rhtxB7rwjtn8HCLdrgqpp",
        "gap": 5.2255570509548415,
        "focus": -0.028229846187356206
      },
      "endBinding": {
        "elementId": "FhZ13FAFuuKvs9E5yE-UQ",
        "gap": 6.026403787904673,
        "focus": -0.03788645445029888
      },
      "lastCommittedPoint": null,
      "startArrowhead": null,
      "endArrowhead": "arrow",
      "points": [
        [0, 0],
        [88.00052211351073, 1.224905691533479]
      ]
    }
  ],
  "appState": {
    "theme": "dark",
    "viewBackgroundColor": "#ffffff",
    "currentItemStrokeColor": "#000000",
    "currentItemBackgroundColor": "transparent",
    "currentItemFillStyle": "hachure",
    "currentItemStrokeWidth": 1,
    "currentItemStrokeStyle": "solid",
    "currentItemRoughness": 1,
    "currentItemOpacity": 100,
    "currentItemFontFamily": 1,
    "currentItemFontSize": 36,
    "currentItemTextAlign": "left",
    "currentItemStartArrowhead": null,
    "currentItemEndArrowhead": "arrow",
    "scrollX": 1679.9387975434129,
    "scrollY": 1123.8813545566832,
    "zoom": {
      "value": 0.9787226484203204
    },
    "currentItemRoundness": "round",
    "gridSize": null,
    "colorPalette": {},
    "currentStrokeOptions": null,
    "previousGridSize": null
  },
  "files": {}
}
```
