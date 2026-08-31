from typing import Literal

ApiV1DeliveryControllersPartialUpdateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersPartialUpdateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_delivery_controllers_partial_update_archived_reason_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersPartialUpdateArchivedReasonErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
