# comp211-checkoff-3

I explored the idea and process behind using C to write Python extensions. The idea is that by using libraries written in C, we can run Python programs more efficiently.

What I discovered:
Python is an interpreted language and runs more slowly than C due to the Python interpreter. 
Through using extensions like NumPy that are written in C, we are able to perform operations quicker due to:
- Avoiding the Python interpreter
- Cache locality: elements of an array are stored contiguously, making it much easier to access them
- Better memory efficiency: items are stored as basic integers, rather than Python objects

For a pre-existing extension, you just need to install the package and import it in your Python code.

For a custom extension, you must:
- Write the C extension, which contains the C implementation and Python interface
- Write setup.py, a file that tells Python how to compile your C extension
- Compile the C extension using python setup.py build_ext --inplace
- Import and call extension
