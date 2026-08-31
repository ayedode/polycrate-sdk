from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.external_traffic_policy_enum import ExternalTrafficPolicyEnum, check_external_traffic_policy_enum
from ..models.region_loadbalancer_config_kind_enum import (
    RegionLoadbalancerConfigKindEnum,
    check_region_loadbalancer_config_kind_enum,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.region_loadbalancer_config_region_config import RegionLoadbalancerConfigRegionConfig


T = TypeVar("T", bound="RegionLoadbalancerConfig")


@_attrs_define
class RegionLoadbalancerConfig:
    """
    Attributes:
        kind (RegionLoadbalancerConfigKindEnum | Unset): * `cilium` - cilium
            * `metallb` - metallb Default: 'cilium'.
        region_name (None | str | Unset): Geografischer Region-Bezeichner, z.B. 'fra1'
        credential (None | Unset | UUID):
        default_product (None | Unset | UUID):
        external_traffic_policy (ExternalTrafficPolicyEnum | Unset): * `Local` - Local
            * `Cluster` - Cluster Default: 'Local'.
        bgp_peer_asn (int | None | Unset):
        bgp_peer_ip (None | str | Unset):
        region_config (RegionLoadbalancerConfigRegionConfig | Unset):
        active (bool | Unset):  Default: True.
    """

    kind: RegionLoadbalancerConfigKindEnum | Unset = "cilium"
    region_name: None | str | Unset = UNSET
    credential: None | Unset | UUID = UNSET
    default_product: None | Unset | UUID = UNSET
    external_traffic_policy: ExternalTrafficPolicyEnum | Unset = "Local"
    bgp_peer_asn: int | None | Unset = UNSET
    bgp_peer_ip: None | str | Unset = UNSET
    region_config: RegionLoadbalancerConfigRegionConfig | Unset = UNSET
    active: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        region_name: None | str | Unset
        if isinstance(self.region_name, Unset):
            region_name = UNSET
        else:
            region_name = self.region_name

        credential: None | str | Unset
        if isinstance(self.credential, Unset):
            credential = UNSET
        elif isinstance(self.credential, UUID):
            credential = str(self.credential)
        else:
            credential = self.credential

        default_product: None | str | Unset
        if isinstance(self.default_product, Unset):
            default_product = UNSET
        elif isinstance(self.default_product, UUID):
            default_product = str(self.default_product)
        else:
            default_product = self.default_product

        external_traffic_policy: str | Unset = UNSET
        if not isinstance(self.external_traffic_policy, Unset):
            external_traffic_policy = self.external_traffic_policy

        bgp_peer_asn: int | None | Unset
        if isinstance(self.bgp_peer_asn, Unset):
            bgp_peer_asn = UNSET
        else:
            bgp_peer_asn = self.bgp_peer_asn

        bgp_peer_ip: None | str | Unset
        if isinstance(self.bgp_peer_ip, Unset):
            bgp_peer_ip = UNSET
        else:
            bgp_peer_ip = self.bgp_peer_ip

        region_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.region_config, Unset):
            region_config = self.region_config.to_dict()

        active = self.active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if region_name is not UNSET:
            field_dict["region_name"] = region_name
        if credential is not UNSET:
            field_dict["credential"] = credential
        if default_product is not UNSET:
            field_dict["default_product"] = default_product
        if external_traffic_policy is not UNSET:
            field_dict["external_traffic_policy"] = external_traffic_policy
        if bgp_peer_asn is not UNSET:
            field_dict["bgp_peer_asn"] = bgp_peer_asn
        if bgp_peer_ip is not UNSET:
            field_dict["bgp_peer_ip"] = bgp_peer_ip
        if region_config is not UNSET:
            field_dict["region_config"] = region_config
        if active is not UNSET:
            field_dict["active"] = active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.region_loadbalancer_config_region_config import RegionLoadbalancerConfigRegionConfig

        d = dict(src_dict)
        _kind = d.pop("kind", UNSET)
        kind: RegionLoadbalancerConfigKindEnum | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_region_loadbalancer_config_kind_enum(_kind)

        def _parse_region_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_name = _parse_region_name(d.pop("region_name", UNSET))

        def _parse_credential(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                credential_type_0 = UUID(data)

                return credential_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        credential = _parse_credential(d.pop("credential", UNSET))

        def _parse_default_product(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                default_product_type_0 = UUID(data)

                return default_product_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        default_product = _parse_default_product(d.pop("default_product", UNSET))

        _external_traffic_policy = d.pop("external_traffic_policy", UNSET)
        external_traffic_policy: ExternalTrafficPolicyEnum | Unset
        if isinstance(_external_traffic_policy, Unset):
            external_traffic_policy = UNSET
        else:
            external_traffic_policy = check_external_traffic_policy_enum(_external_traffic_policy)

        def _parse_bgp_peer_asn(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        bgp_peer_asn = _parse_bgp_peer_asn(d.pop("bgp_peer_asn", UNSET))

        def _parse_bgp_peer_ip(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bgp_peer_ip = _parse_bgp_peer_ip(d.pop("bgp_peer_ip", UNSET))

        _region_config = d.pop("region_config", UNSET)
        region_config: RegionLoadbalancerConfigRegionConfig | Unset
        if isinstance(_region_config, Unset):
            region_config = UNSET
        else:
            region_config = RegionLoadbalancerConfigRegionConfig.from_dict(_region_config)

        active = d.pop("active", UNSET)

        region_loadbalancer_config = cls(
            kind=kind,
            region_name=region_name,
            credential=credential,
            default_product=default_product,
            external_traffic_policy=external_traffic_policy,
            bgp_peer_asn=bgp_peer_asn,
            bgp_peer_ip=bgp_peer_ip,
            region_config=region_config,
            active=active,
        )

        region_loadbalancer_config.additional_properties = d
        return region_loadbalancer_config

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
