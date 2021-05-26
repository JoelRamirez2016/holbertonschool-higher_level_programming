#include <stdio.h>
#include <Python.h>

void print_python_string(PyObject *p);

void print_python_string(PyObject *p)
{
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
		printf("  length: %lu\n", PyUnicode_GET_SIZE(p));
		printf("  value: %s\n", PyUnicode_AsUTF8(p));
	}
}
