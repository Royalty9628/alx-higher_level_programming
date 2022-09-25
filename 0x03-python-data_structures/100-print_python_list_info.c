#include <stdio.h>
#include <python.h>

/**
 * print_python_list_info - prints python list info
 * @p: pointer to PyObject struct
 * Return: no return
 */

void print_python_list_info(PyObject *p)
{
	long int size, j;
	PyListObject *list;
	PyObject *item;

	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", size);

	list = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", list->allocated);

	for (j = 0; j < size; j++)
	{
		item = PyList_GetItem(p, j);
		printf("Element %ld: %s\n", j, Py_TYPE(item)->tp_name);
	}
}
