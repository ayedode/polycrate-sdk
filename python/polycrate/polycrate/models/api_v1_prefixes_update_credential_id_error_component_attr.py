from typing import Literal

ApiV1PrefixesUpdateCredentialIdErrorComponentAttr = Literal["credential_id"]

API_V1_PREFIXES_UPDATE_CREDENTIAL_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PrefixesUpdateCredentialIdErrorComponentAttr
] = {
    "credential_id",
}


def check_api_v1_prefixes_update_credential_id_error_component_attr(
    value: str,
) -> ApiV1PrefixesUpdateCredentialIdErrorComponentAttr:
    if value in API_V1_PREFIXES_UPDATE_CREDENTIAL_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_UPDATE_CREDENTIAL_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
