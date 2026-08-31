from typing import Literal

ApiV1OrganizationsListEndpointMonitoringMode = Literal["auto", "manual"]

API_V1_ORGANIZATIONS_LIST_ENDPOINT_MONITORING_MODE_VALUES: set[ApiV1OrganizationsListEndpointMonitoringMode] = {
    "auto",
    "manual",
}


def check_api_v1_organizations_list_endpoint_monitoring_mode(
    value: str,
) -> ApiV1OrganizationsListEndpointMonitoringMode:
    if value in API_V1_ORGANIZATIONS_LIST_ENDPOINT_MONITORING_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_LIST_ENDPOINT_MONITORING_MODE_VALUES!r}"
    )
