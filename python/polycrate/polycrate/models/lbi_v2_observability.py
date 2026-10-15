from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.lbi_v2_observability_metrics_profile import (
    LbiV2ObservabilityMetricsProfile,
    check_lbi_v2_observability_metrics_profile,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="LbiV2Observability")


@_attrs_define
class LbiV2Observability:
    """
    Attributes:
        metrics_profile (LbiV2ObservabilityMetricsProfile | Unset): * `basic` - basic
            * `standard` - standard
            * `full` - full Default: 'standard'.
    """

    metrics_profile: LbiV2ObservabilityMetricsProfile | Unset = "standard"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metrics_profile: str | Unset = UNSET
        if not isinstance(self.metrics_profile, Unset):
            metrics_profile = self.metrics_profile

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metrics_profile is not UNSET:
            field_dict["metricsProfile"] = metrics_profile

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _metrics_profile = d.pop("metricsProfile", UNSET)
        metrics_profile: LbiV2ObservabilityMetricsProfile | Unset
        if isinstance(_metrics_profile, Unset):
            metrics_profile = UNSET
        else:
            metrics_profile = check_lbi_v2_observability_metrics_profile(_metrics_profile)

        lbi_v2_observability = cls(
            metrics_profile=metrics_profile,
        )

        lbi_v2_observability.additional_properties = d
        return lbi_v2_observability

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
