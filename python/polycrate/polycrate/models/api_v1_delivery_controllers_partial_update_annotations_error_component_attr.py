from typing import Literal

ApiV1DeliveryControllersPartialUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersPartialUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_delivery_controllers_partial_update_annotations_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersPartialUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
