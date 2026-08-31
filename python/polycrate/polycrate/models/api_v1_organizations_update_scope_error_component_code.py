from typing import Literal

ApiV1OrganizationsUpdateScopeErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_ORGANIZATIONS_UPDATE_SCOPE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1OrganizationsUpdateScopeErrorComponentCode] = {
    "invalid_choice",
    "null",
}


def check_api_v1_organizations_update_scope_error_component_code(
    value: str,
) -> ApiV1OrganizationsUpdateScopeErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_UPDATE_SCOPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_SCOPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
