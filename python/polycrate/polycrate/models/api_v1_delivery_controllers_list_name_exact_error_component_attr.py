from typing import Literal

ApiV1DeliveryControllersListNameExactErrorComponentAttr = Literal["name_exact"]

API_V1_DELIVERY_CONTROLLERS_LIST_NAME_EXACT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersListNameExactErrorComponentAttr
] = {
    "name_exact",
}


def check_api_v1_delivery_controllers_list_name_exact_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersListNameExactErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_LIST_NAME_EXACT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_LIST_NAME_EXACT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
