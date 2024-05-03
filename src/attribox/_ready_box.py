"""The 'readyBox' will dynamically add the attributes required by AttriBox
to the given object. If the given object is a class, the class will
instead be subclassed and provided the required attributes in the
namespace of the subclass. This behaviour may be overridden by providing
'bound=True' as a keyword argument. This will apply the accessor functions
as if defined on the metaclass from which the class is derived."""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations


def readyBox(obj: object, **kwargs) -> None:
  """The 'readyBox' function will dynamically add the attributes required by
  AttriBox to the given object."""
  names = ['__outer_box__', '__owning_instance__', '__field_owner__',
           '__field_name__']
  Names = ['OuterBox', 'OwningInstance', 'FieldOwner', 'FieldName']

  for name in names:
    setattr(obj, name, None)
    setattr(obj, 'get%s' % name[2:], lambda: getattr(obj, name))
    setattr(obj, 'set%s' % name[2:], lambda value: setattr(obj, name, value))
  return None
