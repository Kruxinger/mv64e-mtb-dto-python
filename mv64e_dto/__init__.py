from pydantic.fields import FieldInfo

def safe_repr(self):
    return f"FieldInfo(annotation={getattr(self, 'annotation', None)}, default={getattr(self, 'default', None)})"

FieldInfo.__repr__ = safe_repr
