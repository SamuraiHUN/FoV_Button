Search this:

void initsystemSetting()

add before this:

PyObject * systemSetFovValue(PyObject * poSelf, PyObject * poArgs)
{
	int fov;
	if (!PyTuple_GetInteger(poArgs, 0, &fov))
		return Py_BuildException();
	CPythonSystem::Instance().SetFovValue(fov);
	return Py_BuildNone();
}
PyObject * systemGetFovValue(PyObject * poSelf, PyObject * poArgs)
{
	return Py_BuildValue("i", CPythonSystem::Instance().GetFovValue());
}

Search:

NULL,

add before this:

