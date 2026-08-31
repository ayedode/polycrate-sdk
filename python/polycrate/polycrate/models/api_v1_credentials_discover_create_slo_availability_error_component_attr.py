from typing import Literal

ApiV1CredentialsDiscoverCreateSloAvailabilityErrorComponentAttr = Literal["slo_availability"]

API_V1_CREDENTIALS_DISCOVER_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CredentialsDiscoverCreateSloAvailabilityErrorComponentAttr
] = {
    "slo_availability",
}


def check_api_v1_credentials_discover_create_slo_availability_error_component_attr(
    value: str,
) -> ApiV1CredentialsDiscoverCreateSloAvailabilityErrorComponentAttr:
    if value in API_V1_CREDENTIALS_DISCOVER_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_DISCOVER_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
