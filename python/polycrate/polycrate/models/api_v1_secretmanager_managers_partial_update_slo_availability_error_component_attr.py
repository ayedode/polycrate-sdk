from typing import Literal

ApiV1SecretmanagerManagersPartialUpdateSloAvailabilityErrorComponentAttr = Literal["slo_availability"]

API_V1_SECRETMANAGER_MANAGERS_PARTIAL_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersPartialUpdateSloAvailabilityErrorComponentAttr
] = {
    "slo_availability",
}


def check_api_v1_secretmanager_managers_partial_update_slo_availability_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersPartialUpdateSloAvailabilityErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_PARTIAL_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_PARTIAL_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
