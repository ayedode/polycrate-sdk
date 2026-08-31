from typing import Literal

ApiV1ProvidersUpdateCsiStorageClassesErrorComponentCode = Literal["invalid", "null"]

API_V1_PROVIDERS_UPDATE_CSI_STORAGE_CLASSES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProvidersUpdateCsiStorageClassesErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_providers_update_csi_storage_classes_error_component_code(
    value: str,
) -> ApiV1ProvidersUpdateCsiStorageClassesErrorComponentCode:
    if value in API_V1_PROVIDERS_UPDATE_CSI_STORAGE_CLASSES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_UPDATE_CSI_STORAGE_CLASSES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
