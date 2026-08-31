from typing import Literal

ApiV1DeliveryControllersUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_DELIVERY_CONTROLLERS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersUpdateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_delivery_controllers_update_kind_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersUpdateKindErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
