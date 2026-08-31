from typing import Literal

ApiV1DeliveryControllersCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_DELIVERY_CONTROLLERS_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_delivery_controllers_create_archived_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersCreateArchivedErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
