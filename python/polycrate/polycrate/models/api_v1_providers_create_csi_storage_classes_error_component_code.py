from typing import Literal

ApiV1ProvidersCreateCsiStorageClassesErrorComponentCode = Literal["invalid", "null"]

API_V1_PROVIDERS_CREATE_CSI_STORAGE_CLASSES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProvidersCreateCsiStorageClassesErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_providers_create_csi_storage_classes_error_component_code(
    value: str,
) -> ApiV1ProvidersCreateCsiStorageClassesErrorComponentCode:
    if value in API_V1_PROVIDERS_CREATE_CSI_STORAGE_CLASSES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_CREATE_CSI_STORAGE_CLASSES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
