from typing import Literal

ApiV1DeliveryControllersCreateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_DELIVERY_CONTROLLERS_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersCreateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_delivery_controllers_create_archived_reason_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersCreateArchivedReasonErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
