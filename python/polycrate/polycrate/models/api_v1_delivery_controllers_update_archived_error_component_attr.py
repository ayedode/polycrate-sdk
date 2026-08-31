from typing import Literal

ApiV1DeliveryControllersUpdateArchivedErrorComponentAttr = Literal["archived"]

API_V1_DELIVERY_CONTROLLERS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersUpdateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_delivery_controllers_update_archived_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersUpdateArchivedErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
