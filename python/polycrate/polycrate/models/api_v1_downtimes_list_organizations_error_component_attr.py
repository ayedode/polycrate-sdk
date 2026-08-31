from typing import Literal

ApiV1DowntimesListOrganizationsErrorComponentAttr = Literal["organizations"]

API_V1_DOWNTIMES_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DowntimesListOrganizationsErrorComponentAttr
] = {
    "organizations",
}


def check_api_v1_downtimes_list_organizations_error_component_attr(
    value: str,
) -> ApiV1DowntimesListOrganizationsErrorComponentAttr:
    if value in API_V1_DOWNTIMES_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
