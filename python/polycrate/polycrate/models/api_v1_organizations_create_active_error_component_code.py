from typing import Literal

ApiV1OrganizationsCreateActiveErrorComponentCode = Literal["invalid", "null"]

API_V1_ORGANIZATIONS_CREATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsCreateActiveErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_organizations_create_active_error_component_code(
    value: str,
) -> ApiV1OrganizationsCreateActiveErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_CREATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CREATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
