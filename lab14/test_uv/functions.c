#define PY_SSIZE_T_CLEAN
#include <Python.h>

static PyObject* functions_sum_of_squares(PyObject* self, PyObject* args){
    long n = 0;
    if(!PyArg_ParseTuple(args, "l", &n))
        return 0;
    long long result = 0;
    for(register long i = 1; i <= n; ++i)
        result += (long long) (i * i);
    return PyLong_FromLongLong(result);
}

static long long fib(long long n){
    if(n <= 1)
        return n;
    return fib(n - 1) + fib(n - 2);
}

static PyObject* functions_fibonacci(PyObject *self, PyObject *args){
    long n = 0;
    if(!PyArg_ParseTuple(args, "l", &n))
        return 0;
    return PyLong_FromLongLong(fib((long long) n));
}

static PyMethodDef functions_methods[] = {
    {"sum_of_squares", (PyCFunction) functions_sum_of_squares, METH_VARARGS, "Sum of squares"},
    {"fibonacci", (PyCFunction) functions_fibonacci, METH_VARARGS, "N-th term of the Fibonacci sequence"},
    {0, 0, 0, 0}
};

static struct PyModuleDef functionsModule = {
    PyModuleDef_HEAD_INIT , "functions" , 0 , -1, functions_methods
};

PyMODINIT_FUNC PyInit_functions(void){
    return PyModule_Create(&functionsModule);
}