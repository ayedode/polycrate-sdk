from typing import Literal

ApiV1OrganizationsCreateEndpointMonitorsErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type", "not_a_list", "null"
]

API_V1_ORGANIZATIONS_CREATE_ENDPOINT_MONITORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsCreateEndpointMonitorsErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "not_a_list",
    "null",
}


def check_api_v1_organizations_create_endpoint_monitors_error_component_code(
    value: str,
) -> ApiV1OrganizationsCreateEndpointMonitorsErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_CREATE_ENDPOINT_MONITORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CREATE_ENDPOINT_MONITORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
