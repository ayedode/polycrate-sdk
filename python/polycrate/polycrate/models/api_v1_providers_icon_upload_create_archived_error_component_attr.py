from typing import Literal

ApiV1ProvidersIconUploadCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_PROVIDERS_ICON_UPLOAD_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersIconUploadCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_providers_icon_upload_create_archived_error_component_attr(
    value: str,
) -> ApiV1ProvidersIconUploadCreateArchivedErrorComponentAttr:
    if value in API_V1_PROVIDERS_ICON_UPLOAD_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_ICON_UPLOAD_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
