from typing import Literal

ApiV1SecretmanagerManagersUpdateSloAvailabilityErrorComponentAttr = Literal["slo_availability"]

API_V1_SECRETMANAGER_MANAGERS_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersUpdateSloAvailabilityErrorComponentAttr
] = {
    "slo_availability",
}


def check_api_v1_secretmanager_managers_update_slo_availability_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersUpdateSloAvailabilityErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
