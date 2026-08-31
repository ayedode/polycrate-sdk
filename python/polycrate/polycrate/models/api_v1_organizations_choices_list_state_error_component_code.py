from typing import Literal

ApiV1OrganizationsChoicesListStateErrorComponentCode = Literal["invalid_choice"]

API_V1_ORGANIZATIONS_CHOICES_LIST_STATE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsChoicesListStateErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_organizations_choices_list_state_error_component_code(
    value: str,
) -> ApiV1OrganizationsChoicesListStateErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_CHOICES_LIST_STATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CHOICES_LIST_STATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
