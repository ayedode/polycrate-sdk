from typing import Literal

ApiV1ProvidersUpdateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_PROVIDERS_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersUpdateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_providers_update_sla_availability_error_component_attr(
    value: str,
) -> ApiV1ProvidersUpdateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_PROVIDERS_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
