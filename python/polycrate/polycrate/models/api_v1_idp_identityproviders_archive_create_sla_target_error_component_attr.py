from typing import Literal

ApiV1IdpIdentityprovidersArchiveCreateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_IDP_IDENTITYPROVIDERS_ARCHIVE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersArchiveCreateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_idp_identityproviders_archive_create_sla_target_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersArchiveCreateSlaTargetErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_ARCHIVE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_ARCHIVE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
