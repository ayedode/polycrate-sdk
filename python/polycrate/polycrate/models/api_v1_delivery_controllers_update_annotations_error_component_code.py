from typing import Literal

ApiV1DeliveryControllersUpdateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_DELIVERY_CONTROLLERS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DeliveryControllersUpdateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_delivery_controllers_update_annotations_error_component_code(
    value: str,
) -> ApiV1DeliveryControllersUpdateAnnotationsErrorComponentCode:
    if value in API_V1_DELIVERY_CONTROLLERS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
