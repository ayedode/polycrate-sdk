from typing import Literal

ApiV1ProvidersPartialUpdateIconFilenameErrorComponentAttr = Literal["icon_filename"]

API_V1_PROVIDERS_PARTIAL_UPDATE_ICON_FILENAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersPartialUpdateIconFilenameErrorComponentAttr
] = {
    "icon_filename",
}


def check_api_v1_providers_partial_update_icon_filename_error_component_attr(
    value: str,
) -> ApiV1ProvidersPartialUpdateIconFilenameErrorComponentAttr:
    if value in API_V1_PROVIDERS_PARTIAL_UPDATE_ICON_FILENAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_PARTIAL_UPDATE_ICON_FILENAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
