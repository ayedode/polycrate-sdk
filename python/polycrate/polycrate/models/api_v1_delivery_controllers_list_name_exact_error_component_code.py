from typing import Literal

ApiV1DeliveryControllersListNameExactErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_DELIVERY_CONTROLLERS_LIST_NAME_EXACT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DeliveryControllersListNameExactErrorComponentCode
] = {
    "null_characters_not_allowed",
}


def check_api_v1_delivery_controllers_list_name_exact_error_component_code(
    value: str,
) -> ApiV1DeliveryControllersListNameExactErrorComponentCode:
    if value in API_V1_DELIVERY_CONTROLLERS_LIST_NAME_EXACT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_LIST_NAME_EXACT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
