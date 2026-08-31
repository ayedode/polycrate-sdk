from typing import Literal

ApiV1ProvidersUpdateIconFilenameErrorComponentAttr = Literal["icon_filename"]

API_V1_PROVIDERS_UPDATE_ICON_FILENAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersUpdateIconFilenameErrorComponentAttr
] = {
    "icon_filename",
}


def check_api_v1_providers_update_icon_filename_error_component_attr(
    value: str,
) -> ApiV1ProvidersUpdateIconFilenameErrorComponentAttr:
    if value in API_V1_PROVIDERS_UPDATE_ICON_FILENAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_UPDATE_ICON_FILENAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
