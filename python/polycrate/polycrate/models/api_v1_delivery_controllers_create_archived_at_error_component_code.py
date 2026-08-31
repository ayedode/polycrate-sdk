from typing import Literal

ApiV1DeliveryControllersCreateArchivedAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_DELIVERY_CONTROLLERS_CREATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DeliveryControllersCreateArchivedAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_delivery_controllers_create_archived_at_error_component_code(
    value: str,
) -> ApiV1DeliveryControllersCreateArchivedAtErrorComponentCode:
    if value in API_V1_DELIVERY_CONTROLLERS_CREATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_CREATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
