from typing import Literal

ApiV1DeliveryControllersPartialUpdateSlaTargetErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits"
]

API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_SLA_TARGET_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DeliveryControllersPartialUpdateSlaTargetErrorComponentCode
] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
}


def check_api_v1_delivery_controllers_partial_update_sla_target_error_component_code(
    value: str,
) -> ApiV1DeliveryControllersPartialUpdateSlaTargetErrorComponentCode:
    if value in API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_SLA_TARGET_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_SLA_TARGET_ERROR_COMPONENT_CODE_VALUES!r}"
    )
