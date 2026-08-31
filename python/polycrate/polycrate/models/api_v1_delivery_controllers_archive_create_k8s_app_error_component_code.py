from typing import Literal

ApiV1DeliveryControllersArchiveCreateK8SAppErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_DELIVERY_CONTROLLERS_ARCHIVE_CREATE_K8S_APP_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DeliveryControllersArchiveCreateK8SAppErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_delivery_controllers_archive_create_k8s_app_error_component_code(
    value: str,
) -> ApiV1DeliveryControllersArchiveCreateK8SAppErrorComponentCode:
    if value in API_V1_DELIVERY_CONTROLLERS_ARCHIVE_CREATE_K8S_APP_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_ARCHIVE_CREATE_K8S_APP_ERROR_COMPONENT_CODE_VALUES!r}"
    )
