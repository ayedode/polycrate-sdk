from typing import Literal

ApiV1ProvidersReconcileCreateIconFilenameErrorComponentAttr = Literal["icon_filename"]

API_V1_PROVIDERS_RECONCILE_CREATE_ICON_FILENAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersReconcileCreateIconFilenameErrorComponentAttr
] = {
    "icon_filename",
}


def check_api_v1_providers_reconcile_create_icon_filename_error_component_attr(
    value: str,
) -> ApiV1ProvidersReconcileCreateIconFilenameErrorComponentAttr:
    if value in API_V1_PROVIDERS_RECONCILE_CREATE_ICON_FILENAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_RECONCILE_CREATE_ICON_FILENAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
