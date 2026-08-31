from typing import Literal

ApiV1ProvidersReconcileCreateCsiStorageClassesErrorComponentCode = Literal["invalid", "null"]

API_V1_PROVIDERS_RECONCILE_CREATE_CSI_STORAGE_CLASSES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProvidersReconcileCreateCsiStorageClassesErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_providers_reconcile_create_csi_storage_classes_error_component_code(
    value: str,
) -> ApiV1ProvidersReconcileCreateCsiStorageClassesErrorComponentCode:
    if value in API_V1_PROVIDERS_RECONCILE_CREATE_CSI_STORAGE_CLASSES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_RECONCILE_CREATE_CSI_STORAGE_CLASSES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
