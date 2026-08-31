from typing import Literal

ApiV1DeliveryControllersPartialUpdateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersPartialUpdateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_delivery_controllers_partial_update_archived_at_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersPartialUpdateArchivedAtErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
