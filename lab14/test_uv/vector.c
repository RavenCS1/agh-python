#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <math.h>

typedef struct {
    PyObject_HEAD
    double x;
    double y;
} Vector2DObject;

static int Vector2D_init(Vector2DObject* self, PyObject* args, PyObject* kwargs){
    static char* kwlist[] = {"x", "y", 0};
    self -> x = 0.0;
    self -> y = 0.0;
    if(!PyArg_ParseTupleAndKeywords(args, kwargs, "|dd", kwlist, &self -> x, &self -> y)){
        PyErr_SetString(PyExc_TypeError, "Vector2D() optionally accepts two doubles");
        return -1;
    }
    return 0;
}

static PyObject* Vector2D_str(Vector2DObject* self){
    char buf[100] = {0};
    snprintf(buf, sizeof(buf), "Vector2D(%g, %g)", self -> x, self -> y);
    return PyUnicode_FromString(buf);
}

static PyObject* Vector2D_scale(Vector2DObject* self, PyObject* args){
    double factor = 0.0;
    if(!PyArg_ParseTuple(args, "d", &factor))
        return 0;
    self -> x *= factor;
    self -> y *= factor;
    Py_RETURN_NONE;
}

static PyObject* Vector2D_magnitude(Vector2DObject* self, PyObject* Py_UNUSED(ignored)){
    return PyFloat_FromDouble(sqrt(self -> x * self -> x + self -> y * self -> y));
}

static PyObject* Vector2D_add(Vector2DObject* self, PyObject* args){
    Vector2DObject* other = 0;
    if(!PyArg_ParseTuple(args, "O!", Py_TYPE(self), (PyObject **) &other))
        return 0;
    self -> x += other -> x;
    self -> y += other -> y;
    Py_RETURN_NONE;
}

static PyMethodDef Vector2D_methods[] = {
    {"scale", (PyCFunction) Vector2D_scale, METH_VARARGS, "Scale the vector by a number"},
    {"magnitude", (PyCFunction) Vector2D_magnitude, METH_VARARGS, "Vector magnitude"},
    {"add", (PyCFunction)Vector2D_add, METH_VARARGS, "Vector addition"},
    {0, 0, 0, 0}
};

static PyTypeObject Vector2DType = {
    PyVarObject_HEAD_INIT(0, 0)
    .tp_name      = "vector.Vector2D",
    .tp_basicsize = sizeof(Vector2DObject),
    .tp_itemsize  = 0,
    .tp_flags     = Py_TPFLAGS_DEFAULT,
    .tp_doc       = "2D vector",
    .tp_methods   = Vector2D_methods,
    .tp_init      = (initproc) Vector2D_init,
    .tp_new       = PyType_GenericNew,
    .tp_str       = (reprfunc) Vector2D_str,
};

static struct PyModuleDef Vector2Dmodule = {
    PyModuleDef_HEAD_INIT, "vector", 0, -1, 0
};

PyMODINIT_FUNC PyInit_vector(void){
    PyObject* m = 0;
    if(PyType_Ready(&Vector2DType) < 0)
        return 0;
    m = PyModule_Create(&Vector2Dmodule);
    if(!m)
        return 0;
    Py_INCREF(&Vector2DType);
    PyModule_AddObject(m, "Vector2D", (PyObject *) &Vector2DType);
    return m;
}
