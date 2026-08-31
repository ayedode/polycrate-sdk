from typing import Literal

ApiV1DeliveryControllersPartialUpdateApplicationsSyncedErrorComponentAttr = Literal["applications_synced"]

API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_APPLICATIONS_SYNCED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersPartialUpdateApplicationsSyncedErrorComponentAttr
] = {
    "applications_synced",
}


def check_api_v1_delivery_controllers_partial_update_applications_synced_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersPartialUpdateApplicationsSyncedErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_APPLICATIONS_SYNCED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_APPLICATIONS_SYNCED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
