#include <stdio.h>
#include <Python.h>

void print_python_string(PyObject *p);

/**
 * print_python_string - print description of a Py string
 * @p: python string unicode
 */
void print_python_string(PyObject *p)
{
	Py_ssize_t len;
	wchar_t *str;

	printf("[.] string object info\n");

	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
	}
	else
	{
		if (PyUnicode_IS_COMPACT_ASCII(p))
			printf("  type: %s\n", "compact ascii");
		else
			printf("  type: %s\n", "compact unicode object");
		printf("  length: %lu\n", (len = PyUnicode_GetLength(p)));
		printf("  value: %ls\n",
			(str = PyUnicode_AsWideCharString(p, &len)));
		PyMem_Free(str);
	}
}
