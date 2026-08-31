from typing import Literal

ApiV1OrganizationsUpdateCreatedByComponentErrorComponentCode = Literal["invalid_choice"]

API_V1_ORGANIZATIONS_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsUpdateCreatedByComponentErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_organizations_update_created_by_component_error_component_code(
    value: str,
) -> ApiV1OrganizationsUpdateCreatedByComponentErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
