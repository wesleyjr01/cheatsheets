https://docs.python.org/3/tutorial/modules.html

* A Module is  a python file ex: `somefile.py`, it's name is `somefile`.

* Packages are collections of modules. Packages are a way of structuring 
Python’s module namespace by using **dotted module names**. For example, 
the module name `A.B` designates a submodule named B in a package named A.

* Ex:

```
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
```

Note that when using from package import item, the item can be either a submodule (or subpackage) of the package, or some other name defined in the package, like a function, class or variable.

Contrarily, when using syntax like import item.subitem.subsubitem, each item except for the last must be a package; the last item can be a module or a package but can’t be a class or function or variable defined in the previous item.


-----------------  Intra-package References ----------------------   
When packages are structured into subpackages (as with the sound 
package in the example), you can use absolute imports to refer to 
submodules of siblings packages. For example, if the 
module `sound.filters.vocoder` needs to use the echo module in the 
`sound.effects` package, it can use from `sound.effects` import `echo`.

You can also write relative imports, with the from module import name
form of import statement. These imports use leading dots to indicate
the current and parent packages involved in the relative import.
From the surround module for example, you might use:

```
from . import echo
from .. import formats
from ..filters import equalizer
```

Note that relative imports are based on the name of the current module.
Since the name of the main module is always `"__main__"`, modules 
intended for use as the main module of a Python application must always 
use absolute imports.
