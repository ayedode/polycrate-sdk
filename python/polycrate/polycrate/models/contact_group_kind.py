from typing import Literal

ContactGroupKind = Literal["dynamic", "generic"]

CONTACT_GROUP_KIND_VALUES: set[ContactGroupKind] = {
    "dynamic",
    "generic",
}


def check_contact_group_kind(value: str) -> ContactGroupKind:
    if value in CONTACT_GROUP_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_GROUP_KIND_VALUES!r}")
