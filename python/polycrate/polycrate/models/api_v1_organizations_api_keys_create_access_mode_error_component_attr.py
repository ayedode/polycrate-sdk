from typing import Literal

ApiV1OrganizationsApiKeysCreateAccessModeErrorComponentAttr = Literal["access_mode"]

API_V1_ORGANIZATIONS_API_KEYS_CREATE_ACCESS_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsApiKeysCreateAccessModeErrorComponentAttr
] = {
    "access_mode",
}


def check_api_v1_organizations_api_keys_create_access_mode_error_component_attr(
    value: str,
) -> ApiV1OrganizationsApiKeysCreateAccessModeErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_API_KEYS_CREATE_ACCESS_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_API_KEYS_CREATE_ACCESS_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
