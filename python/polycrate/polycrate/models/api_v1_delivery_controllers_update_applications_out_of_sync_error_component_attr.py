from typing import Literal

ApiV1DeliveryControllersUpdateApplicationsOutOfSyncErrorComponentAttr = Literal["applications_out_of_sync"]

API_V1_DELIVERY_CONTROLLERS_UPDATE_APPLICATIONS_OUT_OF_SYNC_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersUpdateApplicationsOutOfSyncErrorComponentAttr
] = {
    "applications_out_of_sync",
}


def check_api_v1_delivery_controllers_update_applications_out_of_sync_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersUpdateApplicationsOutOfSyncErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_UPDATE_APPLICATIONS_OUT_OF_SYNC_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_UPDATE_APPLICATIONS_OUT_OF_SYNC_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
