from typing import Literal

PatchedCodeRepositoryRequestCriticalityType2Type1 = Literal["", "high", "low", "medium"]

PATCHED_CODE_REPOSITORY_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[
    PatchedCodeRepositoryRequestCriticalityType2Type1
] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_code_repository_request_criticality_type_2_type_1(
    value: str,
) -> PatchedCodeRepositoryRequestCriticalityType2Type1:
    if value in PATCHED_CODE_REPOSITORY_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_CODE_REPOSITORY_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
