from typing import Literal

OrganizationScope = Literal["system", "user"]

ORGANIZATION_SCOPE_VALUES: set[OrganizationScope] = {
    "system",
    "user",
}


def check_organization_scope(value: str) -> OrganizationScope:
    if value in ORGANIZATION_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ORGANIZATION_SCOPE_VALUES!r}")
