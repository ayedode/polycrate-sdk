from typing import Literal

ContactGroupKindEnum = Literal["dynamic", "generic"]

CONTACT_GROUP_KIND_ENUM_VALUES: set[ContactGroupKindEnum] = {
    "dynamic",
    "generic",
}


def check_contact_group_kind_enum(value: str) -> ContactGroupKindEnum:
    if value in CONTACT_GROUP_KIND_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_GROUP_KIND_ENUM_VALUES!r}")
