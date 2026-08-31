from typing import Literal

ApiV1ProvidersIconUploadCreateSloTargetErrorComponentAttr = Literal["slo_target"]

API_V1_PROVIDERS_ICON_UPLOAD_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersIconUploadCreateSloTargetErrorComponentAttr
] = {
    "slo_target",
}


def check_api_v1_providers_icon_upload_create_slo_target_error_component_attr(
    value: str,
) -> ApiV1ProvidersIconUploadCreateSloTargetErrorComponentAttr:
    if value in API_V1_PROVIDERS_ICON_UPLOAD_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_ICON_UPLOAD_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
