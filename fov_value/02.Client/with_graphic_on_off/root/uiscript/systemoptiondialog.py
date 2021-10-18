search this:

				{
					"name" : "dropItem_apply",
					"type" : "button",

					"x" : 110+105,
					"y" : 50,

					"text" : uiScriptLocale.GRAPHICONOFF_DROP_ITEM_APPLY,

					"default_image" : ROOT_PATH + "middle_Button_01.sub",
					"over_image" : ROOT_PATH + "middle_Button_02.sub",
					"down_image" : ROOT_PATH + "middle_Button_03.sub",
				},


modify to function this:

add under this:

				{
					"name" : "FOV_TYPE",
					"type" : "text",

					"x" : 40 + TEXT_TEMPORARY_X,
					"y" : 75+2,

					"text" : uiScriptLocale.GRAPHICONOFF_FOV_LEVEL, 
				},
				
				{
					"name" : "FOV_TYPE1",
					"type" : "radio_button",

					"x" : 112,
					"y" : 75,

					"text" :  uiScriptLocale.GRAPHICONOFF_FOV_LEVEL1,

					"default_image" : ROOT_PATH + "minimize_empty_button_01.sub",
					"over_image" : ROOT_PATH + "minimize_empty_button_02.sub",
					"down_image" : ROOT_PATH + "minimize_empty_button_03.sub",
				},
				
				{
					"name" : "FOV_TYPE2",
					"type" : "radio_button",

					"x" : 112 + 20,
					"y" : 75,

					"text" :  uiScriptLocale.GRAPHICONOFF_FOV_LEVEL2,

					"default_image" : ROOT_PATH + "minimize_empty_button_01.sub",
					"over_image" : ROOT_PATH + "minimize_empty_button_02.sub",
					"down_image" : ROOT_PATH + "minimize_empty_button_03.sub",
				},
				
				{
					"name" : "FOV_TYPE3",
					"type" : "radio_button",

					"x" : 112 + 40,
					"y" : 75,

					"text" :  uiScriptLocale.GRAPHICONOFF_FOV_LEVEL3,

					"default_image" : ROOT_PATH + "minimize_empty_button_01.sub",
					"over_image" : ROOT_PATH + "minimize_empty_button_02.sub",
					"down_image" : ROOT_PATH + "minimize_empty_button_03.sub",
				},
				
				{
					"name" : "FOV_TYPE4",
					"type" : "radio_button",

					"x" : 112 + 60,
					"y" : 75,

					"text" :  uiScriptLocale.GRAPHICONOFF_FOV_LEVEL4,

					"default_image" : ROOT_PATH + "minimize_empty_button_01.sub",
					"over_image" : ROOT_PATH + "minimize_empty_button_02.sub",
					"down_image" : ROOT_PATH + "minimize_empty_button_03.sub",
				},
				
				{
					"name" : "FOV_TYPE5",
					"type" : "radio_button",

					"x" : 112 + 80,
					"y" : 75,

					"text" :  uiScriptLocale.GRAPHICONOFF_FOV_LEVEL5,

					"default_image" : ROOT_PATH + "minimize_empty_button_01.sub",
					"over_image" : ROOT_PATH + "minimize_empty_button_02.sub",
					"down_image" : ROOT_PATH + "minimize_empty_button_03.sub",
				},
				
				{
					"name" : "fovlevel_apply",
					"type" : "button",

					"x" : 110+105,
					"y" : 75,

					"text" : uiScriptLocale.GRAPHICONOFF_FOV_APPLY,

					"default_image" : ROOT_PATH + "middle_Button_01.sub",
					"over_image" : ROOT_PATH + "middle_Button_02.sub",
					"down_image" : ROOT_PATH + "middle_Button_03.sub",
				},