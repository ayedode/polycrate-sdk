from typing import Literal

ApiV1OrganizationsPartialUpdateEndpointMonitorsErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type", "not_a_list", "null"
]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_ENDPOINT_MONITORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsPartialUpdateEndpointMonitorsErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "not_a_list",
    "null",
}


def check_api_v1_organizations_partial_update_endpoint_monitors_error_component_code(
    value: str,
) -> ApiV1OrganizationsPartialUpdateEndpointMonitorsErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_ENDPOINT_MONITORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_ENDPOINT_MONITORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
