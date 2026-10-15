from typing import Literal

OrgAPIKeyRequestAccessModeType3Type1 = Literal["", "read", "read_write"]

ORG_API_KEY_REQUEST_ACCESS_MODE_TYPE_3_TYPE_1_VALUES: set[OrgAPIKeyRequestAccessModeType3Type1] = {
    "",
    "read",
    "read_write",
}


def check_org_api_key_request_access_mode_type_3_type_1(value: str) -> OrgAPIKeyRequestAccessModeType3Type1:
    if value in ORG_API_KEY_REQUEST_ACCESS_MODE_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ORG_API_KEY_REQUEST_ACCESS_MODE_TYPE_3_TYPE_1_VALUES!r}"
    )
