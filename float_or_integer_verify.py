def i_or_f(s: str) -> bool:

    if not s.strip():
        return False

    try:
        float(s)
        return True
    except ValueError:
        return False