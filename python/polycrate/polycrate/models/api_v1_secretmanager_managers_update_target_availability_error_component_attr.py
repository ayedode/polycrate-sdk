from typing import Literal

ApiV1SecretmanagerManagersUpdateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_SECRETMANAGER_MANAGERS_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersUpdateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_secretmanager_managers_update_target_availability_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersUpdateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
