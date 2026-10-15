from typing import Literal

ContactKind = Literal["generic"]

CONTACT_KIND_VALUES: set[ContactKind] = {
    "generic",
}


def check_contact_kind(value: str) -> ContactKind:
    if value in CONTACT_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_KIND_VALUES!r}")
