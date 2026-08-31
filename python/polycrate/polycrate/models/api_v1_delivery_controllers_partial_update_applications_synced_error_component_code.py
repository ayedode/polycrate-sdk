from typing import Literal

ApiV1DeliveryControllersPartialUpdateApplicationsSyncedErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_APPLICATIONS_SYNCED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DeliveryControllersPartialUpdateApplicationsSyncedErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_delivery_controllers_partial_update_applications_synced_error_component_code(
    value: str,
) -> ApiV1DeliveryControllersPartialUpdateApplicationsSyncedErrorComponentCode:
    if value in API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_APPLICATIONS_SYNCED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_APPLICATIONS_SYNCED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
