from typing import Literal

ApiV1DeliveryControllersPartialUpdateApplicationsOutOfSyncErrorComponentAttr = Literal["applications_out_of_sync"]

API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_APPLICATIONS_OUT_OF_SYNC_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersPartialUpdateApplicationsOutOfSyncErrorComponentAttr
] = {
    "applications_out_of_sync",
}


def check_api_v1_delivery_controllers_partial_update_applications_out_of_sync_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersPartialUpdateApplicationsOutOfSyncErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_APPLICATIONS_OUT_OF_SYNC_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_APPLICATIONS_OUT_OF_SYNC_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
