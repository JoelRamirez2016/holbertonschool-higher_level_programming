#include <stdio.h>
#include <Python.h>

void print_python_string(PyObject *p);

/**
 * print_python_string - print description of a Py string
 * @p: python string unicode
 */
void print_python_string(PyObject *p)
{
	Py_ssize_t size;

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
		printf("  length: %lu\n", (size = PyUnicode_GetLength(p)));
		printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &size));
	}
}
