from typing import Literal

ApiV1CredentialsDiscoverCreateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_CREDENTIALS_DISCOVER_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CredentialsDiscoverCreateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_credentials_discover_create_sla_availability_error_component_attr(
    value: str,
) -> ApiV1CredentialsDiscoverCreateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_CREDENTIALS_DISCOVER_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_DISCOVER_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
