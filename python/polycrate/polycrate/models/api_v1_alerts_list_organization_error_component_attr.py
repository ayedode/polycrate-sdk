from typing import Literal

ApiV1AlertsListOrganizationErrorComponentAttr = Literal["organization"]

API_V1_ALERTS_LIST_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertsListOrganizationErrorComponentAttr] = {
    "organization",
}


def check_api_v1_alerts_list_organization_error_component_attr(
    value: str,
) -> ApiV1AlertsListOrganizationErrorComponentAttr:
    if value in API_V1_ALERTS_LIST_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_LIST_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
