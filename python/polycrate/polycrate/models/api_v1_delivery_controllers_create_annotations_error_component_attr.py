from typing import Literal

ApiV1DeliveryControllersCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_DELIVERY_CONTROLLERS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_delivery_controllers_create_annotations_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersCreateAnnotationsErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
