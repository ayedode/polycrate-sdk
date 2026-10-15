from typing import Literal

OrgAPIKeyAccessModeType1 = Literal["", "read", "read_write"]

ORG_API_KEY_ACCESS_MODE_TYPE_1_VALUES: set[OrgAPIKeyAccessModeType1] = {
    "",
    "read",
    "read_write",
}


def check_org_api_key_access_mode_type_1(value: str) -> OrgAPIKeyAccessModeType1:
    if value in ORG_API_KEY_ACCESS_MODE_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ORG_API_KEY_ACCESS_MODE_TYPE_1_VALUES!r}")
