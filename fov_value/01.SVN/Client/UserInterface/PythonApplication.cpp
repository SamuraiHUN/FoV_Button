search this:

void CPythonApplication::RenderGame()

m_pyGraphic.SetPerspective(30.0f, fAspect, 100.0, fFarClip);

change to:

		int fov_value = CPythonSystem::Instance().GetFovValue();
		if (fov_value == 0)
			m_pyGraphic.SetPerspective(30.0f, fAspect, 100.0, fFarClip);
		else if (fov_value == 1)
			m_pyGraphic.SetPerspective(60.0f, fAspect, 110.0, fFarClip-100.0);
		else if (fov_value == 2)
			m_pyGraphic.SetPerspective(70.0f, fAspect, 115.0, fFarClip-110.0);
		else if (fov_value == 3)
			m_pyGraphic.SetPerspective(85.0f, fAspect, 120.0, fFarClip-120.0);
		else if (fov_value == 4)
			m_pyGraphic.SetPerspective(100.0f, fAspect, 125.0, fFarClip-130.0);
		else
			m_pyGraphic.SetPerspective(30.0f, fAspect, 100.0, fFarClip);


search this:

	m_pyGraphic.SetPerspective(30.0f, fAspect, 100.0, fFarClip);

change to:

	int fov_value = CPythonSystem::Instance().GetFovValue();
	if (fov_value == 0)
		m_pyGraphic.SetPerspective(30.0f, fAspect, 100.0, fFarClip);
	else if (fov_value == 1)
		m_pyGraphic.SetPerspective(60.0f, fAspect, 110.0, fFarClip-100.0);
	else if (fov_value == 2)
		m_pyGraphic.SetPerspective(70.0f, fAspect, 115.0, fFarClip-110.0);
	else if (fov_value == 3)
		m_pyGraphic.SetPerspective(85.0f, fAspect, 120.0, fFarClip-120.0);
	else if (fov_value == 4)
		m_pyGraphic.SetPerspective(100.0f, fAspect, 125.0, fFarClip-130.0);
	else
		m_pyGraphic.SetPerspective(30.0f, fAspect, 100.0, fFarClip);

search this in this function (CPythonApplication::UpdateGame):

		s.SetPerspective(30.0f,fAspect, 100.0f, fFarClip);

change to:



