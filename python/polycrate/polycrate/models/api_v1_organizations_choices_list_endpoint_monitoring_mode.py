from typing import Literal

ApiV1OrganizationsChoicesListEndpointMonitoringMode = Literal["auto", "manual"]

API_V1_ORGANIZATIONS_CHOICES_LIST_ENDPOINT_MONITORING_MODE_VALUES: set[
    ApiV1OrganizationsChoicesListEndpointMonitoringMode
] = {
    "auto",
    "manual",
}


def check_api_v1_organizations_choices_list_endpoint_monitoring_mode(
    value: str,
) -> ApiV1OrganizationsChoicesListEndpointMonitoringMode:
    if value in API_V1_ORGANIZATIONS_CHOICES_LIST_ENDPOINT_MONITORING_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CHOICES_LIST_ENDPOINT_MONITORING_MODE_VALUES!r}"
    )
