from typing import Optional

try:
    # file is created during dvc build
    from . import _build  # type: ignore[attr-defined, import]

    PKG: Optional[str] = _build.PKG  # type: ignore[assignment]
except ImportError:
    PKG = None  # type: ignore[assignment]
