from typing import Literal

ApiV1DeliveryControllersArchiveCreateApplicationsTotalErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_DELIVERY_CONTROLLERS_ARCHIVE_CREATE_APPLICATIONS_TOTAL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DeliveryControllersArchiveCreateApplicationsTotalErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_delivery_controllers_archive_create_applications_total_error_component_code(
    value: str,
) -> ApiV1DeliveryControllersArchiveCreateApplicationsTotalErrorComponentCode:
    if value in API_V1_DELIVERY_CONTROLLERS_ARCHIVE_CREATE_APPLICATIONS_TOTAL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_ARCHIVE_CREATE_APPLICATIONS_TOTAL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
