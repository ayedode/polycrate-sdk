from typing import Literal

ApiV1DeliveryControllersPartialUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersPartialUpdateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_delivery_controllers_partial_update_labels_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersPartialUpdateLabelsErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
