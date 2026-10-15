from typing import Literal

CodeRepositoryEffectiveCriticalityType1 = Literal["high", "low", "medium"]

CODE_REPOSITORY_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[CodeRepositoryEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_code_repository_effective_criticality_type_1(value: str) -> CodeRepositoryEffectiveCriticalityType1:
    if value in CODE_REPOSITORY_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CODE_REPOSITORY_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
