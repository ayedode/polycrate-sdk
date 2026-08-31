from typing import Literal

ApiV1OrganizationsChoicesListStateNotErrorComponentAttr = Literal["state_not"]

API_V1_ORGANIZATIONS_CHOICES_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsChoicesListStateNotErrorComponentAttr
] = {
    "state_not",
}


def check_api_v1_organizations_choices_list_state_not_error_component_attr(
    value: str,
) -> ApiV1OrganizationsChoicesListStateNotErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_CHOICES_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CHOICES_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
