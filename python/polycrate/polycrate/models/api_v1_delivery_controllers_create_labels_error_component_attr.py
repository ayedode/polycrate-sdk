from typing import Literal

ApiV1DeliveryControllersCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_DELIVERY_CONTROLLERS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_delivery_controllers_create_labels_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersCreateLabelsErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
