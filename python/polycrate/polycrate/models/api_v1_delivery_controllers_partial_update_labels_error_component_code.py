from typing import Literal

ApiV1DeliveryControllersPartialUpdateLabelsErrorComponentCode = Literal["invalid"]

API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DeliveryControllersPartialUpdateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_delivery_controllers_partial_update_labels_error_component_code(
    value: str,
) -> ApiV1DeliveryControllersPartialUpdateLabelsErrorComponentCode:
    if value in API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
