from typing import Literal

ApiV1OrganizationsUpdateModifiedByUserErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_ORGANIZATIONS_UPDATE_MODIFIED_BY_USER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsUpdateModifiedByUserErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_organizations_update_modified_by_user_error_component_code(
    value: str,
) -> ApiV1OrganizationsUpdateModifiedByUserErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_UPDATE_MODIFIED_BY_USER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_MODIFIED_BY_USER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
