def audit_vector(path: str) -> dict:
    """
    Inspect a vector dataset and return basic QA metrics.
    """
    raise NotImplementedError


def fix_vector(path: str, out_path: str) -> dict:
    """
    Fix common vector issues (e.g., invalid geometries) and write a cleaned copy.
    """
    raise NotImplementedError
