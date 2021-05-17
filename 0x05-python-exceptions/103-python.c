#include <Python.h>
#include <stdlib.h>
#include <string.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - print some basic info about Python lists Object
 * @p: python object
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *) p;
	PyObject *item;
	int i;

	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
	}
	else
	{
		printf("[*] Size of the Python List = %i\n", (int) PyList_GET_SIZE(list));
		printf("[*] Allocated = %i\n", (int) list->allocated);

		for (i = 0; i < (int) PyList_GET_SIZE(list); i++)
		{
			item = PyList_GET_ITEM(list, i);
			printf("Element %i: %s\n", i, item->ob_type->tp_name);

			if (strcmp(item->ob_type->tp_name, "float") == 0)
				print_python_float(item);
			else if (strcmp(item->ob_type->tp_name, "bytes") == 0)
				print_python_bytes(item);
		}
	}
	fflush(stdout);
}
/**
 * print_python_bytes - print some basic info about Python bytes Object
 * @p: python object
 */
void print_python_bytes(PyObject *p)
{
	PyVarObject *var = (PyVarObject *) p;
	PyBytesObject *bytes = (PyBytesObject *) p;
	int i, size;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
	}
	else
	{
		size = (int) var->ob_size;
		printf("  size: %lu\n", var->ob_size);
		printf("  trying string: %s\n", bytes->ob_sval);
		printf("  first %i bytes:", size + 1> 10 ? 10: size + 1);
		for (i = 0; i <= size && i < 10; i++)
			printf(" %.2hhx", bytes->ob_sval[i]);
		printf("\n");
	}
	fflush(stdout);
}
/**
 * print_python_float - print some basic info about Python float objects
 * @p: python object
 */
void print_python_float(PyObject *p)
{
	PyFloatObject *f = (PyFloatObject *) p;
	char *flt;

	printf("[.] float object info\n");

	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
	}
	else
	{
		flt = PyOS_double_to_string(f->ob_fval, 'r', 0,
				Py_DTSF_ADD_DOT_0, Py_DTST_FINITE);
		printf("  value: %s\n", flt);
		PyMem_Free(flt);
	}
	fflush(stdout);
}
