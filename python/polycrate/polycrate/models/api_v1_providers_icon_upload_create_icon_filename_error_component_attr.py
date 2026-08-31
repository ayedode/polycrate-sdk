from typing import Literal

ApiV1ProvidersIconUploadCreateIconFilenameErrorComponentAttr = Literal["icon_filename"]

API_V1_PROVIDERS_ICON_UPLOAD_CREATE_ICON_FILENAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersIconUploadCreateIconFilenameErrorComponentAttr
] = {
    "icon_filename",
}


def check_api_v1_providers_icon_upload_create_icon_filename_error_component_attr(
    value: str,
) -> ApiV1ProvidersIconUploadCreateIconFilenameErrorComponentAttr:
    if value in API_V1_PROVIDERS_ICON_UPLOAD_CREATE_ICON_FILENAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_ICON_UPLOAD_CREATE_ICON_FILENAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
