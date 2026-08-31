from typing import Literal

ApiV1ProvidersIconUploadCreateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_PROVIDERS_ICON_UPLOAD_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersIconUploadCreateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_providers_icon_upload_create_sla_target_error_component_attr(
    value: str,
) -> ApiV1ProvidersIconUploadCreateSlaTargetErrorComponentAttr:
    if value in API_V1_PROVIDERS_ICON_UPLOAD_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_ICON_UPLOAD_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
