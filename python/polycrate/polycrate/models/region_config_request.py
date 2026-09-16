from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.region_loadbalancer_config_request import RegionLoadbalancerConfigRequest
    from ..models.region_s3_config_request import RegionS3ConfigRequest


T = TypeVar("T", bound="RegionConfigRequest")


@_attrs_define
class RegionConfigRequest:
    """
    Attributes:
        s3 (RegionS3ConfigRequest | Unset):
        loadbalancer (RegionLoadbalancerConfigRequest | Unset):
    """

    s3: RegionS3ConfigRequest | Unset = UNSET
    loadbalancer: RegionLoadbalancerConfigRequest | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        s3: dict[str, Any] | Unset = UNSET
        if not isinstance(self.s3, Unset):
            s3 = self.s3.to_dict()

        loadbalancer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.loadbalancer, Unset):
            loadbalancer = self.loadbalancer.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if s3 is not UNSET:
            field_dict["s3"] = s3
        if loadbalancer is not UNSET:
            field_dict["loadbalancer"] = loadbalancer

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.region_loadbalancer_config_request import RegionLoadbalancerConfigRequest  # noqa: PLC0415
        from ..models.region_s3_config_request import RegionS3ConfigRequest  # noqa: PLC0415

        d = dict(src_dict)
        _s3 = d.pop("s3", UNSET)
        s3: RegionS3ConfigRequest | Unset
        if isinstance(_s3, Unset):
            s3 = UNSET
        else:
            s3 = RegionS3ConfigRequest.from_dict(_s3)

        _loadbalancer = d.pop("loadbalancer", UNSET)
        loadbalancer: RegionLoadbalancerConfigRequest | Unset
        if isinstance(_loadbalancer, Unset):
            loadbalancer = UNSET
        else:
            loadbalancer = RegionLoadbalancerConfigRequest.from_dict(_loadbalancer)

        region_config_request = cls(
            s3=s3,
            loadbalancer=loadbalancer,
        )

        region_config_request.additional_properties = d
        return region_config_request

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
