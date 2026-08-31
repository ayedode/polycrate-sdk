from typing import Literal

ApiV1OrganizationsChoicesListStateErrorComponentAttr = Literal["state"]

API_V1_ORGANIZATIONS_CHOICES_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsChoicesListStateErrorComponentAttr
] = {
    "state",
}


def check_api_v1_organizations_choices_list_state_error_component_attr(
    value: str,
) -> ApiV1OrganizationsChoicesListStateErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_CHOICES_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CHOICES_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
