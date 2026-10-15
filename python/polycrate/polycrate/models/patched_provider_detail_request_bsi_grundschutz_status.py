from typing import Literal

PatchedProviderDetailRequestBsiGrundschutzStatus = Literal["no", "planned", "unknown", "yes"]

PATCHED_PROVIDER_DETAIL_REQUEST_BSI_GRUNDSCHUTZ_STATUS_VALUES: set[PatchedProviderDetailRequestBsiGrundschutzStatus] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_patched_provider_detail_request_bsi_grundschutz_status(
    value: str,
) -> PatchedProviderDetailRequestBsiGrundschutzStatus:
    if value in PATCHED_PROVIDER_DETAIL_REQUEST_BSI_GRUNDSCHUTZ_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_PROVIDER_DETAIL_REQUEST_BSI_GRUNDSCHUTZ_STATUS_VALUES!r}"
    )
