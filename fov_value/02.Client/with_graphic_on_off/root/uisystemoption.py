search this:

			self.fovlevel = 0
			self.fovlevelapplybutton = 0
			self.fovlevelbuttonlist = []


add under this:

			self.fovlevel = 0
			self.fovlevelapplybutton = 0
			self.fovlevelbuttonlist = []

search this:

					self.dropItemLevelButtonList.append(GetObject("dropItem_level%d" % i))

add under this:

					self.fovlevelbuttonlist.append(GetObject("FOV_TYPE%d" % i))

search this:

				self.dropItemLevelApplyButton = GetObject("dropItem_apply")

add under this:


				self.fovlevelapplybutton = GetObject("fovlevel_apply")

search this:

			self.__ClickRadioButton(self.dropItemLevelButtonList, systemSetting.GetDropItemLevel())

add under this:

			self.__ClickRadioButton(self.fovlevelbuttonlist,systemSetting.GetFovValue())

search this:

				self.dropItemLevelButtonList[i].SAFE_SetEvent(self.__OnClickDropItemLevelButton, i)

add under this:

				self.fovlevelbuttonlist[i].SAFE_SetEvent(self.__OnClickFovButton, i)

search this:

			self.dropItemLevelApplyButton.SAFE_SetEvent(self.__OnClickDropItemApplyButton)

add under this:

			self.fovlevelapplybutton.SAFE_SetEvent(self.__OnClickFovApplyButton)


search this:

		# DropItem
		def __OnClickDropItemLevelButton(self, index):
			self.__ClickRadioButton(self.dropItemLevelButtonList, index)
			self.dropItemLevel = index

		def __OnClickDropItemApplyButton(self):
			systemSetting.SetDropItemLevel(self.dropItemLevel)

add under this:

		# fov
		def __OnClickFovButton(self, index):
			self.__ClickRadioButton(self.fovlevelbuttonlist, index)
			self.fovlevel = index
	
		def __OnClickFovApplyButton(self):
			systemSetting.SetFovValue(self.fovlevel)