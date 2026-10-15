from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pop_catalog_api_type import PopCatalogApiType, check_pop_catalog_api_type
from ..models.pop_catalog_bgp_status import PopCatalogBgpStatus, check_pop_catalog_bgp_status
from ..models.pop_catalog_c5_status import PopCatalogC5Status, check_pop_catalog_c5_status
from ..models.pop_catalog_en_50600_status import PopCatalogEn50600Status, check_pop_catalog_en_50600_status
from ..models.pop_catalog_ipv_6_status import PopCatalogIpv6Status, check_pop_catalog_ipv_6_status
from ..models.pop_catalog_iso_27001_status import PopCatalogIso27001Status, check_pop_catalog_iso_27001_status
from ..models.pop_catalog_kind import PopCatalogKind, check_pop_catalog_kind
from ..models.pop_catalog_scs_iaas_status import PopCatalogScsIaasStatus, check_pop_catalog_scs_iaas_status
from ..models.pop_catalog_scs_kaas_status import PopCatalogScsKaasStatus, check_pop_catalog_scs_kaas_status
from ..models.pop_catalog_tier import PopCatalogTier, check_pop_catalog_tier

if TYPE_CHECKING:
    from ..models.provider_catalog import ProviderCatalog


T = TypeVar("T", bound="PopCatalog")


@_attrs_define
class PopCatalog:
    """Public catalog slice for authenticated non-staff reads.

    Spec: polycrate spec inspect 941. Omits asn, certifications, evidence,
    reachability, procurement, and the non-chip network flags.

        Attributes:
            id (UUID):
            name (str):
            kind (PopCatalogKind): * `datacenter` - Datacenter
                * `datacenter-park` - Datacenter Park
                * `region` - Region
            city (None | str): City where the PoP is located
            country (None | str): ISO 3166-1 alpha-2 country code
            region (None | str): Broader region identifier (e.g., 'Europe', 'North America')
            latitude (None | str): Latitude coordinate
            longitude (None | str): Longitude coordinate
            provider_entity (ProviderCatalog): Public catalog slice for authenticated non-staff reads.

                Spec: polycrate spec inspect 941. Omits contacts, evidence, procurement,
                CCM/CSI, and provider URLs. Staff keep ProviderDetailSerializer.
            iso27001_status (PopCatalogIso27001Status): ISO 27001 status for this PoP.

                * `unknown` - Unknown
                * `no` - No
                * `planned` - Planned
                * `yes` - Yes
            c5_status (PopCatalogC5Status): BSI C5 status for this PoP.

                * `none` - None
                * `planned` - Planned
                * `typ1` - Type 1
                * `typ2` - Type 2
            tier (PopCatalogTier): Site tier. EN 50600 is a separate field.

                * `tier1` - Tier 1
                * `tier2` - Tier 2
                * `tier3` - Tier 3
                * `tier4` - Tier 4
            en50600_status (PopCatalogEn50600Status): EN 50600 status for this PoP.

                * `unknown` - Unknown
                * `no` - No
                * `planned` - Planned
                * `yes` - Yes
            scs_iaas_status (PopCatalogScsIaasStatus): SCS-compatible IaaS status for this PoP.

                * `none` - None
                * `compatible` - Compatible
                * `listed_not_certified` - Listed, not certified
            scs_kaas_status (PopCatalogScsKaasStatus): SCS-compatible KaaS status for this PoP.

                * `none` - None
                * `compatible` - Compatible
                * `listed_not_certified` - Listed, not certified
            technologies (Any): Hypervisors at this PoP: openstack, proxmox, custom, other.
            api_type (PopCatalogApiType): Primary API at this PoP.

                * `openstack` - OpenStack
                * `proxmox` - Proxmox
                * `custom_rest` - Custom REST
                * `none` - None
            bgp_status (PopCatalogBgpStatus): BGP at this PoP.

                * `unknown` - Unknown
                * `no` - No
                * `planned` - Planned
                * `yes` - Yes
            ipv6_status (PopCatalogIpv6Status): IPv6 at this PoP.

                * `unknown` - Unknown
                * `no` - No
                * `planned` - Planned
                * `yes` - Yes
    """

    id: UUID
    name: str
    kind: PopCatalogKind
    city: None | str
    country: None | str
    region: None | str
    latitude: None | str
    longitude: None | str
    provider_entity: ProviderCatalog
    iso27001_status: PopCatalogIso27001Status
    c5_status: PopCatalogC5Status
    tier: PopCatalogTier
    en50600_status: PopCatalogEn50600Status
    scs_iaas_status: PopCatalogScsIaasStatus
    scs_kaas_status: PopCatalogScsKaasStatus
    technologies: Any
    api_type: PopCatalogApiType
    bgp_status: PopCatalogBgpStatus
    ipv6_status: PopCatalogIpv6Status
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        kind: str = self.kind

        city: None | str
        city = self.city

        country: None | str
        country = self.country

        region: None | str
        region = self.region

        latitude: None | str
        latitude = self.latitude

        longitude: None | str
        longitude = self.longitude

        provider_entity = self.provider_entity.to_dict()

        iso27001_status: str = self.iso27001_status

        c5_status: str = self.c5_status

        tier: str = self.tier

        en50600_status: str = self.en50600_status

        scs_iaas_status: str = self.scs_iaas_status

        scs_kaas_status: str = self.scs_kaas_status

        technologies = self.technologies

        api_type: str = self.api_type

        bgp_status: str = self.bgp_status

        ipv6_status: str = self.ipv6_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "kind": kind,
                "city": city,
                "country": country,
                "region": region,
                "latitude": latitude,
                "longitude": longitude,
                "provider_entity": provider_entity,
                "iso27001_status": iso27001_status,
                "c5_status": c5_status,
                "tier": tier,
                "en50600_status": en50600_status,
                "scs_iaas_status": scs_iaas_status,
                "scs_kaas_status": scs_kaas_status,
                "technologies": technologies,
                "api_type": api_type,
                "bgp_status": bgp_status,
                "ipv6_status": ipv6_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.provider_catalog import ProviderCatalog  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        kind = check_pop_catalog_kind(d.pop("kind"))

        def _parse_city(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        city = _parse_city(d.pop("city"))

        def _parse_country(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        country = _parse_country(d.pop("country"))

        def _parse_region(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        region = _parse_region(d.pop("region"))

        def _parse_latitude(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        latitude = _parse_latitude(d.pop("latitude"))

        def _parse_longitude(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        longitude = _parse_longitude(d.pop("longitude"))

        provider_entity = ProviderCatalog.from_dict(d.pop("provider_entity"))

        iso27001_status = check_pop_catalog_iso_27001_status(d.pop("iso27001_status"))

        c5_status = check_pop_catalog_c5_status(d.pop("c5_status"))

        tier = check_pop_catalog_tier(d.pop("tier"))

        en50600_status = check_pop_catalog_en_50600_status(d.pop("en50600_status"))

        scs_iaas_status = check_pop_catalog_scs_iaas_status(d.pop("scs_iaas_status"))

        scs_kaas_status = check_pop_catalog_scs_kaas_status(d.pop("scs_kaas_status"))

        technologies = d.pop("technologies")

        api_type = check_pop_catalog_api_type(d.pop("api_type"))

        bgp_status = check_pop_catalog_bgp_status(d.pop("bgp_status"))

        ipv6_status = check_pop_catalog_ipv_6_status(d.pop("ipv6_status"))

        pop_catalog = cls(
            id=id,
            name=name,
            kind=kind,
            city=city,
            country=country,
            region=region,
            latitude=latitude,
            longitude=longitude,
            provider_entity=provider_entity,
            iso27001_status=iso27001_status,
            c5_status=c5_status,
            tier=tier,
            en50600_status=en50600_status,
            scs_iaas_status=scs_iaas_status,
            scs_kaas_status=scs_kaas_status,
            technologies=technologies,
            api_type=api_type,
            bgp_status=bgp_status,
            ipv6_status=ipv6_status,
        )

        pop_catalog.additional_properties = d
        return pop_catalog

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
