Search this:

bool CPythonSystem::IsAutoTiling()
{
	if (m_Config.bSoftwareTiling == 0)
		return true;

	return false;
}

add under this:

int CPythonSystem::GetFovValue()
{
	return m_Config.iFovValue;
}

void CPythonSystem::SetFovValue(int fov)
{
	m_Config.iFovValue = fov;
}

search this:

		else if (!stricmp(command, "SHOW_SALESTEXT"))
			m_Config.bShowSalesText = atoi(value) == 1 ? true : false;

add under this:

		else if (!stricmp(command, "FOV_TYPE"))
			m_Config.iFovValue = atoi(value);

search this:

	fprintf(fp, "SHOW_SALESTEXT			%d\n", m_Config.bShowSalesText);

add under this:

	fprintf(fp, "FOV_TYPE					%d\n", m_Config.iFovValue);

search this:

	m_Config.bShowSalesText		= true;

add under this:

	m_Config.iFovValue					= 0;