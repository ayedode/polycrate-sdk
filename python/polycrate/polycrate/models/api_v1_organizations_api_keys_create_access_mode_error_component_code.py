from typing import Literal

ApiV1OrganizationsApiKeysCreateAccessModeErrorComponentCode = Literal["invalid_choice"]

API_V1_ORGANIZATIONS_API_KEYS_CREATE_ACCESS_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsApiKeysCreateAccessModeErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_organizations_api_keys_create_access_mode_error_component_code(
    value: str,
) -> ApiV1OrganizationsApiKeysCreateAccessModeErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_API_KEYS_CREATE_ACCESS_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_API_KEYS_CREATE_ACCESS_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
