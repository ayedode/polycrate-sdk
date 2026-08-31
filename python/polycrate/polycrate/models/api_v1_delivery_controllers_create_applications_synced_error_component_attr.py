from typing import Literal

ApiV1DeliveryControllersCreateApplicationsSyncedErrorComponentAttr = Literal["applications_synced"]

API_V1_DELIVERY_CONTROLLERS_CREATE_APPLICATIONS_SYNCED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersCreateApplicationsSyncedErrorComponentAttr
] = {
    "applications_synced",
}


def check_api_v1_delivery_controllers_create_applications_synced_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersCreateApplicationsSyncedErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_CREATE_APPLICATIONS_SYNCED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_CREATE_APPLICATIONS_SYNCED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
