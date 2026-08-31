from typing import Literal

ApiV1OrganizationsListStateNotErrorComponentCode = Literal["invalid_choice"]

API_V1_ORGANIZATIONS_LIST_STATE_NOT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsListStateNotErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_organizations_list_state_not_error_component_code(
    value: str,
) -> ApiV1OrganizationsListStateNotErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_LIST_STATE_NOT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_LIST_STATE_NOT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
