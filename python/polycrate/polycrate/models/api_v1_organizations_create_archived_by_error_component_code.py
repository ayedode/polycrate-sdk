from typing import Literal

ApiV1OrganizationsCreateArchivedByErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_ORGANIZATIONS_CREATE_ARCHIVED_BY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsCreateArchivedByErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_organizations_create_archived_by_error_component_code(
    value: str,
) -> ApiV1OrganizationsCreateArchivedByErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_CREATE_ARCHIVED_BY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CREATE_ARCHIVED_BY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
