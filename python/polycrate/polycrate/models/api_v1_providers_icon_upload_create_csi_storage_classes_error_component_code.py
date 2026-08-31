from typing import Literal

ApiV1ProvidersIconUploadCreateCsiStorageClassesErrorComponentCode = Literal["invalid", "null"]

API_V1_PROVIDERS_ICON_UPLOAD_CREATE_CSI_STORAGE_CLASSES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProvidersIconUploadCreateCsiStorageClassesErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_providers_icon_upload_create_csi_storage_classes_error_component_code(
    value: str,
) -> ApiV1ProvidersIconUploadCreateCsiStorageClassesErrorComponentCode:
    if value in API_V1_PROVIDERS_ICON_UPLOAD_CREATE_CSI_STORAGE_CLASSES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_ICON_UPLOAD_CREATE_CSI_STORAGE_CLASSES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
