from typing import Literal

ApiV1OrganizationsPartialUpdateActiveErrorComponentCode = Literal["invalid", "null"]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsPartialUpdateActiveErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_organizations_partial_update_active_error_component_code(
    value: str,
) -> ApiV1OrganizationsPartialUpdateActiveErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
