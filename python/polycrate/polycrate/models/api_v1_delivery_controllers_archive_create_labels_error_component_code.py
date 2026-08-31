from typing import Literal

ApiV1DeliveryControllersArchiveCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_DELIVERY_CONTROLLERS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DeliveryControllersArchiveCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_delivery_controllers_archive_create_labels_error_component_code(
    value: str,
) -> ApiV1DeliveryControllersArchiveCreateLabelsErrorComponentCode:
    if value in API_V1_DELIVERY_CONTROLLERS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
