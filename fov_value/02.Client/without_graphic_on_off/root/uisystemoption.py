search this:

MUSIC_FILENAME_MAX_LEN = 25

add under this:

FOV_LEVEL_MAX_NUM = 5



search this:

		self.ctrlShadowQuality = 0


add under this:

		self.fovlevel = 0
		self.fovlevelapplybutton = 0
		self.fovlevelbuttonlist = []

search this:

			self.tilingApplyButton = GetObject("tiling_apply")

add under this:

			for i in xrange(1, FOV_LEVEL_MAX_NUM + 1):
				self.fovlevelbuttonlist.append(GetObject("FOV_TYPE%d" % i))


			self.fovlevelapplybutton = GetObject("fovlevel_apply")

search this:

		self.__ClickRadioButton(self.cameraModeButtonList, constInfo.GET_CAMERA_MAX_DISTANCE_INDEX())

add under this:

		self.__ClickRadioButton(self.fovlevelbuttonlist,systemSetting.GetFovValue())

search this:

self.selectMusicFile.SetText(musicInfo.fieldMusic[:MUSIC_FILENAME_MAX_LEN])

add under this:

		for i in xrange(FOV_LEVEL_MAX_NUM):
			self.fovlevelbuttonlist[i].SAFE_SetEvent(self.__OnClickFovButton, i)

		self.fovlevelapplybutton.SAFE_SetEvent(self.__OnClickFovApplyButton)


search this:

		def __DayMode_OnCompleteChangeToDark(self):
			background.RegisterEnvironmentData(1, constInfo.ENVIRONMENT_NIGHT)
			# background.ChangeEnvironmentData(1)
			background.SetEnvironmentData(1)
			self.curtain.FadeIn()

add under this:

		def __OnClickFovButton(self, index):
			self.__ClickRadioButton(self.fovlevelbuttonlist, index)
			self.fovlevel = index
	
		def __OnClickFovApplyButton(self):
			systemSetting.SetFovValue(self.fovlevel)