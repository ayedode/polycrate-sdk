from typing import Literal

ApiV1IpaddressesUpdateSloAvailabilityErrorComponentAttr = Literal["slo_availability"]

API_V1_IPADDRESSES_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IpaddressesUpdateSloAvailabilityErrorComponentAttr
] = {
    "slo_availability",
}


def check_api_v1_ipaddresses_update_slo_availability_error_component_attr(
    value: str,
) -> ApiV1IpaddressesUpdateSloAvailabilityErrorComponentAttr:
    if value in API_V1_IPADDRESSES_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
