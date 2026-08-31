from typing import Literal

ApiV1DeliveryControllersListSearchErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_DELIVERY_CONTROLLERS_LIST_SEARCH_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DeliveryControllersListSearchErrorComponentCode
] = {
    "null_characters_not_allowed",
}


def check_api_v1_delivery_controllers_list_search_error_component_code(
    value: str,
) -> ApiV1DeliveryControllersListSearchErrorComponentCode:
    if value in API_V1_DELIVERY_CONTROLLERS_LIST_SEARCH_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_LIST_SEARCH_ERROR_COMPONENT_CODE_VALUES!r}"
    )
