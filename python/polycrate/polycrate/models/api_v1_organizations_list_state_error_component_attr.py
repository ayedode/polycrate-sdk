from typing import Literal

ApiV1OrganizationsListStateErrorComponentAttr = Literal["state"]

API_V1_ORGANIZATIONS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1OrganizationsListStateErrorComponentAttr] = {
    "state",
}


def check_api_v1_organizations_list_state_error_component_attr(
    value: str,
) -> ApiV1OrganizationsListStateErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
